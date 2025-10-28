
import streamlit as st
import pandas as pd
import requests

# FastAPI backend URL
url ="https://ml-patient-api.onrender.com/predict"

st.title("Welcome to My Linear Regression Prediction Model")
st.subheader("Please fill in the details below:")

# Input fields
age = st.number_input("Enter your age", min_value=0, step=1)
service = st.number_input("Enter your service [1 to 3]", min_value=1, max_value=3, step=1)
arrival_year = st.number_input("Enter your arrival year", min_value=2025, step=1)
arrival_month = st.number_input("Enter your arrival month", min_value=1, max_value=12, step=1)
arrival_day = st.number_input("Enter your arrival day", min_value=1, max_value=31, step=1)
departure_year = st.number_input("Enter your departure year", min_value=2025, step=1)
departure_month = st.number_input("Enter your departure month", min_value=1, max_value=12, step=1)
departure_day = st.number_input("Enter your departure day", min_value=1, max_value=31, step=1)

# Prediction button
if st.button("Predict Satisfaction Score"):
    # Create a JSON input payload
    user_input = {
        "age": age,
        "service": service,
        "arrival_year": arrival_year,
        "arrival_month": arrival_month,
        "arrival_day": arrival_day,
        "departure_year": departure_year,
        "departure_month": departure_month,
        "departure_day": departure_day
    }

    try:
        # Send POST request to FastAPI backend
        response = requests.post(url, json=user_input)

        if response.status_code == 200:
            result = response.json()
            st.success("✅ Prediction Successful!")
            st.json(result)
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Could not connect to the API: {e}")

