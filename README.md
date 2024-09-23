# FastAPI Todo App

Ce projet est une application Todo construite avec FastAPI et PostgreSQL pour la gestion des tâches. L'application permet de créer, lire, mettre à jour et supprimer des tâches (CRUD) en utilisant une base de données PostgreSQL.

## Fonctionnalités

- **CRUD sur les tâches** :
  - Créer une tâche
  - Lire toutes les tâches ou une tâche spécifique
  - Mettre à jour une tâche existante
  - Supprimer une tâche

## Prérequis

- Python 3.10 au moins
- PostgreSQL
- [Pipenv](https://pipenv.pypa.io/en/latest/) ou `venv` pour gérer l'environnement virtuel
- FastAPI et SQLAlchemy
- dotenv

## Installation

***1. Cloner le dépôt***

   bash
git clone (lien du git)
cd todoapp

***2. creer un environnement virtuel***
sur MAC 
python3 -m venv tdenv
source tdenv/bin/activate

***3. installer les dependences***
pip install -r requirements.txt

***4. configurer variables d'environnement***
DB_HOST=localhost
DB_NAME=AJOUTER VOTRE BASE DE DONNEES
DB_USER=postgres
DB_PASSWORD=AJOUTEZ VOTRE MOT DE PASS
Assurez-vous que vous avez cree votre base de donnees sur postgresql et lancer sur pg4Admin
***5. demarrer le serveur***
uvicorn main:app --reload
L'application sera disponible à l'adresse suivante : http://127.0.0.1:8000.

***Endpoints***

POST /tasks/ : Créer une nouvelle tâche
GET /tasks/ : Récupérer toutes les tâches
GET /tasks/{task_id} : Récupérer une tâche spécifique
PUT /tasks/{task_id} : Mettre à jour une tâche
DELETE /tasks/{task_id} : Supprimer une tâche

***Technologies utilisées***

FastAPI : Framework Python pour créer des APIs rapides et modernes
SQLAlchemy : ORM pour la gestion des bases de données
PostgreSQL : Base de données relationnelle
Pydantic : Validation des données et des schémas

***Contribuer***

Forker le projet
Créer une nouvelle branche (git checkout -b ma-branche)
Commiter vos modifications (git commit -m 'Ajouter une nouvelle fonctionnalité')
Pousser votre branche (git push origin ma-branche)
Ouvrir une Pull Request

