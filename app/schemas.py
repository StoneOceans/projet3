from pydantic import BaseModel


class EmployeeInput(BaseModel):
    age: int
    revenu_mensuel: float
    nombre_experiences_precedentes: int
    annee_experience_totale: int
    annees_dans_l_entreprise: int
    annees_dans_le_poste_actuel: int
    nombre_participation_pee: int
    nb_formations_suivies: int
    distance_domicile_travail: int
    niveau_education: int
    annees_depuis_la_derniere_promotion: int
    annes_sous_responsable_actuel: int
    satisfaction_employee_environnement: int
    note_evaluation_precedente: int
    satisfaction_employee_nature_travail: int
    satisfaction_employee_equipe: int
    satisfaction_employee_equilibre_pro_perso: int
    note_evaluation_actuelle: int
    heure_supplementaires: int
    augmentation_salaire_precedente_pct: float
    satisfaction_moyenne: float
    ecart_note_evaluation: float
    ratio_anciennete_poste: float
    ratio_anciennete_responsable: float
    experience_avant_entreprise: int
    salaire_par_annee_experience: float
    promotion_ancienne: int
    charge_operationnelle_risque: int
    genre_M: int
    statut_marital_Divorcé_e: int
    statut_marital_Marié_e: int
    departement_Consulting: int
    departement_Ressources_Humaines: int
    poste_Cadre_Commercial: int
    poste_Consultant: int
    poste_Directeur_Technique: int
    poste_Manager: int
    poste_Représentant_Commercial: int
    poste_Senior_Manager: int
    poste_Tech_Lead: int
    domaine_etude_Entrepreunariat: int
    domaine_etude_Infra_Cloud: int
    domaine_etude_Marketing: int
    domaine_etude_Ressources_Humaines: int
    domaine_etude_Transformation_Digitale: int
    frequence_deplacement_Frequent: int
    frequence_deplacement_Occasionnel: int


class PredictionOutput(BaseModel):
    prediction: int
    probability: float