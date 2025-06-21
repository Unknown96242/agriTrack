from flask import Blueprint, render_template, request
from backend.model import Prevision

previsions_bp = Blueprint('previsions', __name__)

@previsions_bp.route('/previsions.html')
def previsions():
    previsions = Prevision.query.all()
    return render_template("previsions.html", previsions=previsions)