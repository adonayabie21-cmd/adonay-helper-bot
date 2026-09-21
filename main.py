import os
import threading
from flask import Flask
import telebot

# Simple HTTP Web Server for Render Health Checks
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# Start Web Server in Background Thread
threading.Thread(target=run_flask).start()

# Telegram Bot Setup
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "ሰላም! ቦቱ በ Render.com ላይ 24/7 በትክክል እየሰራ ነው!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    bot.infinity_polling()

