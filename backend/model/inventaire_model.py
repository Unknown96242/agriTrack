from flask import Flask
from backend.config.connexion import db, init_db

app = Flask(__name__)

class Inventaire(db.Model):
    __tablename__ = 'inventaire'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Machinerie, Equipement, Semence, Engrais
    quantite = db.Column(db.Numeric(10, 2), nullable=False)
    unite = db.Column(db.String(20))
    date_achat = db.Column(db.Date)
    prix_unitaire = db.Column(db.Numeric(10, 2))
    valeur_totale = db.Column(db.Numeric(10, 2))

    def __repr__(self):
        return f"<Inventaire {self.nom} ({self.type}) - {self.quantite} {self.unite}>"