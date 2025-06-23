from flask import Flask
from backend.config.connexion import db
from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)

class Utilisateur(db.Model):
    __tablename__ = 'utilisateurs'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    # role = db.Column(db.String(50), nullable=False) 
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 

    def __repr__(self):
        return f"<Utilisateur {self.nom} - {self.email}>"