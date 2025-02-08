
import telebot
from qwozyyy import qwozyyyFunc
from teebot import types
bot = telebot.TeleBot("7333117946:AAFa98LJs9CJu17eTM7pLB-mVmkWfqA_5Co")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(commands=['qwozyyy'])
def qwozyyy(message):
    qwozyyyFunc(message, bot, types)
