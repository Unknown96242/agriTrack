from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from backend.model import Utilisateur
from backend.config.connexion import db
from werkzeug.security import generate_password_hash


auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Recherche de l'utilisateur dans la base
        user = Utilisateur.query.filter_by(email=email).first()
        if user and user.check_password(password):  # check_password doit être défini dans ton modèle
            session['current_user'] = user.id
            flash("Connexion réussie.", "success")
            return redirect(url_for('index.index'))
        else:
            flash("Email ou mot de passe incorrect.", "danger")
            return render_template("connexion.html", email=email)
    return render_template("connexion.html")


@auth_bp.route('/inscription.html', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form.get('nom') + " " + request.form.get('prenom')
        # Vérifie si le nom est vide
        if not nom.strip():
            flash("Le nom ne peut pas être vide.", "danger")
            return render_template("inscription.html")
        
        email = request.form.get('email')
        password = request.form.get('password')

        # Vérifie si l'utilisateur existe déjà
        if Utilisateur.query.filter_by(email=email).first():
            flash("Cet email est déjà utilisé.", "danger")
            return render_template("inscription.html", email=email)

        # Crée un nouvel utilisateur
        user = Utilisateur(nom=nom, email=email)
        user.set_password(password)  # Méthode qui hash le mot de passe
        db.session.add(user)
        db.session.commit()
        flash("Inscription réussie. Vous pouvez vous connecter.", "success")
        return redirect(url_for('auth.connexion'))

    return render_template("inscription.html")

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash("Déconnexion réussie.", "success")
    return redirect(url_for('auth.connexion'))