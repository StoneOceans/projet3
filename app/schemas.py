from pydantic import BaseModel, Field


class RawEmployeeInput(BaseModel):
    age: int = Field(..., ge=18, le=70)
    revenu_mensuel: float = Field(..., ge=0)
    nombre_experiences_precedentes: int = Field(..., ge=0)
    annee_experience_totale: int = Field(..., ge=0)
    annees_dans_l_entreprise: int = Field(..., ge=0)
    annees_dans_le_poste_actuel: int = Field(..., ge=0)
    nombre_participation_pee: int = Field(..., ge=0)
    nb_formations_suivies: int = Field(..., ge=0)
    distance_domicile_travail: int = Field(..., ge=0)
    niveau_education: int = Field(..., ge=1, le=5)
    annees_depuis_la_derniere_promotion: int = Field(..., ge=0)
    annes_sous_responsable_actuel: int = Field(..., ge=0)

    satisfaction_employee_environnement: int = Field(..., ge=1, le=4)
    note_evaluation_precedente: int = Field(..., ge=1, le=4)
    satisfaction_employee_nature_travail: int = Field(..., ge=1, le=4)
    satisfaction_employee_equipe: int = Field(..., ge=1, le=4)
    satisfaction_employee_equilibre_pro_perso: int = Field(..., ge=1, le=4)
    note_evaluation_actuelle: int = Field(..., ge=1, le=4)

    heure_supplementaires: int = Field(..., ge=0, le=1)
    augmentation_salaire_precedente_pct: float = Field(..., ge=0)

    genre: str
    statut_marital: str
    departement: str
    poste: str
    domaine_etude: str
    frequence_deplacement: str


class PredictionOutput(BaseModel):
    prediction: int
    probability: float
    interpretation: str