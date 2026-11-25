from fastapi import FastAPI
import joblib, numpy as np
from pydantic import BaseModel


app = FastAPI()
model = joblib.load("model.joblib")


class ImgData(BaseModel):
    pixels: list[float]


@app.get("/")
def runmsg():
    return {"message": "ML API is running"}


@app.post("/predict")
def predict(data: ImgData):
    x = np.array(data.pixels).reshape(1, -1)/255.0
    pred = model.predict(x)
    return {"prediction": int(pred[0])}