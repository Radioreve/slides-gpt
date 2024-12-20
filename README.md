# Slides GPT

## Description

Slides GPT est un projet conçu pour faciliter l'interaction avec l'API OpenAI.

## Prérequis

- Python 3.13
- pipenv (pour gérer les dépendances)
- Un compte OpenAI avec une clé d'API valide

## Activez l'environnement virtuel

```shell
pipenv shell
```

## Installer les dépendances 

```shell
pipenv install
```

## Configurer la clé API OpenAI 

Dans le répertoire racine du projet, créez un .env et ajoutez-y les lignes suivantes pour configurer d'OpenAI
```dotenv
OPENAI_API_KEY="your-openai-api-key"
MAX_TOKEN=100
```

## Lancer le serveur

```shell
uvicorn app.main:app --reload
```

## Accéder à Swagger

```shell
http://127.0.0.1:8000/docs
```

## Exécuter les tests

### Exécuter un seul fichier de test 

```shell
python -m unittest tests.test_generate_text
```

### Exécuter tous les tests dans un dossier

```shell
python -m unittest discover -s tests
```

