1) Installer toute les dependances necessaires a ce projet dans votre environnement viretuel 
Dependances necessaires : -flask
                          -flask_migrate
                          -flask_sqlalchemy
                          -flask_wtf
                          -psycopg2
                          -sqlalchemy
                          -wtforms
                          -Blueprint
                          -python-dotenv


2) Creer un fichier .env a la racine du projet et y mettre les variables d'environnement suivantes :
DATABASE_URL=postgresql://username:password@localhost:5432/database_name
SECRET_KEY=votre_cle_secrete
NB: Remplacer username et password par vos identifiants postgres
    Remplacer database_name par le nom de votre base de donnee
    Remplacez egalemet votre_cle_secrete par une cle que vous genererez

# Instructions pour configurer le projet Flask avec PostgreSQL
3) Creer la base de donnees dans votre serveur PostgreSQL avec le nom que vous avez defini dans la variable d'environnement DATABASE_URL
4) Initialiser la base de donnees avec les commandes suivantes :
flask db init
flask db migrate
flask db upgrade