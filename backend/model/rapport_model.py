from flask import Flask
from backend.config.connexion import db, init_db

app = Flask(__name__)

class Rapport(db.Model):
    __tablename__ = 'rapports'
    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200))
    contenu = db.Column(db.Text)
    date_generation = db.Column(db.Date)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateurs.id')) 


    def __repr__(self):
        return f"<Rapport {self.titre} - {self.date_generation}>"