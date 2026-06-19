import joblib

from app.preprocessing import transform_raw_input


MODEL_PATH = "models/model.pkl"

model = joblib.load(MODEL_PATH)


def predict_attrition(data):
    df = transform_raw_input(data)

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return prediction, probability