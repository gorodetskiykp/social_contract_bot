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


# @bot.message_handler(commands=['start'])
def get_location(message):  # выводит список регионов
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, region in enumerate(sorted(b.regions)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=region,
                callback_data='region_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.location, reply_markup=keyboard)
    # bot.send_message(message.chat.id, '{} ⬆️'.format(m.location))


@bot.callback_query_handler(
    func=lambda call: 'family_info_button_pressed' in call.data)
def family_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = b.family_info[int(info)]
    user_info[call.message.chat.id]['family_info'] = info_title
    get_family_agge_info(call.message)


def get_family_info(message):
    """Опрашивает состав семьи."""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(b.family_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='family_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.family_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'family_agge_info_button_pressed' in call.data)
def family_agge_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b.family_agge_info)[int(info)]
    user_info[call.message.chat.id]['family_agge_info'] = info_title
    #bot.send_message(call.message.chat.id, str(user_info))
    get_family_agge2_info(call.message)


def get_family_agge_info(message):  # узнает сколько детей младше 18
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b.family_agge_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='family_agge_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.family_agge_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'family_agge2_info_button_pressed' in call.data)
def family_agge2_info_button_pressed(call):
    _, info = call.data.split(':')
    children_count = int(info)
    info_title = b.family_agge2_info[children_count]
    user_info[call.message.chat.id]['family_agge2_info'] = info_title
    # if children_count:
    #     get_family1_work_info(message)
    get_family_invalid_info(call.message)


def get_family_agge2_info(message):  #  узнает сколько детей старше 18 и моложе 23
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(b.family_agge2_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='family_agge2_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.family_agge2_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'get_family_invalid_info_button_pressed' in call.data)
def get_family_invalid_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b.get_family_invalid_info)[int(info)]
    user_info[call.message.chat.id]['get_family_invalid_info'] = info_title
    get_user_ps_info(call.message)


def get_family_invalid_info(message):  #  узнает есть ли инвалидность
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b.get_family_invalid_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='get_family_invalid_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.get_family_invalid_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'get_user_ps_info_button_pressed' in call.data)
def get_user_ps_invalid_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b.get_user_ps_info)[int(info)]
    user_info[call.message.chat.id]['get_user_ps_info'] = info_title
    get_user_work_info(call.message)


def get_user_ps_info(message):  #  псих аль нет
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b.get_user_ps_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='get_user_ps_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.get_user_ps_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: ' get_user_work_info_button_pressed' in call.data)
def get_user_work_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b. get_user_work_info)[int(info)]
    user_info[call.message.chat.id][' get_user_work_info'] = info_title
    get_family_work_info(call.message)


def get_user_work_info(message):  #  есть работа или нет
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b. get_user_work_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data=' get_user_work_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m. get_user_work_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: ' get_family_work_info_button_pressed' in call.data)
def get_family_work_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b. get_family_work_info)[int(info)]
    user_info[call.message.chat.id]['get_family_work_info'] = info_title
    get_cash_info(call.message)


def get_family_work_info(message):  #  есть работа у супруга или нет
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b. get_family_work_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data=' get_family_work_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m. get_family_work_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: ' get_family1_work_info_button_pressed' in call.data)
def get_family1_work_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b.get_family1_work_info)[int(info)]
    user_info[call.message.chat.id][' get_family1_work_info'] = info_title
    get_cash_info(call.message)


def get_family1_work_info(message):  #  есть работа у детей
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b. get_family1_work_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data=' get_family1_work_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m. get_family1_work_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: ' get_cash_info_button_pressed' in call.data)
def get_cash_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = sorted(b. get_cash_info)[int(info)]
    user_info[call.message.chat.id]['get_cash_info'] = info_title
    bot.send_message(call.message.chat.id, str(user_info))
    get_summ_cash(message)


def get_cash_info(message):  #  есть ли дополнительный доход
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(sorted(b. get_cash_info)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data=' get_cash_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m. get_cash_info, reply_markup=keyboard)


def get_summ_cash(message):
    bot.send_message(message.chat.id, m.get_summ_cash)
    bot.register_next_step_handler(message, save_summ_cash)


def save_summ_cash(message):
    try:
        summ_cash = int(message.text)
        user_info[message.chat.id]['summ_cash'] = summ_cash
    except ValueError:
        bot.send_message(message.chat.id, m.summ_cash_error)
        get_summ_cash(message)
    get_possession_info(message)  # есть ли имущество


@bot.callback_query_handler(
    func=lambda call: 'possession_info_button_pressed' in call.data)
def possession_info_button_pressed(call):
    _, info = call.data.split(':')
    if info == 'end':
        result(message)
    else:
        choice = int(info)
        info_title = b.possession[choice]
        possession_info = user_info[call.message.chat.id].get('possession_info')
        if not possession_info:
            possession_info = []
        if choice in possession_info:
            pass
        else:
            possession_info.add(choice)
        user_info[call.message.chat.id]['possession_info'] = info_title
        get_possession_info(message)


@bot.message_handler(commands=['start'])
def get_possession_info(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    possession_info = user_info[call.message.chat.id].get('possession_info')
    if not possession_info:
        possession_info = []
    for idx, text in enumerate(b.possession):
        if idx in possession_info:
            checkbox = '✅'
        else:
            checkbox = '❎'
        keyboard.add(
            types.InlineKeyboardButton(
                text='{} {}'.format(checkbox, text),
                callback_data='possession_info_button_pressed:{}'.format(idx),
            )
        )
    keyboard.add(
        types.InlineKeyboardButton(
            text=text,
            callback_data='possession_info_button_pressed:end',
        )
    )
    bot.send_message(message.chat.id, m.possession_info, reply_markup=keyboard)


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


# @bot.message_handler(commands=['start'])
def start_message(message):
    client = message.chat.first_name
    bot.send_message(message.chat.id, m.start.format(client))
    bot.register_next_step_handler(message, get_user_name)


bot.infinity_polling()
