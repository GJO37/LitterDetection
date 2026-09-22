# 🗑️ **LITTER DETECTION**

An AI-powered web application designed for real-time image classification as **Clean** or **Dirty** using a deep learning model built with TensorFlow/Keras. 
The application is lightweight, easy to use, and supports image formats such as `.jpg`, `.jpeg` and `.png`.


## 🚀 FEATURES

### 🤖 **AI Classification**
* Binary image classification
* Deep learning model
* Real-time inference

### 🖼️ **Image Processing**
* Automatic preprocessing pipeline
* Normalization and resizing

### 🌐 **Web Interface**
* User-friendly interface
* Instant prediction results


## 🧱 ARCHITECTURE OVERVIEW

```
LitterDetection/
│
├── templates/          # HTML templates
├── static/             # CSS, images and uploads
├── dataset/            # Training dataset
├── model.keras         # Trained model
├── model.py            # Training script
└── app.py              # Flask backend
```


## 🖥️ INSTALLATION

1. Run:
```bash
git clone https://github.com/GJO37/LitterDetection.git
cd LitterDetection
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
```bash
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python app.py
```


## 🛒 PREREQUISITES

* Make sure to provide correct path of the datasets to both `model.py` and `app.py`
* The trained model is not included in the repository. To train the model, open `main.ipynb` notebook and train the model
* After training, the model should be saved as `model_weights.pt` in the root directory


## 🧭 HOW TO USE

1. Launch the Flask application
2. Open the web interface
3. Upload an image and analyze
4. View the Analysis result


## ⚙️ TECH STACK

* **Python 3.14**
* **NumPy**  – Numerical computation
* **Pillow** – Image processing
* **Flask**  – Web framework
* **TensorFlow / Keras** – Deep learning logics
* **HTML & CSS** – Frontend development
