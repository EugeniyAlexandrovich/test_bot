import telebot
from telegram_bot_pagination import InlineKeyboardPaginator

bot = telebot.TeleBot("***")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    with open("text/Greeting.txt", "r", encoding="utf-8") as file:
        text = file.read()
    bot.send_message(message.from_user.id, text)


@bot.message_handler(content_types=['text'])
def all_message(message):
    try:
        global check
        check = message.text
        if message.text == "Старт":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("улица Рождественка", "Кузнецкий мост", "Звонарский переулок")
            keyboard.row("Сандуновский переулок", "Варсонофьевский переулок")
            keyboard.row("Большой, Малый и Нижний Кисельные переулки")
            bot.send_message(message.from_user.id, text="Предлагаю тебе определиться с нашим маршрутом. Я," +
                             "конечно, советую начать с Рождественки, но если ты там уже всё знаешь, " +
                                                        "то можешь выбрать другой маршрут.",
                             reply_markup=keyboard)
        # 1
        if message.text == "улица Рождественка":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("Кузнецкий мост", "Звонарский переулок", "Сандуновский переулок")
            keyboard.row("Варсонофьевский переулок", "Большой, Малый и Нижний Кисельные переулки")
            keyboard.row("Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)   # удаление сообщения пользователя
            send_text(message)
        # 2
        elif message.text == 'Кузнецкий мост':
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("Звонарский переулок", "Сандуновский переулок", "Варсонофьевский переулок")
            keyboard.row("Большой, Малый и Нижний Кисельные переулки", "улица Рождественка")
            keyboard.row("Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)
            send_text(message)
        # 3
        elif message.text == "Звонарский переулок":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("Сандуновский переулок", "Варсонофьевский переулок")
            keyboard.row("Большой, Малый и Нижний Кисельные переулки", "улица Рождественка")
            keyboard.row("Кузнецкий мост", "Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)
            send_text(message)
        # 4
        elif message.text == "Сандуновский переулок":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("Варсонофьевский переулок", "Большой, Малый и Нижний Кисельные переулки")
            keyboard.row("улица Рождественка", "Кузнецкий мост")
            keyboard.row("Звонарский переулок", "Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)
            send_text(message)
        # 5
        elif message.text == "Варсонофьевский переулок":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("Большой, Малый и Нижний Кисельные переулки")
            keyboard.row("улица Рождественка", "Кузнецкий мост", "Звонарский переулок")
            keyboard.row("Сандуновский переулок", "Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)
            send_text(message)
        # 6
        elif message.text == "Большой, Малый и Нижний Кисельные переулки":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row("улица Рождественка", "Кузнецкий мост", "Звонарский переулок")
            keyboard.row("Сандуновский переулок", "Варсонофьевский переулок", "Продолжим в другой раз")
            bot.send_message(message.chat.id, text=message.text, reply_markup=keyboard)
            bot.delete_message(message.chat.id, message.message_id)
            send_text(message)
        # end
        elif message.text == 'Продолжим в другой раз':
            bot.send_message(message.from_user.id, text="Спасибо, что составил мне компанию! Надеюсь, тебе было" +
                                                        " интересно. Если соскучишься по прогулкам, то пиши мне — я " +
                                                        "снова проведу для тебя онлайн-экскурсию по московским улицам.",
                             reply_markup=telebot.types.ReplyKeyboardRemove())
    except:
        pass


@bot.callback_query_handler(func=lambda call: call.data.split("#")[0] == 'element')
def callback_inline(call):
    page = int(call.data.split("#")[1])
    bot.delete_message(call.message.chat.id, call.message.message_id)
    send_text(call.message, page)


def send_text(message, page=1):
    try:
        # 1
        if check == "улица Рождественка":
            with open("text/rozhdestvenka.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 5:
                bot.send_photo(message.chat.id, open("image/Rozhdestvenka_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 11:
                bot.send_photo(message.chat.id, open("image/Rozhdestvenka_image_2.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 12:
                bot.send_photo(message.chat.id, open("image/Rozhdestvenka_image_3.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 19:
                bot.send_photo(message.chat.id, open("image/Rozhdestvenka_image_4.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
        # 2
        if check == "Кузнецкий мост":
            with open("text/kuznetsky_most.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 3:
                bot.send_photo(message.chat.id, open("image/kuznetsky_most_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 6:
                bot.send_photo(message.chat.id, open("image/kuznetsky_most_image_2.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 18:
                bot.send_photo(message.chat.id, open("image/kuznetsky_most_image_3.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
        # 3
        if check == "Звонарский переулок":
            with open("text/zvonarsky_lane.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 4:
                bot.send_photo(message.chat.id, open("image/zvonarsky_lane_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
        # 4
        if check == "Сандуновский переулок":
            with open("text/sandunovsky_lane.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 3:
                bot.send_photo(message.chat.id, open("image/sandunovsky_lane_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
        # 5
        if check == "Варсонофьевский переулок":
            with open("text/varsonofievsky_lane.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 5:
                bot.send_photo(message.chat.id, open("image/varsonofievsky_lane_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            elif page == 6:
                bot.send_photo(message.chat.id, open("image/varsonofievsky_lane_image_2.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
        # 6
        if check == "Большой, Малый и Нижний Кисельные переулки":
            with open("text/kiselny_lanes.txt", "r", encoding="utf-8") as file:
                text = file.readlines()
            paginator = InlineKeyboardPaginator(len(text), current_page=page, data_pattern="element#{page}")
            if page == 7:
                bot.send_photo(message.chat.id, open("image/kiselny_lanes_image_1.jpg", "rb"),
                               caption=text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
            else:
                bot.send_message(message.chat.id, text[page - 1], reply_markup=paginator.markup, parse_mode="Markdown")
    except:
        pass


if __name__ == "__main__":
    bot.polling(none_stop=True)
