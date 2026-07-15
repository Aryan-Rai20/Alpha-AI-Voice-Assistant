import requests
from config import WEATHER_API_KEY

API_KEY = "YOUR_API_KEY"


def get_weather(city="Varanasi"):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)

        data = response.json()

        if data["cod"] != 200:
            return "Sorry Sir, I couldn't find that city."

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

        return f"The current temperature in {city} is {temp} degree Celsius with {weather}."

    except Exception:
        return "Unable to get weather information."
