from flask import Blueprint, render_template, request
from backend.model import Parcelle, Intervention
from calendar import monthrange
from datetime import date
import calendar
from flask import session
from flask import redirect, url_for

index_bp = Blueprint("index", __name__)
@index_bp.route('/index.html')
def index():
    current_user = session.get('current_user')
    if session.get('current_user') is None:
        return redirect(url_for('auth.connexion'))
    
    interventions = Intervention.query.filter_by(utilisateur_id=current_user).all()
    parcelles = Parcelle.query.filter_by(utilisateur_id=current_user).all()
    parcelle_id = request.args.get('parcelle_id', type=int)
    parcelle_sel = Parcelle.query.get(parcelle_id) if parcelle_id else parcelles[0] if parcelles else None
    semis = parcelle_sel.date_semis
    floraison = parcelle_sel.date_floraison

    # Récupère le mois/année depuis l'URL ou prend le mois courant
    year = request.args.get('year', date.today().year, type=int)
    month = request.args.get('month', date.today().month, type=int)
    nb_jours = monthrange(year, month)[1]
    month_name = calendar.month_name[month]
    first_weekday = date(year, month, 1).weekday()
    first_weekday = (first_weekday + 1) % 7

    return render_template(
        "index.html",
        parcelles=parcelles,
        parcelle_sel=parcelle_sel,
        semis=semis,
        floraison=floraison,
        interventions=interventions,
        year=year,
        month=month,
        nb_jours=nb_jours,
        month_name=month_name,
        first_weekday=first_weekday,
        date=date,
    )
    
    
@index_bp.route('/calendar')
def calendar_partial():
    # Récupère les paramètres GET
    parcelle_id = request.args.get('parcelle_id', type=int)
    year = request.args.get('year', date.today().year, type=int)
    month = request.args.get('month', date.today().month, type=int)
    parcelle_sel = Parcelle.query.get(parcelle_id)
    semis = parcelle_sel.date_semis
    floraison = parcelle_sel.date_floraison
    nb_jours = monthrange(year, month)[1]
    month_name = calendar.month_name[month]
    first_weekday = date(year, month, 1).weekday()
    first_weekday = (first_weekday + 1) % 7

    return render_template(
        "calendar_partial.html",
        parcelle_sel=parcelle_sel,
        semis=semis,
        floraison=floraison,
        year=year,
        month=month,
        nb_jours=nb_jours,
        month_name=month_name,
        first_weekday=first_weekday,
        date=date,
    )