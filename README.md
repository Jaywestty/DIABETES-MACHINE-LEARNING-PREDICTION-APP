# 🩺 Diabetes Prediction App

This is a simple and easy-to-use web app built with **Streamlit** that predicts whether a patient has diabetes based on their medical details. Just enter some basic health information, and the app will give you a prediction!

## 📌 Features
- Clean and user-friendly interface.
- Quick diabetes prediction based on input data.
- Visually appealing result display with colors and icons.
- Smooth loading animation for better user experience.
- Uses **pickle** to load a trained machine learning model.

## 🚀 Technologies Used
- Python 🐍
- Streamlit 📊
- Scikit-learn 🤖
- NumPy 🔢
- Pickle 📦

## 📂 Project Structure
```
Diabetes-Prediction-App/
│── model.pkl          # Trained Machine Learning model
│── scaler.pkl         # Scaler for input data normalization
│── app.py            # Streamlit web application
│── README.md         # Project documentation
│── requirements.txt  # Required dependencies
```

## 🛠 Installation
1. Clone the repository:
   ```sh
   [git clone https://github.com/your-username/Diabetes-Prediction-App.git](https://github.com/Jaywestty/DIABETES-MACHINE-LEARNING-PREDICTION-APP.git)
   cd Diabetes-Prediction-App
   ```
2. (Optional but recommended) Set up a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Launch the app:
   ```sh
   streamlit run app.py
   ```

## 🏥 How to Use
1. Open the app in your browser.
2. Enter patient details in the sidebar (e.g., glucose level, BMI, age, etc.).
3. Click the **Predict Diabetes** button.
4. The app will process your input and display the result.


## ⚡ Future Improvements
- Improve model accuracy with better training data.
- Add an API version for easier integration with other apps.
- Store and visualize past predictions for tracking trends.

## 🤝 Contributing
Want to improve the app? Feel free to fork this repo and submit a pull request!

## 📜 License
This project is open-source and available under the MIT License.

---
Developed with ❤️ by FADAIRO OLUWAJUWON

