from flask import Flask, render_template
from backend.config.connexion import db, init_db
from routes import auth_bp, index_bp, inventaires_bp, rapports_bp, previsions_bp, ventes_bp, dashboard_bp
from sqlalchemy import text
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
init_db(app)
with app.app_context():
    db.create_all()
    try:
        db.session.execute(text('SELECT 1'))
        print("Connexion à la base de données réussie !")
    except Exception as e:
        print("Erreur de connexion à la base de données :", e)
        
app.register_blueprint(auth_bp)
app.register_blueprint(index_bp)
app.register_blueprint(inventaires_bp)
app.register_blueprint(previsions_bp)
app.register_blueprint(rapports_bp)
app.register_blueprint(ventes_bp)
app.register_blueprint(dashboard_bp)

migrate = Migrate(app, db)

@app.route('/test_db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return "Connexion à la base de données réussie !"
    except Exception as e:
        return f"Erreur de connexion à la base de données : {e}"

if __name__ == '__main__':
    app.run(debug=True)



