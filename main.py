import logging

from collections import defaultdict

import telebot

from telebot import types

import buttons as b
import messages as m

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

logger = telebot.logger
logger.setLevel(logging.DEBUG)

user_info = defaultdict(dict)


@bot.callback_query_handler(
    func=lambda call: 'region_button_pressed' in call.data)
def region_button_pressed(call):
    _, region = call.data.split(':')
    region_title = sorted(b.regions)[int(region)]
    user_info[call.message.chat.id]['region'] = region_title
    user_info[call.message.chat.id]['money'] = b.regions[region_title]
    get_family_info(call.message)


def get_location(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, region in enumerate(sorted(b.regions)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=region,
                callback_data='region_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.location, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'family_info_button_pressed' in call.data)
def family_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b.family_info)[int(info)]
    user_info[call.message.chat.id]['family_info'] = info_title
    bot.send_message(call.message.chat.id, str(user_info))


def get_family_info(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b.family_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='family_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.family_info, reply_markup=keyboard)


def get_age(message):
    bot.send_message(message.chat.id, m.age)
    bot.register_next_step_handler(message, save_age)


def save_age(message):
    try:
        age = int(message.text)
        user_info[message.chat.id]['age'] = age
        if age <= 25:
            bot.send_message(message.chat.id, m.age25)
    except ValueError:
        bot.send_message(message.chat.id, m.age_error)
        get_age(message)
    get_location(message)


def get_user_name(message):
    user_info[message.chat.id]['name'] = message.text.title()
    get_age(message)


@bot.message_handler(commands=['start'])
def start_message(message):
    client = message.chat.first_name
    bot.send_message(message.chat.id, m.start.format(client))
    bot.register_next_step_handler(message, get_user_name)


bot.infinity_polling()
