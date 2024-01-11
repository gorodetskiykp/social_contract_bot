import logging

import telebot

from telebot import types

import messages as m

from buttons import regions
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

logger = telebot.logger
logger.setLevel(logging.DEBUG)

user_info = {}


@bot.callback_query_handler(
    func=lambda call: 'region_button_pressed' in call.data)
def region_button_pressed(call):
    print(call)
    _, region = call.data.split(':')
    user_info['region'] = region
    bot.send_message(call.message.chat.id, str(user_info))


def get_location(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for region in regions:
        keyboard.add(
            types.InlineKeyboardButton(
                text=region,
                callback_data='region_button_pressed:{}'.format(region),
            )
        )
    bot.send_message(message.chat.id, m.location, reply_markup=keyboard)


def get_age(message):
    bot.send_message(message.chat.id, m.age)
    bot.register_next_step_handler(message, save_age)


def save_age(message):
    try:
        user_info['age'] = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, m.age_error)
        get_age(message)
    get_location(message)


def get_user_name(message):
    user_info['name'] = message.text.title()
    get_age(message)


@bot.message_handler(commands=['start'])
def start_message(message):
    client = message.chat.first_name
    bot.send_message(message.chat.id, m.start.format(client))
    bot.register_next_step_handler(message, get_user_name)


bot.infinity_polling(none_stop=True)
