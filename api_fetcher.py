import requests

API_KEY = "c1e3b246b33fdfa45ed8ad78e671d520"  # Replace with your OpenWeatherMap API key

def get_weather(city="Johannesburg"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"]
    }