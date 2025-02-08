

def baha(message, bot, types):
        markup_inline = types.InlineKeyboardMarkup()

        btn_m = types.InlineKeyboardButton(text="Мем", callback_data="Мем")
        btn_h = types.InlineKeyboardButton(text="Шутка", callback_data="Шутка")

        markup_inline.add(btn_m,btn_h)
        bot.send_message(message.chat.id, "Мем или шутка?", reply_markup=markup_inline)