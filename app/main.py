from fastapi import FastAPI

from app.schemas import RawEmployeeInput, PredictionOutput
from app.model import predict_attrition

app = FastAPI(
    title="HR Attrition API",
    description="API de prédiction du risque d'attrition à partir de données brutes.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "API running"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(data: RawEmployeeInput):
    prediction, probability = predict_attrition(data)

    interpretation = (
        "Risque élevé de départ"
        if prediction == 1
        else "Risque faible de départ"
    )

    return {
        "prediction": prediction,
        "probability": probability,
        "interpretation": interpretation
    }