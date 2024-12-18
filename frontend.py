import streamlit as st
import requests

API_URL = "http://localhost:8000/predict"

st.title("Dubai Weather Prediction")
st.write("Enter the following details to predict the weather in Dubai:")

# Input for user
selected_date = st.date_input("Select Date")

day = selected_date.day
month = selected_date.month
year = selected_date.year

tmin = st.number_input("Minimum Temperature (°C)", value=0.00)
tmax = st.number_input("Maximum Temperature (°C)", value=0.00)
prcp = st.number_input("Precipitation (mm)", value=0.00)
wspd = st.number_input("Wind Speed (km/h)", value=0.00)

# Make prediction
button = st.button("Predict")

if button:
    input_data = {
        "day": day,
        "month": month,
        "year": year,
        "tmin": tmin,
        "tmax": tmax,
        "prcp": prcp,
        "wspd": wspd
    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            prediction = response.json()['prediction']
            st.success(f"Predicted Average Temperature: {prediction:.2f} °C")
        else:
            st.error("Error in prediction.")

    except Exception as e:
        st.error(f"Failed to connect to server:{e}")