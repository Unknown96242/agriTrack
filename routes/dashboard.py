from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.model import Vente, Client, Parcelle
from backend.config.connexion import db
from flask import session

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route('/dashboard.html')
def dashboard():
    current_user = session.get('current_user')
    ventes = Vente.query.filter_by(utilisateur_id=current_user).all()
    clients = Client.query.filter_by(utilisateur_id=current_user).all()
    parcelles = Parcelle.query.filter_by(utilisateur_id=current_user).all()    
    nb_parcelles = len(parcelles)
    sup_totale = sum(parcelle.superficie for parcelle in parcelles)
    tache_en_cours = sum(parcelle.statut == "En cours" for parcelle in parcelles)
    return render_template("dashboard.html", 
                           ventes=ventes, 
                           clients=clients, 
                           parcelles=parcelles, 
                           nb_parcelles=nb_parcelles, 
                           sup_totale=sup_totale,
                           tache_en_cours=tache_en_cours,)

@dashboard_bp.route('/ajout_parcelle.html', methods=['GET', 'POST'])
def ajout_parcelle():
    current_user = session.get('current_user')
    if not current_user:
        flash("Vous devez être connecté pour ajouter une parcelle.", "danger")
        return redirect(url_for('auth.connexion'))
    if request.method == 'POST':
        nom = request.form.get('nom')
        superficie = request.form.get('superficie')
        culture = request.form.get('culture')
        statut = "En cours"
        localisation = request.form.get('localisation')

        parcelle = Parcelle(
            nom=nom,
            superficie=superficie,
            culture=culture,
            statut=statut,
            localisation=localisation,
            utilisateur_id=current_user
        )
        db.session.add(parcelle)
        db.session.commit()
        flash("Parcelle ajoutée avec succès.", "success")
        return redirect(url_for('dashboard.dashboard'))

    return render_template("ajout_parcelle.html")
