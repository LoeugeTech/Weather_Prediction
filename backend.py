from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Load the model
model_path = "model/Dubai_Weather_LR_Model.joblib"

try:
    model = joblib.load(model_path)
except Exception as e:
    raise Exception(status_code=500, detail=str(e))

app = FastAPI()

class WeatherData(BaseModel):
    day: int
    month: int
    year: int
    tmin: float
    tmax: float
    prcp: float
    wspd: float

@app.get("/health")
def health_check():
    return {"status": "OK", "message": "API is running"}

@app.post("/predict")
def predict(data: WeatherData):
    try:
        input_data = np.array([data.day, data.month, data.year, data.tmin, data.tmax, data.prcp, data.wspd])
        prediction = model.predict([input_data])
        return {"prediction": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Error in prediction: {str(e)}')
