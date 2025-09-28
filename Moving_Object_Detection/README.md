# Moving Object Detection

A Python project for **detecting moving objects** in videos or webcam streams using **OpenCV**.  
This project demonstrates motion detection by comparing consecutive frames and highlighting moving objects with bounding boxes.

---
## 📌 Features
- Detects moving objects in **real-time** from webcam or video files.
- Highlights moving objects with **rectangles**.
- Adjustable **sensitivity** using parameters like threshold and contour area.
- Can be extended for **security, surveillance, or traffic monitoring** applications.
---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sevugamoorthi/pantech_solutions.git
   cd Moving_Object_Detection
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
python moving_object_detection.py
```

