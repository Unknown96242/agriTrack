from flask import Blueprint, render_template, request
from backend.model import Vente, Client, Parcelle

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route('/dashboard.html')
def dashboard():
    ventes = Vente.query.all()
    clients = Client.query.all()
    parcelles = Parcelle.query.all()
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
