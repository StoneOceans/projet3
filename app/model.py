import joblib
import pandas as pd


MODEL_PATH = "models/model.pkl"

model = joblib.load(MODEL_PATH)

MODEL_COLUMNS = [
    "age",
    "revenu_mensuel",
    "nombre_experiences_precedentes",
    "annee_experience_totale",
    "annees_dans_l_entreprise",
    "annees_dans_le_poste_actuel",
    "nombre_participation_pee",
    "nb_formations_suivies",
    "distance_domicile_travail",
    "niveau_education",
    "annees_depuis_la_derniere_promotion",
    "annes_sous_responsable_actuel",
    "satisfaction_employee_environnement",
    "note_evaluation_precedente",
    "satisfaction_employee_nature_travail",
    "satisfaction_employee_equipe",
    "satisfaction_employee_equilibre_pro_perso",
    "note_evaluation_actuelle",
    "heure_supplementaires",
    "augmentation_salaire_precedente_pct",
    "satisfaction_moyenne",
    "ecart_note_evaluation",
    "ratio_anciennete_poste",
    "ratio_anciennete_responsable",
    "experience_avant_entreprise",
    "salaire_par_annee_experience",
    "promotion_ancienne",
    "charge_operationnelle_risque",
    "genre_M",
    "statut_marital_Divorcé(e)",
    "statut_marital_Marié(e)",
    "departement_Consulting",
    "departement_Ressources Humaines",
    "poste_Cadre Commercial",
    "poste_Consultant",
    "poste_Directeur Technique",
    "poste_Manager",
    "poste_Représentant Commercial",
    "poste_Senior Manager",
    "poste_Tech Lead",
    "domaine_etude_Entrepreunariat",
    "domaine_etude_Infra & Cloud",
    "domaine_etude_Marketing",
    "domaine_etude_Ressources Humaines",
    "domaine_etude_Transformation Digitale",
    "frequence_deplacement_Frequent",
    "frequence_deplacement_Occasionnel",
]


def predict_attrition(data):
    input_dict = {
        "age": data.age,
        "revenu_mensuel": data.revenu_mensuel,
        "nombre_experiences_precedentes": data.nombre_experiences_precedentes,
        "annee_experience_totale": data.annee_experience_totale,
        "annees_dans_l_entreprise": data.annees_dans_l_entreprise,
        "annees_dans_le_poste_actuel": data.annees_dans_le_poste_actuel,
        "nombre_participation_pee": data.nombre_participation_pee,
        "nb_formations_suivies": data.nb_formations_suivies,
        "distance_domicile_travail": data.distance_domicile_travail,
        "niveau_education": data.niveau_education,
        "annees_depuis_la_derniere_promotion": data.annees_depuis_la_derniere_promotion,
        "annes_sous_responsable_actuel": data.annes_sous_responsable_actuel,
        "satisfaction_employee_environnement": data.satisfaction_employee_environnement,
        "note_evaluation_precedente": data.note_evaluation_precedente,
        "satisfaction_employee_nature_travail": data.satisfaction_employee_nature_travail,
        "satisfaction_employee_equipe": data.satisfaction_employee_equipe,
        "satisfaction_employee_equilibre_pro_perso": data.satisfaction_employee_equilibre_pro_perso,
        "note_evaluation_actuelle": data.note_evaluation_actuelle,
        "heure_supplementaires": data.heure_supplementaires,
        "augmentation_salaire_precedente_pct": data.augmentation_salaire_precedente_pct,
        "satisfaction_moyenne": data.satisfaction_moyenne,
        "ecart_note_evaluation": data.ecart_note_evaluation,
        "ratio_anciennete_poste": data.ratio_anciennete_poste,
        "ratio_anciennete_responsable": data.ratio_anciennete_responsable,
        "experience_avant_entreprise": data.experience_avant_entreprise,
        "salaire_par_annee_experience": data.salaire_par_annee_experience,
        "promotion_ancienne": data.promotion_ancienne,
        "charge_operationnelle_risque": data.charge_operationnelle_risque,
        "genre_M": data.genre_M,
        "statut_marital_Divorcé(e)": data.statut_marital_Divorcé_e,
        "statut_marital_Marié(e)": data.statut_marital_Marié_e,
        "departement_Consulting": data.departement_Consulting,
        "departement_Ressources Humaines": data.departement_Ressources_Humaines,
        "poste_Cadre Commercial": data.poste_Cadre_Commercial,
        "poste_Consultant": data.poste_Consultant,
        "poste_Directeur Technique": data.poste_Directeur_Technique,
        "poste_Manager": data.poste_Manager,
        "poste_Représentant Commercial": data.poste_Représentant_Commercial,
        "poste_Senior Manager": data.poste_Senior_Manager,
        "poste_Tech Lead": data.poste_Tech_Lead,
        "domaine_etude_Entrepreunariat": data.domaine_etude_Entrepreunariat,
        "domaine_etude_Infra & Cloud": data.domaine_etude_Infra_Cloud,
        "domaine_etude_Marketing": data.domaine_etude_Marketing,
        "domaine_etude_Ressources Humaines": data.domaine_etude_Ressources_Humaines,
        "domaine_etude_Transformation Digitale": data.domaine_etude_Transformation_Digitale,
        "frequence_deplacement_Frequent": data.frequence_deplacement_Frequent,
        "frequence_deplacement_Occasionnel": data.frequence_deplacement_Occasionnel,
    }

    df = pd.DataFrame([input_dict])
    df = df[MODEL_COLUMNS]

    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])

    return prediction, probability