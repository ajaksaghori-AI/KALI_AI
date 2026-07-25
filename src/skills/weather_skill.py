import requests
from src.config.api_keys import OPENWEATHER_API_KEY


def get_weather(city):
    """
    Returns the current weather for the given city.
    """

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = round(data["main"]["temp"], 1)
            description = data["weather"][0]["description"]

            return (
                f"The current temperature in {city} is "
                f"{temperature} degrees Celsius with {description}."
            )

        else:
            return "Sorry, I couldn't find that city."

    except Exception:
        return "Sorry, I couldn't connect to the weather service."