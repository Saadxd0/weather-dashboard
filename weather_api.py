import os
from dotenv import load_dotenv
import requests

load_dotenv()  

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
