
import telebot
from baha import baha
from telebot import types
bot = telebot.TeleBot("7333117946:AAFa98LJs9CJu17eTM7pLB-mVmkWfqA_5Co")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(commands=['baha'])
def bah(message):
    baha(message, bot, types)


bot.infinity_pooling()