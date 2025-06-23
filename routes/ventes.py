from flask import Blueprint, render_template, session, redirect, url_for, flash
from backend.model import Vente, Client

ventes_bp = Blueprint('ventes', __name__)

@ventes_bp.route('/ventes.html')
def ventes():
    current_user = session.get('current_user')
    if not current_user:
        flash("Vous devez être connecté pour accéder aux ventes.", "danger")
        return redirect(url_for('auth.connexion'))

    ventes = Vente.query.filter_by(utilisateur_id=current_user).all()
    vente_totale = sum(vente.revenu_total for vente in ventes)
    nombre_clients = Client.query.filter_by(utilisateur_id=current_user).count() if hasattr(Client, 'utilisateur_id') else Client.query.count()
    quantite_total = sum(vente.quantite_vendue for vente in ventes)

    return render_template(
        "ventes.html",
        ventes=ventes,
        vente_totale=vente_totale,
        nombre_clients=nombre_clients,
        quantite_total=quantite_total
    )
