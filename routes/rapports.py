from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from backend.config.connexion import db
from backend.model import Vente, Parcelle, Inventaire, Rapport
from sqlalchemy import extract, func
from backend.model.forms import AjoutRapportForm

rapports_bp = Blueprint('rapports', __name__)

@rapports_bp.route('/rapports.html')
def rapports():
    current_user = session.get('current_user')
    if not current_user:
        flash("Vous devez être connecté pour accéder aux rapports.", "danger")
        return redirect(url_for('auth.connexion'))

    annee = request.args.get('annee', None, type=int)
    mois = request.args.get('mois', None, type=int)

    # Filtrer par utilisateur_id
    couts_par_culture = (
        db.session.query(Parcelle.culture, func.sum(Inventaire.valeur_totale))
        .join(Parcelle, Parcelle.id == Inventaire.parcelle_id)  # adapte la jointure selon ta structure
        .filter(Inventaire.utilisateur_id == current_user)
        .filter(extract('month', Inventaire.date_achat) == mois if mois else True)
        .filter(extract('year', Inventaire.date_achat) == annee if annee else True)
        .group_by(Parcelle.culture)
        .all()
    )

    revenus_par_produit = (
        db.session.query(Vente.produit, func.sum(Vente.revenu_total))
        .filter(Vente.utilisateur_id == current_user)
        .filter(extract('month', Vente.date_vente) == mois if mois else True)
        .filter(extract('year', Vente.date_vente) == annee if annee else True)
        .group_by(Vente.produit)
        .all()
    )

    couts_labels = [c[0] for c in couts_par_culture]
    couts_values = [float(c[1]) for c in couts_par_culture]
    revenus_labels = [r[0] for r in revenus_par_produit]
    revenus_values = [float(r[1]) for r in revenus_par_produit]

    rapport_id = request.args.get('rapport_id')

    # Récupération des rapports pour la navigation (filtrés par utilisateur)
    all_rapports = Rapport.query.filter_by(utilisateur_id=current_user).order_by(Rapport.date_generation.desc()).all()
    nav_rapports = all_rapports[:5]
    autres_rapports = all_rapports[5:] if len(all_rapports) > 5 else []

    selected_rapport = None
    if rapport_id:
        selected_rapport = Rapport.query.filter_by(id=int(rapport_id), utilisateur_id=current_user).first()
        if selected_rapport:
            annee = selected_rapport.date_generation.year
            mois = selected_rapport.date_generation.month

    ventes_query = Vente.query.filter_by(utilisateur_id=current_user)
    if annee:
        ventes_query = ventes_query.filter(extract('year', Vente.date_vente) == annee)
    if mois:
        ventes_query = ventes_query.filter(extract('month', Vente.date_vente) == mois)
    ventes = ventes_query.all()

    rendement_total = sum(v.quantite_vendue for v in ventes)
    revenu_total = sum(v.revenu_total for v in ventes)

    couts_query = Inventaire.query.filter_by(utilisateur_id=current_user)
    if annee:
        couts_query = couts_query.filter(extract('year', Inventaire.date_achat) == annee)
    if mois:
        couts_query = couts_query.filter(extract('month', Inventaire.date_achat) == mois)
    cout_total = sum(i.valeur_totale for i in couts_query.all())

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
    current_user = session.get('current_user')
    if not current_user:
        flash("Vous devez être connecté pour ajouter un rapport.", "danger")
        return redirect(url_for('auth.connexion'))

    form = AjoutRapportForm()

    if form.validate_on_submit():
        nouveau_rapport = Rapport(
            titre=form.titre.data,
            contenu=form.contenu.data,
            date_generation=form.date_generation.data,
            utilisateur_id=current_user  # Associer le rapport à l'utilisateur connecté
        )
        db.session.add(nouveau_rapport)
        db.session.commit()
        flash("Rapport ajouté avec succès.", "success")
        return redirect(url_for('rapports.rapports'))

    return render_template(
        "ajout_rapport.html",
        form=form
    )