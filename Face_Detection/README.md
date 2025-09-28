# Haar Cascade Face Detection

A simple **face detection project** using the [Haar Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) with **OpenCV**.  
This project demonstrates how to detect human faces in images or video streams using the `haarcascade_frontalface_default.xml` pre-trained model.

---

## 📌 Features
- Detects human faces in images and video.
- Uses OpenCV’s **Haar Cascade Classifier**.
- Works in **real-time webcam detection** or with static images.
- Lightweight and easy to integrate into other projects.

---

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sevugamoorthi/pantech_solutions.git
   cd Face_Detection
   ```

## Create and activate a virtual environment (recommended):
 ```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:
```
pip install -r requirements.txt
```

## 🚀 Usage

Detect faces
```
python face_detection.py
```

