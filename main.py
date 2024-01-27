import logging

from collections import defaultdict

import telebot

from telebot import types

import buttons as b
import messages as m

from config import TOKEN, result_address_list

bot = telebot.TeleBot(TOKEN)

# logger = telebot.logger
# logger.setLevel(logging.DEBUG)

user_info = defaultdict(dict)


@bot.callback_query_handler(
    func=lambda call: 'region_button_pressed' in call.data)
def region_button_pressed(call):
    _, region = call.data.split(':')
    region_title = sorted(b.regions)[int(region)]
    user_info[call.message.chat.id]['region'] = region_title
    user_info[call.message.chat.id]['min_money'] = b.regions[region_title]
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.delete_message(call.message.chat.id, call.message.message_id + 1)
    bot.send_message(call.message.chat.id, 'Выбран регион: {}'.format(region_title))
    get_family_info(call.message)


# @bot.message_handler(commands=['start'])
def get_location(message):
    """выводит список регионов"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, region in enumerate(sorted(b.regions)):
        keyboard.add(
            types.InlineKeyboardButton(
                text=region,
                callback_data='region_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.location, reply_markup=keyboard)
    bot.send_message(message.chat.id, '{} ⬆️'.format(m.location))


@bot.callback_query_handler(
    func=lambda call: 'family_info_button_pressed' in call.data)
def family_info_button_pressed(call):
    _, info_idx = call.data.split(':')
    info_title, info_number = b.family_info[int(info_idx)]
    user_info[call.message.chat.id]['family_info'] = info_title
    user_info[call.message.chat.id]['family_info_number'] = info_number
    get_family_agge_info(call.message)


def get_family_info(message):
    """Опрашивает состав семьи."""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, (info, _) in enumerate(b.family_info):
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
    info_title = b.family_agge_info[int(info)]
    user_info[call.message.chat.id]['family_agge_info'] = info_title
    get_family_agge2_info(call.message)


def get_family_agge_info(message):
    """узнает сколько детей младше 18"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(b.family_agge_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='family_agge_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.family_agge_info, reply_markup=keyboard)


def get_family_count(message):
    print(user_info[message.chat.id])
    bot.send_message(message.chat.id, m.get_family_count)
    bot.register_next_step_handler(message, save_family_count)


def save_family_count(message):
    if message.text.isdigit():
        user_info[message.chat.id]['family_count'] = int(message.text)
        get_family_invalid_info(message)
    else:
        bot.send_message(message.chat.id, m.get_family_count_error)
        get_family_count(message)


@bot.callback_query_handler(
    func=lambda call: 'family_agge2_info_button_pressed' in call.data)
def family_agge2_info_button_pressed(call):
    user_info[call.message.chat.id]['family1_work_info'] = []
    _, info = call.data.split(':')
    children_count = int(info)
    info_title = b.family_agge2_info[children_count]
    user_info[call.message.chat.id]['family_agge2_info'] = info_title
    if children_count:
        user_info[call.message.chat.id]['current_child_no_18_23'] = 1
        user_info[call.message.chat.id]['children_18_23_count'] = children_count
        get_family1_work_info(call.message)
    else:
        get_family_count(call.message)


# @bot.message_handler(commands=['start'])
def get_family_agge2_info(message):
    """узнает сколько детей старше 18 и моложе 23"""
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
    info_title = b.get_family_invalid_info[int(info)]
    user_info[call.message.chat.id]['get_family_invalid_info'] = info_title
    get_user_ps_info(call.message)


def get_family_invalid_info(message):
    """узнает есть ли инвалидность"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(b.get_family_invalid_info):
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
    info_title = b.get_user_ps_info[int(info)]
    user_info[call.message.chat.id]['get_user_ps_info'] = info_title
    get_user_work_info(call.message)


def get_user_ps_info(message):
    """псих аль нет"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, info in enumerate(b.get_user_ps_info):
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
    _, answer = b.get_user_work_info[int(info)]
    user_info[call.message.chat.id]['get_user_work_info'] = answer
    get_family_work_info(call.message)


def get_user_work_info(message):
    """есть ли у заявителя работа или нет"""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, (info, _) in enumerate(b.get_user_work_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='get_user_work_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m. get_user_work_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'get_family_work_info_button_pressed' in call.data)
def get_family_work_info_button_pressed(call):
    _, info = call.data.split(':')
    _, answer = b. get_family_work_info[int(info)]
    user_info[call.message.chat.id]['get_family_work_info'] = answer
    get_summ_cash(call.message)


def get_family_work_info(message):
    """есть работа у супруга или нет"""
    if user_info[message.chat.id]['family_info_number'] == 0:
        get_summ_cash(call.message)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, (info, _) in enumerate(b.get_family_work_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='get_family_work_info_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.get_family_work_info, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'get_family1_work_info_button_pressed' in call.data)
def get_family1_work_info_button_pressed(call):
    _, info = call.data.split(':')
    info_title = b.get_family1_work_info[int(info)][1]
    if user_info[call.message.chat.id].get('family1_work_info'):
        user_info[call.message.chat.id]['family1_work_info'].append(info_title)
    else:
        user_info[call.message.chat.id]['family1_work_info'] = [info_title]
    user_info[call.message.chat.id]['children_18_23_count'] -= 1
    if user_info[call.message.chat.id]['children_18_23_count'] > 0:
        user_info[call.message.chat.id]['current_child_no_18_23'] += 1
        get_family1_work_info(call.message)
    else:
        get_family_count(call.message)


def get_family1_work_info(message):
    """есть работа у детей"""
    child_no = user_info[message.chat.id]['current_child_no_18_23']
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, (info, _) in enumerate(b.get_family1_work_info):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='get_family1_work_info_button_pressed:{}'.format(idx),
            )
        )
    family1_work_info = {'{}. {}'.format(child_no, m.get_family1_work_info)}
    bot.send_message(message.chat.id, family1_work_info, reply_markup=keyboard)


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


def report(info):
    with open('report.txt', encoding='utf8') as f:
        template = f.read()
    doc = template.format(
        name=info['name'],
        age=info['age'],
        region_min_money=info['min_money'],
        region=info['region'],
        family_info=info['family_info'],
        children_0_18=info['family_agge_info'],
        children_18_23=info['family_agge2_info'],
    )
    return doc

@bot.message_handler(commands=['start'])
def result(message):
    user_info[message.chat.id] = {
        'name': 'Иванов Иван',
        'age': 40,
        'region': 'Курганская область',
        'min_money': 20_000,
        'family_info': 'Замужем / женат',
        'family_agge_info': 'двое детей',
        'family_agge2_info': 'трое детей',
        'summ_cash': 100_000,
        'family_count': 6,
        'get_user_work_info': 1,
        'get_family_work_info': 1,
        'family1_work_info': [1, 1, 1],
        'get_family_invalid_info': 'нет ни у кого',
        'get_user_ps_info': 'нет, не стою на учете',
        'possession_info': [0, 2, 4],
        'why_money': 1,
    }
    # Состав данных user_info[message.chat.id]
    # - min_money - прожиточный минимум в регионе
    #
    # - get_user_work_info - есть ли у заявителя работа = 0 / 1
    # - get_family_work_info - есть ли у супруга работа = 0 / 1
    # - family1_work_info - есть ли работа у детей 18-23 = [1, 0, ...]
    # - summ_cash - доход семьи, включая дополнительный

    # 1: суммарный доход семьи меньше прожиточного минимума
    case1 = ((user_info[message.chat.id]['summ_cash']
              / user_info[message.chat.id]['family_count'])
             < user_info[message.chat.id]['min_money'])
    # 2: все члены семьи, старше 18, имеют доход
    case2 = all([
        user_info[message.chat.id]['get_user_work_info'],
        user_info[message.chat.id]['get_family_work_info'],
        all(user_info[message.chat.id]['family1_work_info']),
    ])
    # 3: ни у кого нет инвалидности
    case3 = user_info[message.chat.id]['get_family_invalid_info'] == 'нет ни у кого'
    # 4: у заявителя нет психических проблем
    case4 = user_info[message.chat.id]['get_user_ps_info'] == 'нет, не стою на учете'
    # 5: проверка имущества
    possessions = [b.possession_info[choice][1] for choice in user_info[message.chat.id]['possession_info']]
    case5 = not any(possessions)
    # 6: для чего нужны средства
    case6 = b.why_money[user_info[message.chat.id]['why_money']][1] == 0
    case = all([
        case1,
        case2,
        case3,
        case4,
        case5,
        case6,
    ])
    answer = 'Вы проходите' if case else 'Вы не проходите'
    bot.send_message(message.chat.id, answer)

    text = 'Результаты анкеты {} @{}\n\n{}\n\n{}'.format(
        user_info[message.chat.id]['name'],
        message.chat.username,
        answer,
        report(user_info[message.chat.id]),
    )
    for address in result_address_list:
        bot.send_message(address, text)


@bot.callback_query_handler(
    func=lambda call: 'why_money_button_pressed' in call.data)
def why_money_button_pressed(call):
    _, info = call.data.split(':')
    info_title = b.why_money[int(info)]
    user_info[call.message.chat.id]['why_money'] = info_title
    result(call.message)


def why_money(message):
    """На что вам необходимы средства."""
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for idx, (info, info_idx) in enumerate(b.why_money):
        keyboard.add(
            types.InlineKeyboardButton(
                text=info,
                callback_data='why_money_button_pressed:{}'.format(idx),
            )
        )
    bot.send_message(message.chat.id, m.why_money, reply_markup=keyboard)


@bot.callback_query_handler(
    func=lambda call: 'possession_info_button_pressed' in call.data)
def possession_info_button_pressed(call):
    _, info = call.data.split(':')
    if info == 'end':
        why_money(call.message)
    else:
        choice = int(info)
        possession_info = user_info[call.message.chat.id].get('possession_info')
        if not possession_info:
            possession_info = []
        if choice in possession_info:
            possession_info.remove(choice)
        else:
            possession_info.append(choice)
        user_info[call.message.chat.id]['possession_info'] = possession_info
        get_possession_info(call.message)


# @bot.message_handler(commands=['start'])
def get_possession_info(message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    possession_info = user_info[message.chat.id].get('possession_info')
    if not possession_info:
        possession_info = []
    for idx, (text, p_idx) in enumerate(b.possession_info):
        if idx in possession_info:
            checkbox = '☑'
        else:
            checkbox = '☐'
        keyboard.add(
            types.InlineKeyboardButton(
                text='{} {}'.format(checkbox, text),
                callback_data='possession_info_button_pressed:{}'.format(idx),
            )
        )
    keyboard.add(
        types.InlineKeyboardButton(
            text='▶️ Продолжить',
            callback_data='possession_info_button_pressed:end',
        )
    )
    bot.send_message(message.chat.id, m.possession_info, reply_markup=keyboard)


def get_age(message):
    bot.send_message(message.chat.id, m.get_age)
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


def get_name(message):
    bot.send_message(message.chat.id, m.get_name)
    bot.register_next_step_handler(message, save_name)


def save_name(message):
    user_info[message.chat.id]['name'] = message.text.title()
    get_age(message)


# @bot.message_handler(commands=['start'])
def start_message(message):
    if user_info[message.chat.id] and 'why_money' in user_info[call.message.chat.id]:
        bot.send_message(message.chat.id, 'Анкету можно заполнять только один раз.')
        result(message)
    client = message.chat.first_name
    bot.send_message(message.chat.id, m.start.format(client))
    get_name(message)


@bot.message_handler(commands=['id'])
def get_chat_id(message):
    bot.send_message(message.chat.id, message.chat.id)


bot.infinity_polling()
