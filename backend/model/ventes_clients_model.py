from flask import Flask
from backend.config.connexion import db

app = Flask(__name__)

class VenteClient(db.Model):
    __tablename__ = 'ventes_clients'
    vente_id = db.Column(db.Integer, db.ForeignKey('ventes.id'), primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'), primary_key=True)
    vente = db.relationship('Vente', backref='ventes_clients')
    client = db.relationship('Client', backref='ventes_clients')

    def __repr__(self):
        return f"<VenteClient vente={self.vente_id} client={self.client_id}>"