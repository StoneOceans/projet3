-- db/create_db.sql
-- Script de création de la table PostgreSQL du projet HR Attrition API
-- À exécuter après avoir créé la base :
-- createdb hr_attrition
-- psql -U postgres -d hr_attrition -f db/create_db.sql

CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    age INTEGER,
    revenu_mensuel FLOAT,
    nombre_experiences_precedentes INTEGER,
    annee_experience_totale INTEGER,
    annees_dans_l_entreprise INTEGER,
    annees_dans_le_poste_actuel INTEGER,
    nombre_participation_pee INTEGER,
    nb_formations_suivies INTEGER,
    distance_domicile_travail INTEGER,
    niveau_education INTEGER,
    annees_depuis_la_derniere_promotion INTEGER,
    annes_sous_responsable_actuel INTEGER,

    satisfaction_employee_environnement INTEGER,
    note_evaluation_precedente INTEGER,
    satisfaction_employee_nature_travail INTEGER,
    satisfaction_employee_equipe INTEGER,
    satisfaction_employee_equilibre_pro_perso INTEGER,
    note_evaluation_actuelle INTEGER,

    heure_supplementaires INTEGER,
    augmentation_salaire_precedente_pct FLOAT,

    genre VARCHAR(50),
    statut_marital VARCHAR(100),
    departement VARCHAR(100),
    poste VARCHAR(150),
    domaine_etude VARCHAR(150),
    frequence_deplacement VARCHAR(100),

    prediction INTEGER,
    probability FLOAT,
    interpretation VARCHAR(255),
    model_version VARCHAR(50)
);

CREATE INDEX IF NOT EXISTS idx_predictions_created_at
ON predictions(created_at);

CREATE INDEX IF NOT EXISTS idx_predictions_prediction
ON predictions(prediction);