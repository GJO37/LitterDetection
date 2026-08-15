import os, numpy, tensorflow
from datetime import datetime
from keras.utils import load_img, img_to_array
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


MODEL_PATH = r"model.keras"
try:
    model = tensorflow.keras.models.load_model(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    print(f"Error loading model from {MODEL_PATH}: {e}")
    model = None

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

for filename in os.listdir(UPLOAD_FOLDER):
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Could not delete {file_path}: {e}")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img) / 255.0
    return numpy.expand_dims(img_array, axis=0)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Please check server logs.'}), 500

    if 'file' not in request.files:
        return jsonify({'error': 'No files uploaded'}), 400

    files = request.files.getlist('file')
    if not files or all(f.filename == '' for f in files):
        return jsonify({'error': 'No files selected'}), 400

    results = []
    for file in files:
        file_path = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
            unique_filename = f"{timestamp}_{filename}"
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)

            try:
                img_array = preprocess_image(file_path)
                prediction = model.predict(img_array)[0][0]
                label = "Dirty" if prediction > 0.5 else "Clean"
                confidence = prediction if label == "Dirty" else 1 - prediction

                results.append({'label': label, 'confidence': f"{confidence:.2%}",
                                'image_url': f"/static/uploads/{unique_filename}"})
                
            except Exception as e:
                results.append({'label': 'Error', 'confidence': 'N/A',
                                'image_url': None, 'error': str(e)})
                
        else:
            results.append({'label': 'Error', 'confidence': 'N/A',
                            'image_url': None, 'error': f"Invalid file type or no file: {file.filename}"})

    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run()