# 🩺 Diabetes Prediction with TensorFlow
[![Build](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](#)
[![TensorFlow](https://img.shields.io/badge/framework-TensorFlow-orange)](#)

A deep learning project using **TensorFlow** to predict diabetes occurrence based on medical attributes.  
This project leverages the **Pima Indians Diabetes Dataset** to build, train, and evaluate a classification model.

---

## 📖 Table of Contents
- [Features](#features)
- [Quick Demo](#quick-demo)
- [Installation](#installation)
- [Quickstart](#quickstart)
- [Usage Examples](#usage-examples)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training Recipe](#training-recipe)
- [Evaluation & Results](#evaluation--results)
- [Checkpoints & Export](#checkpoints--export)
- [Inference & Serving](#inference--serving)
- [Reproducibility](#reproducibility)
- [Performance Notes](#performance-notes)
- [Tests & CI](#tests--ci)
- [Responsible Use & Limitations](#responsible-use--limitations)
- [Contribution](#contribution)
- [Citation](#citation)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## 🚀 Features
- Binary classification of diabetes (yes/no).
- TensorFlow/Keras-based deep neural network.
- Includes preprocessing pipeline.
- Supports training, evaluation, and inference.
- Export to ONNX / TensorFlow Lite.
- Reproducible training setup with random seeds.

---

## ⚡ Quick Demo
Run the model in Colab:

```bash
# Clone repo
git clone clone https://github.com/sevugamoorthi/pantech_solution.git
cd Diabetes_Prediction

# Run notebook
jupyter notebook notebooks/diabetes_prediction.ipynb
```

---

## 💻 Installation

### Option A: pip
```bash
pip install -r requirements.txt
```

### Option B: conda
```bash
conda env create -f environment.yml
conda activate diabetes-pred
```

### Option C: Docker
```bash
docker build -t diabetes-pred .
docker run -it diabetes-pred
```

---

## 🔑 Quickstart
Run inference:
```
cd /path/to/your/project_folder/

# Run Jupyter Notebook
python -m notebook
```

---

## 📊 Dataset
- **Source**: Pima Indians Diabetes Dataset (UCI ML Repo).  
- **Features**: pregnancies, glucose, blood pressure, BMI, age, etc.  
- **Target**: Binary outcome (diabetes: 0 or 1).  
- **Download**: [Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)


---

## 🏗️ Model Architecture
- Input layer (8 features).  
- Dense(64, relu) → Dense(32, relu) → Dense(16, relu).  
- Output layer: Dense(1, sigmoid).  
- Loss: Binary crossentropy.  
- Optimizer: Adam.  

---

## ⚙️ Training Recipe
- Epochs: 50  
- Batch size: 32  
- Optimizer: Adam (lr=1e-3)  
- Split: 80/20 train-test  
- Hardware: CPU/GPU  
- Seed: 42  

Reproducibility ensured by fixed seed and deterministic TensorFlow ops.

---

## ✅ Evaluation & Results
Metrics:
- Accuracy: `<PLACEHOLDER>`  
- Precision: `<PLACEHOLDER>`  
- Recall: `<PLACEHOLDER>`  
- AUC: `<PLACEHOLDER>`

Run evaluation:
```bash
python evaluate.py --checkpoint checkpoints/model.h5
```

---

## 📦 Checkpoints & Export
- TensorFlow/Keras checkpoint: `checkpoints/model.h5`
- Export to TFLite:
```bash
python export.py --format tflite
```

---

## 🌐 Inference & Serving
Minimal FastAPI server:
```bash
uvicorn app:app --reload
```

Request:
```bash
curl -X POST http://127.0.0.1:8000/predict      -H "Content-Type: application/json"      -d '{"features": [6,148,72,35,0,33.6,0.627,50]}'
```

---

## 🔁 Reproducibility
- `requirements.txt` and `environment.yml` provided.  
- Training script with fixed seed:  
```bash
python train.py --seed 42
```

---

## ⚡ Performance Notes
- Enable GPU acceleration with CUDA/cuDNN.  
- Use mixed precision for faster training.  
- Normalize input features before training.  

---

## 🧪 Tests & CI
Run tests:
```bash
pytest tests/
```

GitHub Actions workflow included in `.github/workflows/ci.yml`.

---

## 🛡 Responsible Use & Limitations
- This model is trained on a specific dataset; **not a medical diagnostic tool**.  
- Predictions should be used only for **educational purposes**.  
- Consult healthcare professionals for medical advice.  

---

## 🤝 Contribution
1. Fork repo  
2. Create feature branch  
3. Run tests before PR  
4. Submit PR with description  

---

## 📚 Citation
```bibtex
@misc{diabetes_prediction_tf,
  title={Diabetes_Prediction},
  author={Sevugamoorthi},
  year={2025},
  howpublished={\url{https://github.com/sevugamoorthi/pantech_solutions/Diabetes_Prediction}},
  license={Apache-2.0}
}
```

---

## 🙏 Acknowledgements
- UCI Machine Learning Repository  
- TensorFlow team  

---

## 📩 Contact
Author: `sevugamoorthi`  
Email: `sevugamoorthi738@gmail.com>`  
GitHub: `https://github.com/sevugamoorthi`
