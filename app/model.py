def predict_attrition(data):

    probability = 0.72

    prediction = 1 if probability > 0.5 else 0

    return prediction, probability