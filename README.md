# HR Attrition API — Projet 3

## Présentation du projet

Le projet répond à une demande de l’entreprise fictive **Futurisys**, qui souhaite disposer d’un Proof of Concept opérationnel permettant :

* d’exposer un modèle de machine learning via une API ;
* de recevoir des données brutes en entrée ;
* de valider les données envoyées par l’utilisateur ;
* de transformer automatiquement les données pour le modèle ;
* de générer une prédiction ;
* d’enregistrer les prédictions en base PostgreSQL ;
* de tester automatiquement le code ;
* de mettre en place une intégration continue avec GitHub Actions ;
* de préparer le déploiement cloud de l’API.


## Structure du projet

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
├── requirements.txt
├── render.yaml
└── uv.lock
```

---

## Technologies utilisées

| Technologie    | Utilisation                           |
| -------------- | ------------------------------------- |
| Python         | Langage principal                     |
| FastAPI        | Création de l’API                     |
| Pydantic       | Validation des données entrantes      |
| Scikit-learn   | Entraînement et utilisation du modèle |
| Random Forest  | Modèle final de prédiction            |
| Joblib         | Sauvegarde et chargement du modèle    |
| Pandas         | Transformation des données            |
| PostgreSQL     | Base de données relationnelle         |
| SQLAlchemy     | ORM pour communiquer avec PostgreSQL  |
| Pytest         | Tests unitaires et fonctionnels       |
| pytest-cov     | Rapport de couverture de tests        |
| Git            | Versionnement du code                 |
| GitHub         | Hébergement du dépôt                  |
| GitHub Actions | Intégration continue                  |
| uv             | Gestion de l’environnement Python     |
| Cloudfanatic   | Déploiement cloud prévu               |

---

## Fonctionnement général

L’API reçoit des données brutes concernant un salarié.

Ces données sont ensuite :

1. validées avec Pydantic ;
2. transformées automatiquement dans `preprocessing.py` ;
3. converties en 47 variables attendues par le modèle ;
4. envoyées au modèle Random Forest ;
5. utilisées pour générer une prédiction ;
6. enregistrées dans PostgreSQL ;
7. retournées à l’utilisateur via l’API.

```text
Données brutes utilisateur
↓
Validation Pydantic
↓
Prétraitement automatique
↓
Création des 47 variables du modèle
↓
Prédiction avec Random Forest
↓
Enregistrement PostgreSQL
↓
Réponse API
```

---

## Modèle de machine learning

Le modèle utilisé est un **Random Forest Classifier** entraîné dans le notebook du projet.

Le modèle final est sauvegardé dans :

```text
models/model.pkl
```

Il est chargé automatiquement par l’API au démarrage.

Le modèle attend 47 variables en entrée. Ces variables sont générées automatiquement à partir des données brutes envoyées à l’API.

Exemples de variables créées automatiquement :

* `satisfaction_moyenne`
* `ecart_note_evaluation`
* `ratio_anciennete_poste`
* `ratio_anciennete_responsable`
* `experience_avant_entreprise`
* `salaire_par_annee_experience`
* `promotion_ancienne`
* `charge_operationnelle_risque`

Exemples de variables catégorielles encodées :

* `genre_M`
* `statut_marital_Marié(e)`
* `departement_Consulting`
* `poste_Consultant`
* `frequence_deplacement_Occasionnel`

---

## Installation du projet

### 1. Cloner le dépôt

```bash
git clone https://github.com/StoneOceans/projet3.git
cd projet3
```

### 2. Installer uv

```bash
pip install uv
```

### 3. Installer les dépendances

```bash
uv sync
```

Si nécessaire, installer manuellement les dépendances :

```bash
uv add fastapi uvicorn pydantic pandas numpy scikit-learn joblib sqlalchemy psycopg2-binary python-dotenv
uv add --dev pytest pytest-cov httpx
```

---

## Configuration de l’environnement

Créer un fichier `.env` à la racine du projet.

Exemple :

```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/hr_attrition
MODEL_VERSION=1.0.0
```

Le fichier `.env` contient des informations sensibles. Il ne doit pas être envoyé sur GitHub.

Un fichier `.env.example` est fourni :

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/hr_attrition
MODEL_VERSION=1.0.0
```

---

## Base de données PostgreSQL

La base de données utilisée s’appelle :

```text
hr_attrition
```

La table principale est :

```text
predictions
```

Elle permet de stocker :

* les données brutes reçues par l’API ;
* la prédiction générée ;
* la probabilité associée ;
* l’interprétation du résultat ;
* la version du modèle ;
* la date et l’heure de la prédiction.

### Création de la base

Avec `psql` :

```sql
CREATE DATABASE hr_attrition;
```

### Script SQL

Un script de création de table est disponible dans :

```text
db/create_db.sql
```

La table peut également être créée automatiquement par SQLAlchemy au démarrage de l’API.

---

## Lancer l’API en local

Depuis la racine du projet :

```bash
uv run uvicorn app.main:app --reload
```

L’API est disponible ici :

```text
http://127.0.0.1:8000
```

La documentation Swagger est disponible ici :

```text
http://127.0.0.1:8000/docs
```

La documentation ReDoc est disponible ici :

```text
http://127.0.0.1:8000/redoc
```

---

## Endpoints disponibles

| Méthode | Endpoint       | Description                                      |
| ------- | -------------- | ------------------------------------------------ |
| GET     | `/`            | Vérifie que l’API fonctionne                     |
| GET     | `/health`      | Vérifie l’état de l’API, du modèle et de la base |
| POST    | `/predict`     | Génère une prédiction d’attrition                |
| GET     | `/predictions` | Retourne l’historique des prédictions            |

---

## Exemple de requête `/predict`

Exemple de données brutes envoyées à l’API :

```json
{
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
```

Exemple de réponse :

```json
{
  "prediction": 0,
  "probability": 0.23,
  "interpretation": "Risque faible de départ"
}
```

---

## Tests

Les tests sont écrits avec Pytest.

Ils couvrent :

* le fonctionnement de l’endpoint `/` ;
* le fonctionnement de l’endpoint `/health` ;
* le fonctionnement de l’endpoint `/predict` ;
* les erreurs de validation Pydantic ;
* le fonctionnement de l’endpoint `/predictions` ;
* la transformation des données brutes ;
* la création des 47 variables attendues par le modèle ;
* le format de sortie du modèle.

### Lancer les tests

```bash
uv run pytest --cov=app
```

### Générer un rapport HTML

```bash
uv run pytest --cov=app --cov-report=html
```

Le rapport est généré dans :

```text
htmlcov/index.html
```


## CI/CD avec GitHub Actions

Le projet contient un pipeline GitHub Actions dans :

```text
.github/workflows/ci.yml
```

Le pipeline est exécuté automatiquement lors des pushs ou pull requests.

Il réalise les étapes suivantes :

```text
Récupération du code
↓
Installation de Python
↓
Installation de uv
↓
Démarrage d’un service PostgreSQL
↓
Installation des dépendances
↓
Vérification des fichiers importants
↓
Lancement des tests Pytest avec couverture
```

Le pipeline GitHub Actions est fonctionnel et les tests passent avec succès.


## Déploiement cloud

Le déploiement cloud est prévu avec Cloudfanatic.

L’objectif du déploiement est de rendre l’API accessible publiquement avec une URL distante.

Le déploiement doit exposer les endpoints suivants :

```text
/
 /health
 /predict
 /predictions
 /docs
```

La commande de lancement en production doit être équivalente à :

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Une fois le déploiement finalisé, l’URL de production sera ajoutée ici :


Gestion Git

Le projet utilise Git avec plusieurs branches fonctionnelles.

Branches principales :

```text
main
feature/api-fastapi
feature/raw-input-postgresql
feature/postgresql
```

---

## Sécurité

* les variables sensibles sont stockées dans `.env` ;
* le fichier `.env` est exclu de GitHub ;
* un fichier `.env.example` est fourni ;
* les données entrantes sont validées avec Pydantic ;
* les erreurs de validation retournent automatiquement une erreur HTTP 422 ;
* PostgreSQL est utilisé via SQLAlchemy ;
* les tests automatisés vérifient les fonctionnalités principales.

---

URL de production : https://ajarl.projet.dev-data.eu/docs
>>>>>>> feature/postgresql

