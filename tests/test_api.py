from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


VALID_PAYLOAD = {
    "age": 35,
    "revenu_mensuel": 4500,
    "nombre_experiences_precedentes": 2,
    "annee_experience_totale": 10,
    "annees_dans_l_entreprise": 5,
    "annees_dans_le_poste_actuel": 3,
    "nombre_participation_pee": 1,
    "nb_formations_suivies": 2,
    "distance_domicile_travail": 8,
    "niveau_education": 3,
    "annees_depuis_la_derniere_promotion": 1,
    "annes_sous_responsable_actuel": 3,
    "satisfaction_employee_environnement": 3,
    "note_evaluation_precedente": 3,
    "satisfaction_employee_nature_travail": 3,
    "satisfaction_employee_equipe": 3,
    "satisfaction_employee_equilibre_pro_perso": 3,
    "note_evaluation_actuelle": 3,
    "heure_supplementaires": 0,
    "augmentation_salaire_precedente_pct": 12,
    "genre": "M",
    "statut_marital": "Marié(e)",
    "departement": "Consulting",
    "poste": "Consultant",
    "domaine_etude": "Transformation Digitale",
    "frequence_deplacement": "Occasionnel"
}


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "API running"


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True


def test_predict_endpoint():
    response = client.post("/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "probability" in result
    assert "interpretation" in result

    assert result["prediction"] in [0, 1]
    assert 0 <= result["probability"] <= 1


def test_predict_with_invalid_age():
    invalid_payload = VALID_PAYLOAD.copy()
    invalid_payload["age"] = 12

    response = client.post("/predict", json=invalid_payload)

    assert response.status_code == 422


def test_predictions_history_endpoint():
    response = client.get("/predictions")

    assert response.status_code == 200
    assert isinstance(response.json(), list)