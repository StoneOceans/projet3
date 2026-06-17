from fastapi import FastAPI
from app.schemas import EmployeeInput, PredictionOutput
from app.model import predict_attrition

app = FastAPI(
    title="HR Attrition API",
    description="API de prédiction du risque d'attrition",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionOutput)
def predict(data: EmployeeInput):

    prediction, probability = predict_attrition(data)

    return {
        "prediction": prediction,
        "probability": probability
    }