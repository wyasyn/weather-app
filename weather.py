from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def get_current_weather(city="Kampala"):
    """Returns the current weather for a city"""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions *** \n')
    
    city = input("\nPlease enter a city name: ")
    
    # Check for empty strings or strings with only spaces
    if not bool(city.strip()):
        city = 'Kampala'
    
    weather_data = get_current_weather(city)
    
    print('\n')
    
    pprint(weather_data)