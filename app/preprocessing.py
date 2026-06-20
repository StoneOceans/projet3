import pandas as pd


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


def transform_raw_input(data):
    row = data.model_dump()

    transformed = {}

    transformed["age"] = row["age"]
    transformed["revenu_mensuel"] = row["revenu_mensuel"]
    transformed["nombre_experiences_precedentes"] = row["nombre_experiences_precedentes"]
    transformed["annee_experience_totale"] = row["annee_experience_totale"]
    transformed["annees_dans_l_entreprise"] = row["annees_dans_l_entreprise"]
    transformed["annees_dans_le_poste_actuel"] = row["annees_dans_le_poste_actuel"]
    transformed["nombre_participation_pee"] = row["nombre_participation_pee"]
    transformed["nb_formations_suivies"] = row["nb_formations_suivies"]
    transformed["distance_domicile_travail"] = row["distance_domicile_travail"]
    transformed["niveau_education"] = row["niveau_education"]
    transformed["annees_depuis_la_derniere_promotion"] = row["annees_depuis_la_derniere_promotion"]
    transformed["annes_sous_responsable_actuel"] = row["annes_sous_responsable_actuel"]
    transformed["satisfaction_employee_environnement"] = row["satisfaction_employee_environnement"]
    transformed["note_evaluation_precedente"] = row["note_evaluation_precedente"]
    transformed["satisfaction_employee_nature_travail"] = row["satisfaction_employee_nature_travail"]
    transformed["satisfaction_employee_equipe"] = row["satisfaction_employee_equipe"]
    transformed["satisfaction_employee_equilibre_pro_perso"] = row["satisfaction_employee_equilibre_pro_perso"]
    transformed["note_evaluation_actuelle"] = row["note_evaluation_actuelle"]
    transformed["heure_supplementaires"] = row["heure_supplementaires"]
    transformed["augmentation_salaire_precedente_pct"] = row["augmentation_salaire_precedente_pct"]

    transformed["satisfaction_moyenne"] = (
        row["satisfaction_employee_environnement"]
        + row["satisfaction_employee_nature_travail"]
        + row["satisfaction_employee_equipe"]
        + row["satisfaction_employee_equilibre_pro_perso"]
    ) / 4

    transformed["ecart_note_evaluation"] = (
        row["note_evaluation_actuelle"] - row["note_evaluation_precedente"]
    )

    transformed["ratio_anciennete_poste"] = (
        row["annees_dans_le_poste_actuel"] / row["annees_dans_l_entreprise"]
        if row["annees_dans_l_entreprise"] > 0
        else 0
    )

    transformed["ratio_anciennete_responsable"] = (
        row["annes_sous_responsable_actuel"] / row["annees_dans_l_entreprise"]
        if row["annees_dans_l_entreprise"] > 0
        else 0
    )

    transformed["experience_avant_entreprise"] = (
        row["annee_experience_totale"] - row["annees_dans_l_entreprise"]
    )

    transformed["salaire_par_annee_experience"] = (
        row["revenu_mensuel"] / row["annee_experience_totale"]
        if row["annee_experience_totale"] > 0
        else row["revenu_mensuel"]
    )

    transformed["promotion_ancienne"] = (
        1 if row["annees_depuis_la_derniere_promotion"] >= 5 else 0
    )

    transformed["charge_operationnelle_risque"] = (
        1
        if row["heure_supplementaires"] == 1
        and row["satisfaction_employee_equilibre_pro_perso"] <= 2
        else 0
    )

    transformed["genre_M"] = 1 if row["genre"] == "M" else 0

    transformed["statut_marital_Divorcé(e)"] = (
        1 if row["statut_marital"] == "Divorcé(e)" else 0
    )
    transformed["statut_marital_Marié(e)"] = (
        1 if row["statut_marital"] == "Marié(e)" else 0
    )

    transformed["departement_Consulting"] = (
        1 if row["departement"] == "Consulting" else 0
    )
    transformed["departement_Ressources Humaines"] = (
        1 if row["departement"] == "Ressources Humaines" else 0
    )

    transformed["poste_Cadre Commercial"] = (
        1 if row["poste"] == "Cadre Commercial" else 0
    )
    transformed["poste_Consultant"] = (
        1 if row["poste"] == "Consultant" else 0
    )
    transformed["poste_Directeur Technique"] = (
        1 if row["poste"] == "Directeur Technique" else 0
    )
    transformed["poste_Manager"] = (
        1 if row["poste"] == "Manager" else 0
    )
    transformed["poste_Représentant Commercial"] = (
        1 if row["poste"] == "Représentant Commercial" else 0
    )
    transformed["poste_Senior Manager"] = (
        1 if row["poste"] == "Senior Manager" else 0
    )
    transformed["poste_Tech Lead"] = (
        1 if row["poste"] == "Tech Lead" else 0
    )

    transformed["domaine_etude_Entrepreunariat"] = (
        1 if row["domaine_etude"] == "Entrepreunariat" else 0
    )
    transformed["domaine_etude_Infra & Cloud"] = (
        1 if row["domaine_etude"] == "Infra & Cloud" else 0
    )
    transformed["domaine_etude_Marketing"] = (
        1 if row["domaine_etude"] == "Marketing" else 0
    )
    transformed["domaine_etude_Ressources Humaines"] = (
        1 if row["domaine_etude"] == "Ressources Humaines" else 0
    )
    transformed["domaine_etude_Transformation Digitale"] = (
        1 if row["domaine_etude"] == "Transformation Digitale" else 0
    )

    transformed["frequence_deplacement_Frequent"] = (
        1 if row["frequence_deplacement"] == "Frequent" else 0
    )
    transformed["frequence_deplacement_Occasionnel"] = (
        1 if row["frequence_deplacement"] == "Occasionnel" else 0
    )

    df = pd.DataFrame([transformed])
    df = df[MODEL_COLUMNS]

    return df