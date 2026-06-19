# HR Attrition API - Projet 3

## 1. Présentation du projet

Cette application permet :

- de recevoir des données brutes concernant un salarié ;
- de valider automatiquement les données avec Pydantic ;
- de transformer les données brutes en variables exploitables par le modèle ;
- de générer une prédiction avec un modèle Random Forest entraîné ;
- d’enregistrer les données et les résultats dans une base PostgreSQL ;
- de consulter l’historique des prédictions ;
- de tester automatiquement le projet avec Pytest ;
- d’automatiser les tests avec GitHub Actions.

---

## 2. Objectifs du projet

Les objectifs principaux sont :

- créer une API avec FastAPI ;
- exposer un modèle de machine learning via un endpoint `/predict` ;
- utiliser Pydantic pour valider les entrées ;
- utiliser PostgreSQL pour stocker les prédictions ;
- écrire des tests unitaires et fonctionnels avec Pytest ;
- générer un rapport de couverture avec pytest-cov ;
- mettre en place une intégration continue avec GitHub Actions ;
- structurer correctement le dépôt GitHub ;
- documenter l’installation, l’utilisation et le fonctionnement du projet.

---

## 3. Structure du projet

```text
projet3/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── model.py
│   ├── preprocessing.py
│   ├── database.py
│   ├── db_models.py
│   └── crud.py
├── data/
├── db/
│   ├── create_db.sql
│   └── schema_bdd.md
├── models/
│   └── model.pkl
├── notebooks/
│   └── 01_feature_engineering_modelisation_finetuning_SHAP.ipynb
├── presentation/
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_model.py
│   └── test_preprocessing.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock