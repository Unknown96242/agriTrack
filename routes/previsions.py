import requests
from flask import render_template, Blueprint

previsions_bp = Blueprint('previsions', __name__)

@previsions_bp.route('/previsions.html')
def previsions():
    api_key = "234b98945460ba88c68738ebbe90ef2e"
    lat = "14.693425"
    long = "-17.447938"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Conversion Kelvin → Celsius
    temp_c = round(data["main"]["temp"] - 273.15, 1)
    feels_like_c = round(data["main"]["feels_like"] - 273.15, 1)

    previsions = [
        {"type": "Ville", "valeur": f"{data['name']} ({data['sys']['country']})"},
        {"type": "Météo", "valeur": data["weather"][0]["description"]},
        {"type": "Température", "valeur": f"{temp_c} °C"},
        {"type": "Ressentie", "valeur": f"{feels_like_c} °C"},
        {"type": "Humidité", "valeur": f"{data['main']['humidity']} %"},
        {"type": "Vent", "valeur": f"{data['wind']['speed']} m/s"},
        {"type": "Pression", "valeur": f"{data['main']['pressure']} hPa"},
    ]

    return render_template("previsions.html", previsions=previsions)