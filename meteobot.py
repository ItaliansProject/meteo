import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text("Benvenuto! Inviami il nome di una città per ottenere le informazioni meteo.")

def echo(update, context):
    city = update.message.text
    api_key = context.bot_data['api_key']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        description = weather_data["weather"][0]["description"].capitalize()
        temperature = round(weather_data["main"]["temp"], 1)
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        message = f"A {city.upper()} la media attuale, indica una temperatura di {temperature}°C, umidità del {humidity}%, e vento di {wind_speed} km/n."
        update.message.reply_text(message)
    else:
        update.message.reply_text("Si è verificato un errore durante la richiesta delle informazioni sul meteo.")

def main():
    
    TOKEN = input("Inserisci il token del tuo bot Telegram: ")
    
    api_key = input("Inserisci la tua API key generata tramite openweathermap.org: ")

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    
    updater.dispatcher.bot_data['api_key'] = api_key

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()
