from flask import Flask
from backend.config.connexion import db, init_db

app = Flask(__name__)



class Vente(db.Model):
    __tablename__ = 'ventes'
    id = db.Column(db.Integer, primary_key=True)
    produit = db.Column(db.String(100), nullable=False)
    prix_unitaire = db.Column(db.Numeric(10, 2), nullable=False)
    quantite_vendue = db.Column(db.Numeric(10, 2), nullable=False)
    unite = db.Column(db.String(20))
    revenu_total = db.Column(db.Numeric(10, 2))
    date_vente = db.Column(db.Date)

    def __repr__(self):
        return f"<Vente {self.produit} - {self.quantite_vendue}{self.unite} - {self.revenu_total}€>"






