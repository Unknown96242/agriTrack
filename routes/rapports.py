from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from backend.config.connexion import db
from backend.model import Vente, Parcelle, Inventaire, Rapport
from sqlalchemy import extract, func
from backend.model.forms import AjoutRapportForm

rapports_bp = Blueprint('rapports', __name__)
@rapports_bp.route('/rapports.html')
def rapports():
    
    annee = request.args.get('annee', None, type=int)
    mois = request.args.get('mois', None, type=int)
    
    couts_par_culture = (
        db.session.query(Parcelle.culture, func.sum(Inventaire.valeur_totale))
        .join(Parcelle, Parcelle.id == Inventaire.id)  # adapte la jointure selon ta structure
        .filter(extract('month', Inventaire.date_achat) == mois if mois else True)
        .filter(extract('year', Inventaire.date_achat) == annee if annee else True)
        .group_by(Parcelle.culture)
        .all()
    )
    
    revenus_par_produit = (
        db.session.query(Vente.produit, func.sum(Vente.revenu_total))
        .filter(extract('month', Vente.date_vente) == mois if mois else True)
        .filter(extract('year', Vente.date_vente) == annee if annee else True)
        .group_by(Vente.produit)
        .all()
    )
    # paration des donees données pour Chart.js
    couts_labels = [c[0] for c in couts_par_culture]
    couts_values = [float(c[1]) for c in couts_par_culture]
    revenus_labels = [r[0] for r in revenus_par_produit]
    revenus_values = [float(r[1]) for r in revenus_par_produit]
    
    # Récupération de l'ID du rapport depuis l'URL
    rapport_id = request.args.get('rapport_id')

    # Récupération des rapports pour la navigation
    all_rapports = Rapport.query.order_by(Rapport.date_generation.desc()).all()
    nav_rapports = all_rapports[:5]
    autres_rapports = all_rapports[5:] if len(all_rapports) > 5 else []

    # Si un rapport est sélectionné, on récupère ses données
    selected_rapport = None
    if rapport_id:
        selected_rapport = Rapport.query.get(int(rapport_id))
        if selected_rapport:
            annee = selected_rapport.date_generation.year
            mois = selected_rapport.date_generation.month

    # Calculs selon annee et mois (issus du rapport sélectionné ou de l'URL)
    ventes_query = Vente.query
    if annee:
        ventes_query = ventes_query.filter(extract('year', Vente.date_vente) == annee)
    if mois:
        ventes_query = ventes_query.filter(extract('month', Vente.date_vente) == mois)
    ventes = ventes_query.all()

    # Calculs des totaux
    rendement_total = sum(v.quantite_vendue for v in ventes)
    revenu_total = sum(v.revenu_total for v in ventes)

    # Calcul des coûts totaux
    couts_query = Inventaire.query
    if annee:
        couts_query = couts_query.filter(extract('year', Inventaire.date_achat) == annee)
    if mois:
        couts_query = couts_query.filter(extract('month', Inventaire.date_achat) == mois)
    cout_total = sum(i.valeur_totale for i in couts_query.all())

    # Si aucun rapport n'est sélectionné, on prend le dernier rapport
    return render_template(
        "rapports.html",
        nav_rapports=nav_rapports,
        autres_rapports=autres_rapports,
        annee=annee,
        mois=mois,
        rendement_total=rendement_total,
        revenu_total=revenu_total,
        cout_total=cout_total,
        selected_rapport=selected_rapport,
        couts_labels=couts_labels,
        couts_values=couts_values,
        revenus_labels=revenus_labels,
        revenus_values=revenus_values
    )

@rapports_bp.route('/ajout_rapport.html', methods=['GET', 'POST'])
def ajout_rapport():
    form = AjoutRapportForm()

    if form.validate_on_submit():
        # Création et ajout du rapport
        nouveau_rapport = Rapport(
            titre=form.titre.data,
            contenu=form.contenu.data,
            date_generation=form.date_generation.data
        )
        db.session.add(nouveau_rapport)
        db.session.commit()
        flash("Rapport ajouté avec succès.", "success")
        return redirect(url_for('rapports.rapports'))

    return render_template(
        "ajout_rapport.html",
        form=form
    )