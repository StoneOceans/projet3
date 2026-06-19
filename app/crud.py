import os

from dotenv import load_dotenv
from sqlalchemy.orm import Session

from app.db_models import PredictionLog

load_dotenv()

MODEL_VERSION = os.getenv("MODEL_VERSION", "1.0.0")


def save_prediction(
    db: Session,
    data,
    prediction: int,
    probability: float,
    interpretation: str
):
    raw_data = data.model_dump()

    db_prediction = PredictionLog(
        **raw_data,
        prediction=prediction,
        probability=probability,
        interpretation=interpretation,
        model_version=MODEL_VERSION
    )

    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)

    return db_prediction


def get_predictions(db: Session, limit: int = 20):
    return (
        db.query(PredictionLog)
        .order_by(PredictionLog.created_at.desc())
        .limit(limit)
        .all()
    )