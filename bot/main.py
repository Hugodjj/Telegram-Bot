import dotenv
import telebot
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

dcc_bot = telebot.TeleBot(API_KEY)

def main():
    dcc_bot.polling()

main()