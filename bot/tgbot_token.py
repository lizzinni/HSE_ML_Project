import os
from dotenv import load_dotenv
import telebot
from telebot import TeleBot

load_dotenv()

my_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(my_token)