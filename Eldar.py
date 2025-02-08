import random #Для того чтобы был рандом
def eldar(message, bot):
    random_number = random.randint(1, 5) #генерация чисел
    bot.send_message(message.chat.id, random_number) #Вывод?



















