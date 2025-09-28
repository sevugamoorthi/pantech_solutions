# 🐾 Animal Classification using CNN  
A Convolutional Neural Network (CNN) based image classification project to classify animals into **Cat, Dog, Elephant, Lion, and Tiger**.  

This project covers the full pipeline:  
1. **Dataset preparation** (download, cleaning, renaming)  
2. **Model training**  
3. **Model testing & inference**  

## 🚀 Getting Started  

### 1. Clone Repository  
```bash
git clone https://github.com/sevugamoorthi/pantech_solution.git
cd Animal_Classification
```

Optional dataset
Get the dataset from [here](https://drive.google.com/drive/folders/1F_T6BBRMXgnYT-0WPfPoaE6mYNAM-ekd?usp=sharing)

📸 Dataset Preparation
Step 1: Download Images

Use datasetDownloadFromGoogle.py to download images for each class (Cat, Dog, Elephant, Lion, Tiger).
```
python datasetDownloadFromGoogle.py
```
Step 2: Remove Duplicates

Run the duplicate remover script:
```
python remove_duplicated_image.py
```

Step 3: Rename Images

To keep dataset consistent:
```
python rename.py
```

Now you have a clean dataset ready for training.

🧠 Training the Model

Navigate to the training folder and run:
```
cd training
python training.py
```

This will:

Build a CNN model

Train it on your dataset

Save the model as model.json and weights as model.weights.h5 inside the testing folder

folder

🔍 Testing the Model

Move to the testing folder:
```
cd testing
python test.py
```

This script will:

Load model.json and model.weights.h5

Test the model on new images

Print predictions for Cat, Dog, Elephant, Lion, Tiger

📊 Results & Accuracy

The CNN model can achieve high accuracy depending on the dataset quality and size.

You can further improve performance using data augmentation, transfer learning (e.g., VGG16, ResNet), or fine-tuning.

🛠 Future Improvements

Add more animal classes

Use pre-trained models for better accuracy

Deploy model as a web app using Flask/Streamlit

Build a real-time animal classifier with OpenCV

👨‍💻 Author

Developed by Sevugamoorthi

📧 Email: sevugamoorthi738@gmail.com

🌐 GitHub: [sevugamoorthi](https://github.com/sevugamoorthi)