from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.crud import get_predictions, save_prediction
from app.database import Base, engine, get_db
from app.model import predict_attrition
from app.schemas import PredictionOutput, RawEmployeeInput

Base.metadata.create_all(bind=engine)

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
        "model_loaded": True,
        "database": "connected"
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(data: RawEmployeeInput, db: Session = Depends(get_db)):
    prediction, probability = predict_attrition(data)

    interpretation = (
        "Risque élevé de départ"
        if prediction == 1
        else "Risque faible de départ"
    )

    save_prediction(
        db=db,
        data=data,
        prediction=prediction,
        probability=probability,
        interpretation=interpretation
    )

    return {
        "prediction": prediction,
        "probability": probability,
        "interpretation": interpretation
    }


@app.get("/predictions")
def predictions_history(limit: int = 20, db: Session = Depends(get_db)):
    return get_predictions(db=db, limit=limit)