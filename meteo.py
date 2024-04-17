import requests
from termcolor import colored
import time

api_key = input("Inserisci la tua API key generata tramite openweathermap.org : ")

while True:
    
    city = input(colored("Inserisci il nome della città o scrivi 'exit' per uscire:\n", 'green'))
    
    if city.lower() == 'exit':
        break
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data["weather"][0]["description"].capitalize()
        temperature = round(weather_data["main"]["temp"], 1)  
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        
        message = f"\nA {colored(city.upper(), 'red')} la media attuale, indica una temperatura di {colored(temperature, 'cyan')}°C, umidità del {colored(humidity, 'yellow')}%, e vento di {colored(wind_speed, 'cyan')} km/n.\n"
        
        for char in message:
            print(char, end='', flush=True)
            time.sleep(0.05)  

        print()  
    
    else:
        print("Si è verificato un errore durante la richiesta delle informazioni sul meteo.")
