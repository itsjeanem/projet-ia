from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("../models/rf_model.pkl")

@app.post("/predict")
def predict(data: dict):
    features = np.array(list(data.values())).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}