from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length

class AjoutRapportForm(FlaskForm):
    titre = StringField(
        "Titre",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Titre du rapport"}
    )
    contenu = TextAreaField(
        "Contenu",
        validators=[DataRequired(), Length(max=500)],
        render_kw={"placeholder": "Contenu du rapport"}
    )
    date_generation = DateField(
        "Date de génération",
        validators=[DataRequired()],
        format='%Y-%m-%d',
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    submit = SubmitField("Ajouter")
    
class AjoutMaterielForm(FlaskForm):
    nom = StringField(
        "Nom du materiel",
        validators=[DataRequired(), Length(max=100)],
        render_kw={"placeholder": "Nom du matériel"}
    )
    type = StringField(
        "Type de materiel",
        validators=[DataRequired(), Length(max=50)],
        render_kw={"placeholder": "Type de matériel"}
    )
    quantite = FloatField(
        "Quantité",
        validators=[DataRequired(), Length(max=10)],
        render_kw={"placeholder": "Quantité"}
    )
    unite = StringField(
        "Unité",
        validators=[DataRequired(), Length(max=20)],
        render_kw={"placeholder": "Unité (ex: kg, litres)"}
    )
    date_achat = DateField(
        "Date d'achat",
        validators=[DataRequired()],
        format='%Y-%m-%d',
        render_kw={"placeholder": "YYYY-MM-DD"}
    )
    prix_unitaire = FloatField(
        "Prix unitaire",
        validators=[DataRequired(), Length(max=10)],
        render_kw={"placeholder": "Prix unitaire"}
    )
    submit = SubmitField("Ajouter")