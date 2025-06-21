from flask import Blueprint, render_template
from backend.model import Vente, Client

ventes_bp = Blueprint('ventes', __name__)

@ventes_bp.route('/ventes.html')
def ventes():
    ventes = Vente.query.all()
    vente_totale = sum(vente.revenu_total for vente in ventes)
    nombre_clients = Client.query.count()
    quantite_total = sum(vente.quantite_vendue for vente in ventes)

    # for vente in ventes:
    return render_template("ventes.html", ventes=ventes, vente_totale=vente_totale, nombre_clients=nombre_clients, quantite_total=quantite_total)
