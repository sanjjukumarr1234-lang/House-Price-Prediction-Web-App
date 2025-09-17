import pandas as pd
import joblib
import streamlit as st
import os

# -------------------------------
# Load trained model safely
# -------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "House_Price.pkl")

# Load model with joblib
model = joblib.load(model_path)

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("House Price Prediction")
st.header("🏠 House Price Prediction Web App")

# User inputs
area = st.number_input("Enter Area (in sqft)", min_value=500, max_value=20000, value=1000)
beds = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10, value=2)
baths = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=5, value=1)
stories = st.number_input("Enter Number of Stories", min_value=1, max_value=4, value=1)
mainroad = st.selectbox("Main Road", [0, 1])  # 1 = Yes, 0 = No
guestroom = st.selectbox("Guest Room", [0, 1])
basement = st.selectbox("Basement", [0, 1])
hotwaterheating = st.selectbox("Hot Water Heating", [0, 1])
airconditioning = st.selectbox("Air Conditioning", [0, 1])
parking = st.number_input("Number of Parking Spaces", min_value=0, max_value=5, value=1)
prefarea = st.selectbox("Preferred Area", [0, 1])
furnishingstatus = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])

# Encode furnishingstatus same way as training
furnish_map = {"Unfurnished": 0, "Semi-Furnished": 1, "Furnished": 2}
furnishingstatus = furnish_map[furnishingstatus]

# Build input DataFrame
input_data = pd.DataFrame(
    [[area, beds, baths, stories, mainroad, guestroom, basement,
      hotwaterheating, airconditioning, parking, prefarea, furnishingstatus]],
    columns=["area", "bedrooms", "bathrooms", "stories", "mainroad", "guestroom",
             "basement", "hotwaterheating", "airconditioning", "parking",
             "prefarea", "furnishingstatus"]
)

# Prediction button
if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"💰 The predicted price of the house is ₹{prediction[0] * 10000:.0f}")
