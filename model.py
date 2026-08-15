import os, numpy
from sklearn.model_selection import train_test_split
from keras.utils import load_img, img_to_array
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential


dataset_dir = "dataset"
images = []
labels = []

classes = {"clean": 0, "dirty": 1}

for class_name, label in classes.items():
    folder = os.path.join(dataset_dir, class_name)
    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(folder, filename)
            img = load_img(img_path, target_size=(224, 224))
            img_array = img_to_array(img) / 255.0
            images.append(img_array)
            labels.append(label)

images = numpy.array(images)
labels = numpy.array(labels)

if images.size == 0 or labels.size == 0:
    raise ValueError("No images found. Check the dataset path and file names.")

X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)
print(f"Training Samples: {len(X_train)}, Testing Samples: {len(X_test)}")

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(X_train, y_train, epochs=10, batch_size=16, validation_data=(X_test, y_test))
model.save("model.keras")

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")