from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.sql import func

from app.database import Base


class PredictionLog(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=False), server_default=func.now())

    age = Column(Integer)
    revenu_mensuel = Column(Float)
    nombre_experiences_precedentes = Column(Integer)
    annee_experience_totale = Column(Integer)
    annees_dans_l_entreprise = Column(Integer)
    annees_dans_le_poste_actuel = Column(Integer)
    nombre_participation_pee = Column(Integer)
    nb_formations_suivies = Column(Integer)
    distance_domicile_travail = Column(Integer)
    niveau_education = Column(Integer)
    annees_depuis_la_derniere_promotion = Column(Integer)
    annes_sous_responsable_actuel = Column(Integer)

    satisfaction_employee_environnement = Column(Integer)
    note_evaluation_precedente = Column(Integer)
    satisfaction_employee_nature_travail = Column(Integer)
    satisfaction_employee_equipe = Column(Integer)
    satisfaction_employee_equilibre_pro_perso = Column(Integer)
    note_evaluation_actuelle = Column(Integer)

    heure_supplementaires = Column(Integer)
    augmentation_salaire_precedente_pct = Column(Float)

    genre = Column(String(50))
    statut_marital = Column(String(100))
    departement = Column(String(100))
    poste = Column(String(150))
    domaine_etude = Column(String(150))
    frequence_deplacement = Column(String(100))

    prediction = Column(Integer)
    probability = Column(Float)
    interpretation = Column(String(255))
    model_version = Column(String(50))