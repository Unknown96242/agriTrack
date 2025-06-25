Documentation du projet AgriTrack

Présentation

AgriTrack est une application web de gestion agricole développée avec Flask, SQLAlchemy et PostgreSQL. Elle permet aux utilisateurs de gérer leurs parcelles, inventaires, ventes, clients, rapports et d’accéder à des prévisions météorologiques en temps réel.

Fonctionnalités principales
Authentification : Inscription, connexion, déconnexion sécurisées.
Gestion des parcelles : Ajout, affichage, suppression de parcelles agricoles, filtrées par utilisateur.
Gestion de l’inventaire : Ajout et suivi du matériel agricole, filtré par utilisateur.
Gestion des ventes : Suivi des ventes et des clients, filtrés par utilisateur.
Rapports : Génération de rapports personnalisés sur les coûts, revenus et rendements.
Prévisions météo : Affichage des prévisions météo en temps réel via l’API OpenWeatherMap.
Tableau de bord : Vue synthétique des données de l’exploitation pour chaque utilisateur.

STRUCTURE DU PROJET

python-projet/
│
├── app.py
├── backend/
│   ├── config/
│   │   └── connexion.py
│   └── model/
│       ├── __init__.py
│       ├── utilisateur_model.py
│       ├── parcelle_model.py
│       ├── inventaire_model.py
│       ├── vente_model.py
│       └── ... (autres modèles)
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── inventaires.py
│   ├── ventes.py
│   ├── rapports.py
│   ├── previsions.py
│   └── ... (autres routes)
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── ajout_parcelle.html
│   ├── inscription.html
│   ├── connexion.html
│   ├── previsions.html
│   └── ... (autres templates)
└── static/
    └── ... (fichiers CSS, JS)

INSTALLATION

1) git clone <url-du-repo>
cd python-projet

2) Créer un environnement virtuel
python -m venv env
env\Scripts\activate

3) Installer toute les dependances necessaires a ce projet dans votre environnement viretuel 

pip install Dependances
Dependances necessaires : -flask
                          -flask_migrate
                          -flask_sqlalchemy
                          -flask_wtf
                          -psycopg2
                          -sqlalchemy
                          -wtforms
                          -Blueprint
                          -python-dotenv
                          -requests


4) Creer un fichier .env a la racine du projet et y mettre les variables d'environnement suivantes :
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=votre_cle_secrete
NB: Remplacer username et password par vos identifiants postgres
    Remplacer database_name par le nom de votre base de donnee
    Remplacez egalemet votre_cle_secrete par une cle que vous genererez

# Instructions pour configurer le projet Flask avec PostgreSQL
5) Creer la base de donnees dans votre serveur PostgreSQL avec le nom que vous avez defini dans la variable d'environnement DATABASE_URL

6) Initialiser la base de donnees avec les commandes suivantes :
flask db init
flask db migrate -m "Initialisation"
flask db upgrade

7)Lancer l’application
python app.py


SECURITE
-Les mots de passe sont hashés avec werkzeug.security.
-Les données sont filtrées par utilisateur (utilisateur_id).
-Les routes sensibles nécessitent une session active.

API METEO
-Utilise OpenWeatherMap (clé API à renseigner dans previsions.py).
-Les prévisions sont affichées en temps réel, non stockées en base.

Déconnexion
-Accessible via le menu utilisateur (avatar en haut à droite).
-Vide la session et redirige vers la page de connexion.

AUTEURS
Projet réalisé par : -TCHIKAYA BERY Ray Emilien
                     -STACKYS OBIANG
                     - KABA Keita