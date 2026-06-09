# HR Attrition Project - TechNova Partners

## Installation sous Windows PowerShell

```powershell
cd C:\Users\ajarl\Documents\hr_attrition_project

# Créer le projet si ce n'est pas encore fait
uv init

# Créer/recréer l'environnement avec Python 3.11
uv venv --python 3.11

# Activer l'environnement sous PowerShell
.venv\Scripts\Activate.ps1

# Vérifier le Python utilisé
Get-Command python
python --version

# Installer les dépendances à partir du pyproject.toml
uv sync

# Ajouter le kernel Jupyter
python -m ipykernel install --user --name hr-attrition-env --display-name "HR Attrition Project"

# Lancer Jupyter
python -m jupyter lab
```

Si PowerShell bloque l'activation :
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.venv\Scripts\Activate.ps1
```

## Structure conseillée

```text
hr_attrition_project/
├── data/
│   ├── extrait_sirh.csv
│   ├── extrait_eval.csv
│   └── extrait_sondage.csv
├── notebooks/
│   └── 01_eda_feature_engineering.ipynb
├── pyproject.toml
└── README.md
```
