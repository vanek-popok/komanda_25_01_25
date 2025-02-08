
import telebot
from makzoro import makzoro

bot = telebot.TeleBot("7333117946:AAFa98LJs9CJu17eTM7pLB-mVmkWfqA_5Co")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(commands=['makzoro'])
def makz(message):
    makzoroFUNC(message, bot)