
import telebot
from Eldar import eldar
from telebot import types

from makzoro import makzoro
from baha import baha
from telebot import types


from ivan import ivanvan


from andrey import andreyFunc
from telebot import types


from qwozyyy import qwozyyyFunc
from teebot import types
>>>>>>> dd5da23c9f9b5e2ba6298bd611688d500ae9b5af

bot = telebot.TeleBot("7333117946:AAFa98LJs9CJu17eTM7pLB-mVmkWfqA_5Co")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет")


@bot.message_handler(commands=["edik"])
def edik(message):
    eldar(message, bot)

@bot.message_handler(commands=['makzoro'])
def makz(message):
    makzoroFUNC(message, bot)

@bot.message_handler(commands=['baha'])
def bah(message):
    baha(message, bot, types)


@bot.message_handler(commands=['ivan'])
def ivan(message):
    ivanvan(message,bot)



@bot.message_handler(commands=['andrey'])
def andre(message):
    andreyFunc(message, bot, types)


@bot.message_handler(commands=['qwozyyy'])
def qwozyyy(message):
    qwozyyyFunc(message, bot, types)




bot.infinity_pooling()

