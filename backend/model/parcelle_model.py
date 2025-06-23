from flask import Flask
from backend.config.connexion import db, init_db
from sqlalchemy import Boolean

app = Flask(__name__)

class Parcelle(db.Model):
    __tablename__ = 'parcelles'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    superficie = db.Column(db.Numeric(10, 2), nullable=False)
    culture = db.Column(db.String(100))
    date_semis = db.Column(db.Date)
    statut = db.Column(db.String(50))
    fertilisation = db.Column(Boolean, default=False)
    irrigation = db.Column(Boolean, default=False)
    controle_ravageurs = db.Column(Boolean, default=False)
    date_germination = db.Column(db.Date)
    date_croissance_vegetative = db.Column(db.Date)
    date_floraison = db.Column(db.Date)
    localisation = db.Column(db.String(255))  # Ajout de la localisation
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id')) 

    def __repr__(self):
        return f"<Parcelle {self.nom} - {self.culture} ({self.superficie} ha)>"