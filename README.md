# Manuel d'Utilisation — Détection d'Intrusions Réseau par IA

Ce programme est conçu pour détecter les intrusions réseau à l'aide de techniques d'intelligence artificielle (apprentissage supervisé et non supervisé). Il s'appuie sur le jeu de données **CICIDS2017** et expose une API de prédiction via **FastAPI**.

---

## Contenu du projet

- `notebooks/experimentation.ipynb` — Notebook Jupyter pour l'exploration des données, l'entraînement et l'évaluation des modèles
- `api/main.py` — API REST (FastAPI) pour servir les prédictions du modèle
- `models/` — Dossier de sauvegarde des modèles entraînés (`.pkl`)
- `data/` — Dossier contenant le jeu de données (fichiers CSV)
- `requirements.txt` — Liste des dépendances Python du projet
- `README.md` — Manuel d'utilisation du projet

---

## Jeu de données

Le projet utilise le dataset **CICIDS2017 Cleaned and Preprocessed**.

### Option 1 — Télécharger le dataset

Téléchargez-le depuis Kaggle :
👉 [https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed](https://www.kaggle.com/datasets/ericanacletoribeiro/cicids2017-cleaned-and-preprocessed)

Placez le fichier CSV téléchargé dans le dossier `data/` :

```
data/
  cicids2017_cleaned.csv
```

### Option 2 — Utiliser votre propre jeu de données

Vous pouvez utiliser votre propre fichier CSV à condition qu'il respecte les conditions suivantes :

- Le fichier doit contenir une colonne de label : `Label` ou `Attack Type`
- Les valeurs `benign`, `normal traffic` ou `normal` seront considérées comme du trafic normal (classe `0`)
- Toutes les autres valeurs seront considérées comme des attaques (classe `1`)
- Les autres colonnes doivent être des features numériques

Placez votre fichier dans le dossier `data/` et ajustez le chemin dans le notebook si nécessaire.

---

## Installation

### 1. Prérequis

- **Python 3.8+**
- **pip** — gestionnaire de paquets Python

### 2. Créer un environnement virtuel (recommandé)

```bash
python -m venv .venv
```

Activer l'environnement :

- **Windows (PowerShell)** :
  ```bash
  .venv\Scripts\Activate.ps1
  ```
- **Windows (CMD)** :
  ```bash
  .venv\Scripts\activate.bat
  ```
- **Linux / macOS** :
  ```bash
  source .venv/bin/activate
  ```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Utilisation

### Étape 1 — Expérimentation et entraînement du modèle

Ouvrez et exécutez le notebook Jupyter :

```bash
jupyter notebook notebooks/experimentation.ipynb
```

Le notebook effectue les étapes suivantes :

1. **Chargement des données** depuis `data/cicids2017_cleaned.csv`
2. **Nettoyage et encodage** — création d'une cible binaire (normal = `0`, attaque = `1`)
3. **Entraînement d'un modèle supervisé** — Random Forest Classifier
4. **Évaluation** — rapport de classification, matrice de confusion, courbe ROC
5. **Entraînement d'un modèle non supervisé** — Isolation Forest
6. **Sauvegarde du modèle** — le modèle Random Forest est exporté dans `models/rf_model.pkl`

### Étape 2 — Lancer l'API de prédiction

Une fois le modèle entraîné et sauvegardé, lancez le serveur API :

```bash
cd api
uvicorn main:app --reload
```

L'API sera accessible à l'adresse : [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentation interactive (Swagger UI) : [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
