# Waterleak Simulation

Détection de fuites en temps réel sur un réseau de canalisations via Isolation Forest.

## Dataset
Source : Aghashahi et al. (2022) - Dataset of Leak Simulations in Experimental Testbed Water Distribution System  
DOI : https://doi.org/10.17632/tbrnp6vrnj.1  
Licence : CC BY 4.0

## Installation

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python main.py
```

Lance le scénario `ideal` par défaut. Télécharge automatiquement les données depuis HuggingFace, démarre l'API sur `http://localhost:8000` et lance la simulation.

### Choisir un scénario

```bash
python main.py --scenario ideal       # signal propre, fuite franche
python main.py --scenario difficile   # fort débit, fuite subtile
python main.py --scenario bruite      # signal transitoire, cas limite
```

## Endpoints API

| Endpoint | Description |
|----------|-------------|
| `GET /results` | Tous les résultats |
| `GET /results/latest` | Dernier résultat |
| `GET /status` | État de la simulation |

## Structure

```
models/          ← modèle Isolation Forest + scaler
features.py      ← extraction de features
simulation.py    ← simulation temps réel
api.py           ← FastAPI
ingest.py        ← téléchargement des données
main.py          ← point d'entrée
```
