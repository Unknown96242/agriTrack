from flask import Flask
from backend.config.connexion import db, init_db

app = Flask(__name__)

class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id')) 


    def __repr__(self):
        return f"<Client {self.nom}>"