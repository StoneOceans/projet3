from app.model import predict_attrition
from app.schemas import RawEmployeeInput


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


def test_model_prediction_output_format():
    data = RawEmployeeInput(**VALID_PAYLOAD)

    prediction, probability = predict_attrition(data)

    assert prediction in [0, 1]
    assert isinstance(probability, float)
    assert 0 <= probability <= 1