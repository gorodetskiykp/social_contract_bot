regions = {
    'Республика Адыгея': 13290,
    'Республика Башкортостан': 13753,
    'Республика Бурятия': 15669,
    'Республика Алтай (Горный Алтай)': 13753,
    'Республика Дагестан': 14062,
    'Республика Ингушетия': 14339,
    'Кабардино-Балкарская Республика': 16535,
    'Республика Калмыкия': 14644,
    'Республика Карачаево-Черкессия': 14186,
    'Республика Карелия': 18592,
    'Республика Коми': 18389,
    'Республика Марий Эл': 13424,
    'Республика Мордовия': 12966,
    'Республика Саха (Якутия)': 23034,
    'Республика Северная Осетия — Алания': 13729,
    'Республика Татарстан': 13135,
    'Республика Тыва': 15608,
    'Удмуртская Республика': 13753,
    'Республика Хакасия': 15762,
    'Чувашская Республика': 13271,
    'Алтайский край': 13753,
    'Краснодарский край': 14835,
    'Красноярский край': 17153,
    'Приморский край': 18152,
    'Ставропольский край': 13729,
    'Хабаровский край': 19937,
    'Амурская область': 17823,
    'Архангельская область': 16675,
    'Астраханская область': 14796,
    'Белгородская область': 12981,
    'Брянская область': 14102,
    'Владимирская область': 14796,
    'Волгоградская область': 13118,
    'Вологодская область': 15608,
    'Воронежская область': 13271,
    'Ивановская область': 14339,
    'Иркутская область': 16169,
    'Калининградская область': 15917,
    'Калужская область': 14644,
    'Камчатский край': 27549,
    'Кемеровская область': 13881,
    'Кировская область': 13576,
    'Костромская область': 14034,
    'Курганская область': 14526,
    'Курская область': 13271,
    'Ленинградская область': 16017,
    'Липецкая область': 12826,
    'Магаданская область': 26542,
    'Московская область': 18296,
    'Мурманская область': 24413,
    'Нижегородская область': 14339,
    'Новгородская область': 15144,
    'Новосибирская область': 15317,
    'Омская область': 13723,
    'Оренбургская область': 13444,
    'Орловская область': 14186,
    'Пензенская область': 12813,
    'Пермский край': 14034,
    'Псковская область': 15101,
    'Ростовская область': 14339,
    'Рязанская область': 13576,
    'Самарская область': 14339,
    'Саратовская область': 12813,
    'Сахалинская область': 20745,
    'Свердловская область': 15300,
    'Смоленская область': 14949,
    'Тамбовская область': 13308,
    'Тверская область': 14796,
    'Томская область': 15059,
    'Тульская область': 15254,
    'Тюменская область': 15453,
    'Ульяновская область': 13576,
    'Челябинская область': 14279,
    'Забайкальский край': 18080,
    'Ярославская область': 14949,
    'Санкт-Петербург': 18023,
    'Еврейская автономная область': 20185,
    'Республика Крым': 14796,
    'Ненецкий автономный округ': 27890,
    'Ханты-Мансийский автономный округ — Югра': 20435,
    'Чукотский автономный округ': 39813,
    'Ямало-Ненецкий автономный округ': 21760,
    'Севастополь': 17181,
    'Чеченская республика': 14644,
}

family_info = (
    'Замужем / женат',
    'Холост / не замужем / в разводе',
    'Проживаю в гражданском браке',
    'Вдова / Вдовец',
)

family_agge_info = (
    'нет детей',
    'один ребенок',
    'двое детей',
    'трое детей',
    'четверо детей',
    'пятеро детей',
)

family_agge2_info = (
    # Значения справочника используются в коде!!!
    # 'нет' должен стоять на 0 позиции
    'нет',  # 0
    'один ребенок',  # 1
    'двое детей',
    'трое детей',
    'четверо детей',
)

get_family_invalid_info = (
    'инвалидности нет ни у кого',
    'инвалидность есть у меня',
    'инвалидность есть у супруга/супруги',
    'инвалидность есть у ребенка',
)

get_user_ps_info = (
    'нет, не стою на учете',
    'да, стою на учете',
)

get_user_work_info = (
    'да, есть официальное трудоустройство',
    'не работаю, работаю не официально',
    'есть ИП',
    'есть ООО (только учредитель)',
    'есть ООО (учредитель и директор)',
    'самозанятый/ая',
)

get_family_work_info = (
    'официально трудоустроен/на',
    'не работает, работает не официально',
    'есть ИП',
    'есть ООО (только учредитель)',
    'есть ООО (учредитель и директор)',
    'самозанятый/ая',
)

get_family1_work_info = (
    'есть место учебы',
    'работает официально',
    'работает не официально',
    'инное',
)

get_cash_info = (
    'сдача в аренду имущества (авто, недвижимость)',
    'получение пособийб пенсий( любые выплаты от государства, в том числе единое пособие',
    'возврат процентов по кредиту, возврат подоходного налога',
    'продажа имущества (авто, квартира, дача и т.д.',
    'проценты по вкладам в банке',
    'стипендия',
    'нет дополнительного дохода',
)

possession_info = (
    'Дом',
    'Машина',
)
