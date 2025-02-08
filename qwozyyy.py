
def qwozyyy(message, bot, types):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Кнопка 1", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Кнопка 2", callback_data="button2")
    keyboard.add(button1, button2)
    bot.send_message(chat_id=chat_id, text="Выберите кнопку:", reply_markup=keyboard)

