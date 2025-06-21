from flask import Flask
from backend.config.connexion import db

app = Flask(__name__)

class Intervention(db.Model):
    __tablename__ = 'interventions'
    id = db.Column(db.Integer, primary_key=True)
    parcelle_id = db.Column(db.Integer, db.ForeignKey('parcelles.id'))
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    statut = db.Column(db.String(50))
    parcelle = db.relationship('Parcelle', backref='interventions')

    def __repr__(self):
        return f"<Intervention {self.type} sur parcelle {self.parcelle_id} le {self.date}>"