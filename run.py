import os
from PIL import Image

import telebot
from telebot import types  # add-ons connected

bot = telebot.TeleBot("1777047041:AAG5OtIuQ1Ct-aPvyt1ZSR74eDrOSJ7IU0U")

menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
coffee_list_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
serve_or_menu_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
tea_list = telebot.types.ReplyKeyboardMarkup(True, True)
bakery_list = telebot.types.ReplyKeyboardMarkup(True, True)

menu_keyboard.row('Кофе☕️', 'Чай🍵', 'Выпечка🍩', 'Акции🤩')
coffee_list_keyboard.row('Латте', 'Капучино', 'Эспрессо')
tea_list.row('Черный чай🧉', 'Зеленый чай🍵')
serve_or_menu_keyboard.row('Меню🔖', 'Оформить заказ🙋🏻')
bakery_list.row('Чизкейк🍰', 'Круассан🥐', 'Печенье с шоколодом🍪')


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)  # Connect the keyboard
    # Specify the name
    # of the button that the user will see
    button_phone = types.KeyboardButton(text="Отправить номер телефона📱", request_contact=True)
    keyboard.add(button_phone)  # Add this button
    bot.send_message(
        message.chat.id,
        'Вас приветствует Бот кофейни Гвоздь ☕️🥨.'
        '\nДля того чтобы мы могли принять Ваш заказ нам необходимо знать Ваш номер телефона.'
        '\nПожалуйста, нажмите кнопку отправки номера чтобы продолжить)⬇️',
        reply_markup=keyboard)
    directory = os.getcwd()
    with open(directory + '/' + "gvozd_logo.png", "rb") as image:
        bot.send_photo(message.chat.id, image)


@bot.message_handler(content_types=['contact'])
def show_menu(message):
    print(message.contact.phone_number)
    bot.send_message(message.chat.id, "Отлитчно, теперь Вы можете оформить Ваш заказ 😉", reply_markup=menu_keyboard)


@bot.message_handler(content_types=['text'])
def process_answers(message):
    if "Кофе" in message.text:
        bot.send_message(message.chat.id,
                         "Окей)"
                         "\nКакой Вы предпочтете?",
                         reply_markup=coffee_list_keyboard)
    elif "Чай" in message.text:
        bot.send_message(message.chat.id,
                         "Окей)"
                         "\nКакой Вы предпочтете?",
                         reply_markup=tea_list)
    elif "Выпечка" in message.text:
        bot.send_message(message.chat.id,
                         "Окей)"
                         "\nКакой Вы предпочтете?",
                         reply_markup=bakery_list)
    elif "Латте" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "latte.png", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Капучино" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "cappuccino.jpeg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Эспрессо" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "espresso.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Черный чай" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "black_tea.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Зеленый чай" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "green_tea.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Чизкейк" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "cheese_cake.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Круассан" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "croissant.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Печенье" in message.text:
        bot.send_message(message.chat.id,
                         "Хороший выбор 😏"
                         "\nВы можете вернутся в меню, если хотите добавить еще что-то в заказ."
                         "\nЛибо нажмите кнопку оформления заказа 👌",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "cookies.jpg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Акции" in message.text:
        bot.send_message(message.chat.id,
                         "При первом заказе через нашего Бота,"
                         "\nВы получите вкусный бонус 😄🥰😏",
                         reply_markup=serve_or_menu_keyboard
                         )
        directory = os.getcwd()
        with open(directory + '/' + "present.jpeg", "rb") as image:
            bot.send_photo(message.chat.id, image)
    elif "Меню" in message.text:
        bot.send_message(message.chat.id, "Пожалуйста, выберите что Вас интересует 😉", reply_markup=menu_keyboard)
    elif "Оформить заказ" in message.text:
        bot.send_message(message.chat.id,
                         "Оки-доки. Начинаем готовить Ваш заказ 😋"
                         "\nМы свяжемся с Вами в течении 5 минут⏰"
                         , reply_markup=menu_keyboard)
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAANcYFZlCC7vAgENrOEFlw-3a32Swz4AAjcHAAJjK-IJo5ws6zpnLQ0eBA")


@bot.message_handler(content_types=['sticker'])
def print_sticker_id(message):
    print(message)


bot.polling(none_stop=True)
