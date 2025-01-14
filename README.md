# Dubai Weather Prediction

This is a simple web application built using Streamlit to predict the average temperature in Dubai based on certain weather-related input parameters. The app takes user input for specific weather variables and sends to a backend API for prediction.

## Features

- User can input the following weather parameters:
  - **Date**: The date for which the prediction is required.
  - **Minimum Temperature**: The minimum temperature on the selected date (in °C).
  - **Maximum Temperature**: The maximum temperature on the selected date (in °C).
  - **Precipitation**: Precipitation for the selected date (in mm).
  - **Wind Speed**: Wind speed for the selected date (in km/h).
  
- The app sends the input data to a prediction API running on `http://localhost:8000/predict` and displays the predicted average temperature for Dubai.

## Requirements

Before running the app, ensure you have the following installed:

- Python 3.6+
- Streamlit
- Requests

You can install the required Python libraries using `pip`:

```bash
pip install streamlit requests
```

Additionally, ensure the prediction API is running locally at `http://localhost:8000/predict` (or update the `API_URL` variable with the appropriate URL if the API is hosted elsewhere).

## How to Run

1. Save the code in a Python file, for example `weather_predictor.py`.
2. Open a terminal/command prompt.
3. Run the following command to start the Streamlit app:

```bash
uvicorn backend:app --reload
```
```bash
streamlit run frontend.py
```

4. The app will open in your default web browser, where you can input the required parameters and click "Predict" to get the predicted average temperature.

## How it Works

1. **User Input**: The app asks the user to provide:
   - Date
   - Minimum Temperature (°C)
   - Maximum Temperature (°C)
   - Precipitation (mm)
   - Wind Speed (km/h)
   
2. **API Request**: Once the user clicks the "Predict" button, the app formats the inputs into a JSON object and sends it as a `POST` request to the specified API URL (`http://localhost:8000/predict`).

3. **Prediction Response**: If the request is successful, the app retrieves the predicted average temperature from the response and displays it to the user. If there is an error in the prediction or API connection, an error message will be shown.

## Code Explanation

### Importing Libraries

```python
import streamlit as st
import requests
```
- `streamlit`: Used to create the user interface of the web app.
- `requests`: Used to send HTTP requests to the prediction API.

### API URL

```python
API_URL = "http://localhost:8000/predict"
```
- This variable stores the URL of the API where the weather prediction request will be sent.

### Streamlit UI

```python
st.title("Dubai Weather Prediction")
st.write("Enter the following details to predict the weather in Dubai:")
```
- `st.title` and `st.write` are used to display the title and description of the web app.

### User Input Widgets

```python
selected_date = st.date_input("Select Date")
tmin = st.number_input("Minimum Temperature (°C)", value=0.00)
tmax = st.number_input("Maximum Temperature (°C)", value=0.00)
prcp = st.number_input("Precipitation (mm)", value=0.00)
wspd = st.number_input("Wind Speed (km/h)", value=0.00)
```
- `st.date_input` allows the user to select a date.
- `st.number_input` provides inputs for temperature, precipitation, and wind speed.

### Handling Button Click

```python
button = st.button("Predict")
```
- `st.button` creates a button that triggers the prediction process when clicked.

### Making the API Request

```python
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
```
- When the user clicks "Predict", the input data is collected and formatted into a dictionary.

### Sending the Request

```python
response = requests.post(API_URL, json=input_data)
```
- The app sends the `POST` request to the API with the user inputs in JSON format.

### Handling the Response

```python
if response.status_code == 200:
    prediction = response.json()['prediction']
    st.success(f"Predicted Average Temperature: {prediction:.2f} °C")
else:
    st.error("Error in prediction.")
```
- If the API response is successful (status code 200), the predicted average temperature is extracted from the response JSON and displayed.
- If there's an error, an error message is shown.

### Error Handling

```python
except Exception as e:
    st.error(f"Failed to connect to server:{e}")
```
- If there’s an exception (e.g., network issues or the API is down), an error message is shown to the user.

## Error Handling

- **API Not Available**: If the prediction API is not running or cannot be reached, the user will see an error message: "Failed to connect to server."
- **Invalid Response**: If the API returns an unexpected response, the app will show "Error in prediction."

## Customization

You can customize the following parts of the app:

- **API_URL**: Update the `API_URL` to point to a different weather prediction API if required.
- **Input Parameters**: Add or modify the input parameters as needed to fit the specific model requirements.

## Troubleshooting

- **API Connection Issues**: Ensure the prediction API is running on the specified URL (`http://localhost:8000/predict`).
- **Invalid Input Values**: Ensure the input values are within realistic ranges for weather data.
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Streamlit for building the interactive web app interface.
- Requests for making HTTP requests to the API.
