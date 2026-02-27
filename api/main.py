from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../models/rf_model.pkl")

class FlowData(BaseModel):
    features: list

@app.post("/predict")
def predict(data: FlowData):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}