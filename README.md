# Slides GPT

## Description

Slides GPT est un projet conçu pour faciliter l'interaction avec l'API OpenAI.

## Prérequis

- Python 3.13
- pipenv (pour gérer les dépendances)
- Un compte OpenAI avec une clé d'API valide

## Installer les dépendances 

```shell
pipenv install
```

## Configurer la clé API OpenAI 

```dotenv
OPENAI_API_KEY="your-openai-api-key"
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

```shell
pytest
```

