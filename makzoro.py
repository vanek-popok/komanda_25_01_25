def makzoroFUNC(message, bot):
    if message.text.lower() == "привет":
        bot.reply_to(message, "Привет, Как дела?")
    if message.text.lower() == "пока":
            bot.reply_to(message, "Хорошего дня/вечера")