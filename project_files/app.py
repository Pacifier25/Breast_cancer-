import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import base64

# Set the browser tab title and favicon
st.set_page_config(
    page_title="Breast Cancer Detector",  # App name
    page_icon="pink_ribbon.jpg",         # Favicon file
    layout="wide"                         # Wide layout for better spacing
)

# Load the pre-trained model
model = tf.keras.models.load_model('breast_cancer_model.h5')

# Function to set a background image
def set_background(image_file):
    # Encode image to base64
    with open(image_file, "rb") as image:
        encoded_image = base64.b64encode(image.read()).decode()

    # Inject CSS with base64 image as background
    st.markdown(
        f"""
        <style>
        /* General Styling */
        .block-container {{
            padding-top: 0px !important;
            padding-bottom: 0px !important;
        }}
        header {{
            visibility: hidden; /* Hide header */
        }}
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }}
        /* Prediction Text */
        .result-text {{
            font-size: 40px;
            font-weight: bold;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            margin-top: 20px;
        }}
        /* Message Styling */
        .info-text {{
            font-size: 22px;
            color: #333;
            background-color: #f1f1f1;
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply the background image
set_background("pink_background.jpg")  # Background image filename

# Function to load and encode logo
def load_logo(image_file):
    with open(image_file, "rb") as image:
        encoded_logo = base64.b64encode(image.read()).decode()
    return f"data:image/jpeg;base64,{encoded_logo}"

# Load and display logo at the top-center
logo_base64 = load_logo("logo.jpg")  # Replace with your logo file
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{logo_base64}" width="120"> <!-- Adjust width if needed -->
    </div>
    """,
    unsafe_allow_html=True,
)

# Set up the Streamlit App
st.title("Breast Cancer Detector")  # App title
st.write("Upload your image, and our model will classify it as Cancer Detected or No Cancer Detected.")

# Upload Image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Split the screen into two columns
    col1, col2 = st.columns([1, 1])  # 50% for image and 50% for results

    # Display the uploaded image in the left column
    with col1:
        image = Image.open(uploaded_file)

        # Convert RGBA or Grayscale to RGB
        if image.mode == 'RGBA':
            image = image.convert('RGB')  # Convert RGBA to RGB
        elif image.mode == 'L':
            image = image.convert('RGB')  # Convert grayscale to RGB

        # Display the image with a fixed width
        st.image(image, caption="Uploaded Image", width=500)  # Adjust width here

        # Preprocess the image
        img = image.resize((224, 224))  # Resize to model input size
        img_array = np.array(img) / 255.0  # Normalize pixel values
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Make Prediction
        prediction = model.predict(img_array)

    # Confidence levels
    confidence_benign = (1 - prediction[0][0]) * 100
    confidence_malignant = prediction[0][0] * 100

    # Prediction output
    if prediction[0][0] < 0.5:
        result = f"No Cancer Detected ({confidence_benign:.2f}%)"
        message = "Great news! No signs of cancer detected. Stay safe and healthy! 🌸"
        color = "green"  # Green for no cancer
    else:
        result = f"Cancer Detected ({confidence_malignant:.2f}%)"
        message = "Please consult a doctor for further diagnosis and steps. Take care! 💖"
        color = "red"  # Red for cancer detected

    # Display prediction in the right column
    with col2:
        # Display Prediction Result
        st.markdown(
            f'<div class="result-text" style="color: {color}; background-color: #f8f9fa;">{result}</div>',
            unsafe_allow_html=True,
        )
        
        # Add Message Styling
        st.markdown(
            f"""
            <div style="
                font-size: 22px;
                color: {color};
                background-color: #f1f1f1;
                padding: 15px;
                border-radius: 10px;
                margin-top: 10px;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            ">
                {message}
            </div>
            """,
            unsafe_allow_html=True,
        )
