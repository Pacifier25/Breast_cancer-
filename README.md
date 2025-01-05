# Breast Cancer Detector <img src="https://github.com/user-attachments/assets/d3d84ba3-55d0-4f1d-80f4-812ff1da65e9" width="20" height="20">

---

## 🌟 Overview
The **Breast Cancer Detector** is an AI-powered tool designed to analyze histopathological images and classify whether cancer is present or not. This project leverages deep learning techniques to deliver highly accurate predictions, making it a valuable tool for early detection and treatment planning.

### 📊 Dataset
This project uses the **BreakHis Dataset**, which contains **9,109 microscopic images** of breast tumor tissue collected from **82 patients**. The images are available at different magnification factors (40X, 100X, 200X, and 400X) and consist of **2,480 benign** and **5,429 malignant** samples in **PNG format** (700x460 pixels, 3-channel RGB). The dataset was developed in collaboration with the **P&D Laboratory – Pathological Anatomy and Cytopathology, Parana, Brazil**.

### 🧠 Model
The model is based on **DenseNet201**, a pre-trained Convolutional Neural Network (CNN) architecture. It has been **fine-tuned with 50 layers** to optimize performance for this dataset. The use of transfer learning allows the model to leverage pre-trained weights, enhancing feature extraction and classification accuracy.

---

## 🎯 Features
- **Upload Image**: Users can upload histopathological images in `.jpg`, `.png`, or `.jpeg` format.  
- **AI-Powered Classification**: Utilizes a pre-trained deep learning model to classify images with high accuracy.  
- **Real-Time Feedback**: Displays classification results along with the confidence percentage.  
- **User-Friendly Interface**: Built with **Streamlit** for an intuitive and interactive experience.  

---

## 🛠️ Technology Stack
- **Programming Language**: Python  
- **Deep Learning Framework**: TensorFlow/Keras  
- **Frontend Framework**: Streamlit  
- **Deployment**: GitHub and Microsoft Azure (upcoming)  

---

## 📂 Folder Structure
```
├── project_files
│   ├── app.py
│   ├── requirements.txt
│   ├── model
│       ├── breast_cancer_model.h5
└── README.md
```

---

## 📊 Results
- **Final Training Accuracy**: **96.33%**  
- **Final Validation Accuracy**: **93.55%**  
- **Model Type**: DenseNet201 (Fine-tuned with 50 layers)  
- **Dataset Used**: [BreakHis Dataset](https://www.kaggle.com/datasets/ambarish/breakhis)  

---

## 📊 Visualizations

### **Training vs Validation Loss**
![image](https://github.com/user-attachments/assets/eb2e46bd-4f41-45ed-9f34-2186998a63df)

### **Training vs Validation Accuracy**
![image](https://github.com/user-attachments/assets/9eb701c3-9ddd-4906-9f95-d28809569d04)

---

## 🎥 Demo Video
[Watch Demo Video](https://drive.google.com/file/d/13kRBsFV0ZZ06bPaCiBW84kv0QuTsNtK4/view?usp=sharing)


---

## 💻 Installation Guide

### Prerequisites
- **Python** 3.7 or later  
- **Virtual Environment** (optional)  

### Steps
1. **Clone the Repository**:
```bash
git clone https://github.com/Pacifier25/Breast_cancer-.git
cd Breast_cancer-
```
2. **Create Virtual Environment**:
```bash
python -m venv env
source env/bin/activate      # For Linux/Mac
env\Scripts\activate         # For Windows
```
3. **Install Dependencies**:
```bash
pip install -r project_files/requirements.txt
```
4. **Run the Application**:
```bash
streamlit run project_files/app.py
```

---

## 🚀 Deployment
The app is currently deployed on Streamlit and will soon be available on Microsoft Azure.

---

## 📥 Download
**[Click here to download the project files](https://github.com/Pacifier25/Breast_cancer-/archive/refs/heads/main.zip)**

---

## 🙏 Acknowledgements
- **Dataset**: Kaggle - [BreakHis Dataset](https://www.kaggle.com/datasets/ambarish/breakhis)  
- **Frameworks**: TensorFlow and Streamlit  
- **Design Elements**: Pink Ribbon Awareness Theme  

---

Thank you for checking out this project! Feel free to contribute or reach out with feedback!
