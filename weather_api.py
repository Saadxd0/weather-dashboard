import requests

API_KEY = "f36fe5d07df38ba95c8c64e35e4c94ea"  # Replace this

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
