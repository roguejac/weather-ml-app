from flask import Flask, render_template, request
from api_fetcher import get_weather
from ml_model import predict, save_weather_data
import os

app = Flask(__name__)

CITIES = ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Bloemfontein", "Polokwane"]

@app.route("/", methods=["GET", "HEAD"])
def index():
    city = request.args.get("city", "Johannesburg")
    weather = get_weather(city)
    prediction = predict(weather["temp"], weather["humidity"])
    save_weather_data(weather)

    return render_template("index.html", weather=weather, prediction=prediction, cities=CITIES)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render sets PORT automatically
    app.run(host="0.0.0.0", port=port)
