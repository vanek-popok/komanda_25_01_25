def Georgi(message, bot, types):
    if "мем" in text:
        bot.send_photo(message.chat.id, get("https://i.pinimg.com/736x/47/78/48/4778489809eb2388f98d884755a47532.jpg").content)
    elif "шутка" in text:
        bot.send_message(message.chat.id, "Почему шутить можно над всеми, кроме безногих?\n"
                                          "Шутки про них обычно не заходят.")