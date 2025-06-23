from flask import Blueprint, render_template, request, redirect, url_for
from backend.config.connexion import db
from backend.model import Inventaire
from backend.model.forms import AjoutMaterielForm
from flask import session

inventaires_bp = Blueprint('inventaires', __name__)

@inventaires_bp.route('/inventaires.html')

def inventaires():
    current_user = session.get('current_user')
    if not current_user:
        return redirect(url_for('auth.connexion'))
    # Récupère les types distincts de matériel
    # pour le filtre dans la page d'inventaire
    types = db.session.query(Inventaire.type).distinct().all()
    types = [t[0] for t in types if t[0]]
    filtre = request.args.get('type', 'tout')
    if filtre == 'tout':
        inventaires = Inventaire.query.filter_by(utilisateur_id=current_user).all()
    else:
        inventaires = Inventaire.query.filter_by(type=filtre,utilisateur_id=current_user).all()
    return render_template("inventaires.html", inventaires=inventaires, filtre=filtre, types=types)


@inventaires_bp.route('/ajout_materiel.html', methods=['GET', 'POST'])
def ajout_materiel():
    current_user = session.get('current_user')
    if not current_user:
        return redirect(url_for('auth.connexion'))
    form = AjoutMaterielForm()
    champs = [
        'nom',
        'type',
        'quantite',
        'unite',
        'date_achat',
        'prix_unitaire',
    ]

    if form.validate_on_submit():
        nouveau_materiel = Inventaire(
            nom=form.nom.data,
            type=form.type.data,
            quantite=form.quantite.data,
            unite=form.unite.data,
            date_achat=form.date_achat.data,
            prix_unitaire=float(form.prix_unitaire.data),
            valeur_totale=float(form.quantite.data) * float(form.prix_unitaire.data) if form.prix_unitaire.data else None,
            utilisateur_id=current_user
            
        )
        db.session.add(nouveau_materiel)
        db.session.commit()
        return redirect('/inventaires.html')
    return render_template("ajout_materiel.html", form=form, champs=champs)