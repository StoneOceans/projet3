from app.preprocessing import MODEL_COLUMNS, transform_raw_input
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


def test_transform_raw_input_returns_dataframe_with_47_columns():
    data = RawEmployeeInput(**VALID_PAYLOAD)

    df = transform_raw_input(data)

    assert df.shape[0] == 1
    assert df.shape[1] == 47
    assert list(df.columns) == MODEL_COLUMNS


def test_transform_raw_input_creates_business_features():
    data = RawEmployeeInput(**VALID_PAYLOAD)

    df = transform_raw_input(data)

    assert "satisfaction_moyenne" in df.columns
    assert "ecart_note_evaluation" in df.columns
    assert "ratio_anciennete_poste" in df.columns
    assert "salaire_par_annee_experience" in df.columns


def test_transform_raw_input_encodes_categorical_features():
    data = RawEmployeeInput(**VALID_PAYLOAD)

    df = transform_raw_input(data)

    assert df["genre_M"].iloc[0] == 1
    assert df["statut_marital_Marié(e)"].iloc[0] == 1
    assert df["departement_Consulting"].iloc[0] == 1
    assert df["poste_Consultant"].iloc[0] == 1
    assert df["frequence_deplacement_Occasionnel"].iloc[0] == 1