import streamlit as st
import pickle
import numpy as np
import time

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Streamlit app styling
st.markdown(
    """
    <style>
        body { background-color: #f4f4f4; }
        .main-title { text-align: center; color: #2c3e50; font-size: 36px; font-weight: bold; }
        .sub-text { text-align: center; font-size: 18px; color: #7f8c8d; }
        .stButton > button { width: 100%; background: linear-gradient(to right, #4CAF50, #2ecc71); color: white; }
        .result-box { padding: 20px; border-radius: 10px; text-align: center; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("""
    <h1 class='main-title'>🩺 Diabetes Prediction App</h1>
    <p class='sub-text'>This app predicts the likelihood of diabetes based on patient medical details.</p>
""", unsafe_allow_html=True)

# Sidebar for user inputs
st.sidebar.header("Enter Patient Details 🏥")

pregnancies = st.sidebar.slider('Pregnancies 🤰', 0, 20, 0)
glucose = st.sidebar.slider('Glucose Level 🍬', 0, 300, 120)
blood_pressure = st.sidebar.slider('Blood Pressure 💉', 0, 200, 80)
skin_thickness = st.sidebar.slider('Skin Thickness 📏', 0, 100, 20)
insulin = st.sidebar.slider('Insulin Level 💊', 0, 900, 80)
bmi = st.sidebar.slider('BMI ⚖️', 0.0, 70.0, 25.0, step=0.1)
dpf = st.sidebar.slider('Diabetes Pedigree Function 🧬', 0.0, 3.0, 0.5, step=0.01)
age = st.sidebar.slider('Age 🎂', 0, 120, 30)

# Prediction button
if st.sidebar.button('🔍 Predict Diabetes'):
    # Create input array
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    # Scale the data
    input_data_scaled = scaler.transform(input_data)
    
    # Loading animation
    with st.spinner('Analyzing medical data... ⏳'):
        time.sleep(2)
    
    # Make prediction
    prediction = model.predict(input_data_scaled)
    
    # Display the result with better styling and animations
    if prediction[0] == 1:
        st.markdown("""
            <div class='result-box' style='background-color: #ff4d4d; color: white;'>
                🚨 <strong>Prediction: DIABETES DETECTED!</strong><br> Please consult a medical professional.
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class='result-box' style='background-color: #4CAF50; color: white;'>
                ✅ <strong>Prediction: NO DIABETES!</strong><br> Maintain a healthy lifestyle! 🏃‍♂️🥗
            </div>
        """, unsafe_allow_html=True)