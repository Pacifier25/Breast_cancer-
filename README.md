# Breast Cancer Detector


🌟 Overview
The Breast Cancer Detector is an AI-powered tool that analyzes histopathological images to classify whether cancer is present or not. This project uses deep learning techniques to deliver highly accurate predictions, making it a valuable tool in early detection and treatment planning.

🎯 Features
Upload Image: Users can upload histopathological images in .jpg, .png, or .jpeg format.
AI-Powered Classification: Utilizes a pre-trained deep learning model to classify images with high accuracy.
Real-Time Feedback: Displays classification results along with the confidence percentage.
User-Friendly Interface: Built with Streamlit for an intuitive and interactive experience.
🔬 Technology Stack
Programming Language: Python
Deep Learning Framework: TensorFlow/Keras
Frontend Framework: Streamlit
Deployment: GitHub and Microsoft Azure (upcoming)
📂 Folder Structure
graphql
Copy code
.
├── README.md                     # Project documentation
├── breast_cancer_project.ipynb   # Jupyter Notebook for model training
├── project_files/                # Supporting project files
│   ├── app.py                    # Main application script
│   ├── logo.jpg                  # Application logo
│   ├── pink_background.jpg       # UI background image
│   ├── pink_ribbon.jpg           # Breast cancer awareness ribbon
│   ├── requirements.txt          # Dependencies
│   ├── style.css                 # Custom CSS for styling
│   ├── breast_cancer_model.h5    # Pre-trained model
🎨 User Interface

The app features an elegant UI designed with a pink theme to promote breast cancer awareness.

⚡ Results
Accuracy Achieved: 74.59%
Model Type: Convolutional Neural Network (CNN)
Dataset Used: Breast Cancer Histopathological Images
💻 Installation Guide
Prerequisites
Python 3.7 or later
Virtual environment (optional)
Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/Pacifier25/Breast_cancer-.git
cd Breast_cancer-
Set Up Virtual Environment:

bash
Copy code
python -m venv env
source env/bin/activate   # For Linux/Mac
env\Scripts\activate      # For Windows
Install Dependencies:

bash
Copy code
pip install -r project_files/requirements.txt
Run the Application:

bash
Copy code
streamlit run project_files/app.py
🚀 Deployment
The app is deployed on Streamlit and will soon be available on Microsoft Azure.

📥 Model File
The trained model (breast_cancer_model.h5) is tracked using Git LFS and is included in this repository.

📚 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

🙏 Acknowledgements
Dataset: Kaggle - Breast Cancer Histopathology Images
Framework: TensorFlow and Streamlit
Awareness Logo: Pink Ribbon Image
