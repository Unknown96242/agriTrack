from flask import Flask
from backend.config.connexion import db, init_db

app = Flask(__name__)

class Prevision(db.Model):
    __tablename__ = 'previsions'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(100))
    valeur = db.Column(db.Text)

    def __repr__(self):
        return f"<Prevision {self.type} le {self.date}>"