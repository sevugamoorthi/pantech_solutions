# 🧠 AI & Computer Vision Projects

This repository contains multiple Machine Learning and Computer Vision projects implemented using **Python, OpenCV, TensorFlow/Keras, and Deep Learning models**.  
Each project demonstrates practical applications of AI in real-world scenarios such as image classification, medical prediction, face detection, emotion recognition, and object tracking.

---

## 📂 Projects Overview

### 1. 🐾 Animal Classification using CNN
- **Goal:** Classify animals such as **Cat, Dog, Elephant, Lion, Tiger** using a Convolutional Neural Network (CNN).
- **Process:**
  - Download dataset using `datasetDownloadFromGoogle.py`.
  - Remove duplicate images with `remove_duplicated_image.py`.
  - Rename dataset files using `rename.py`.
  - Train CNN model (`training/training.py`).
  - Test with `testing/test.py` (uses `model.json` and `model.weights.h5`).
- **Tech:** TensorFlow/Keras, OpenCV, Python.

---

### 2. 🩺 Diabetes Prediction using Sequential Model
- **Goal:** Predict whether a patient is diabetic based on medical dataset features.
- **Process:**
  - Load dataset (e.g., PIMA Indians Diabetes Dataset).
  - Build **Sequential Deep Learning Model** with dense layers.
  - Train, validate, and test predictions.
- **Tech:** TensorFlow/Keras (Sequential API), Numpy, Pandas, Scikit-learn.

---

### 3. 👤 Face Detection using Haarcascade
- **Goal:** Detect human faces in images or real-time webcam feed.
- **Process:**
  - Use OpenCV’s **Haar Cascade Classifier** (`haarcascade_frontalface_default.xml`).
  - Detect faces in images/video streams.
  - Draw bounding boxes around detected faces.
- **Tech:** OpenCV.

---

### 4. 🙂 Face Emotion Detection
- **Goal:** Detect and classify human emotions (Happy, Sad, Angry, Neutral, etc.) using facial expressions.
- **Process:**
  - Detect faces using Haar Cascade.
  - Use pre-trained **facial_emotion_recognition** model to classify emotions.
- **Tech:** Keras, OpenCV, Numpy.

---

### 5. 🚶 Moving Object Detection
- **Goal:** Detect and highlight moving objects in video streams or CCTV footage.
- **Process:**
  - Use **frame differencing** and **contour detection** in OpenCV.
  - Highlight moving regions in live video.
- **Tech:** OpenCV.

---

### 6. 📦 Object Recognition using MobileNetSSD
- **Goal:** Detect and recognize multiple objects in real-time.
- **Process:**
  - Load **MobileNetSSD_deploy.prototxt** and **MobileNetSSD_deploy.caffemodel**.
  - Perform real-time object detection (e.g., person, car, chair, dog).
- **Tech:** OpenCV DNN module, Pre-trained MobileNetSSD.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+  
- Virtual Environment (recommended)

### Install Dependencies
```bash
pip install -r requirements.txt
```

Clone Repository
```
git clone https://github.com/sevugamoorthi/pantech_solutions.git
cd project/folder
```

📊 Results & Features

✅ Animal Classification: CNN achieves high accuracy on multi-class dataset.

✅ Diabetes Prediction: Deep learning model predicts risk with good precision.

✅ Face Detection: Real-time face detection with Haarcascade.

✅ Emotion Detection: Recognizes 5+ emotions from webcam input.

✅ Moving Object Detection: Detects and tracks moving objects in videos.

✅ Object Recognition: Identifies 20+ object categories using MobileNetSSD.

📌 Tech Stack

Languages: Python

Libraries: TensorFlow, Keras, OpenCV, NumPy, Pandas, Scikit-learn

Models: CNN, Sequential Deep Learning, Haarcascade, MobileNetSSD

👨‍💻 Author

Developed by Sevugamoorthi
📧 Contact: sevugamoorthi738@gmail.com

🔗 GitHub: [sevugamoorthi](https://github.com/sevugamoorthi/pantech_solutions)