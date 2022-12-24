import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup as b4

API = '5833569406:AAFu2QEOGUauEu8H1G74AWj_6VznGshzJWc'

URL_KOLOBOK = 'https://nukadeti.ru/skazki/kolobok'
URL_TEREMOK = 'https://nukadeti.ru/skazki/teremok'
URL_MASHA_I_MEDVED = 'https://nukadeti.ru/skazki/masha_i_medved'
URL_KASHA_IZ_TOPORA = 'https://nukadeti.ru/skazki/kasha_iz_topora'
URL_REPKA = 'https://nukadeti.ru/skazki/repka'

URL_GUSI_LEBEDI = 'https://nukadeti.ru/skazki/gusi_lebedi'
URL_KROSHECHKA_HAVROSHECHKA = 'https://nukadeti.ru/skazki/kroshechka_khavroshechka'
URL_PRAVDA_I_KRIVDA = 'https://nukadeti.ru/skazki/pravda_i_krivda'
URL_TRI_BRATA = 'https://nukadeti.ru/skazki/bratya_grimm_tri_brata'
URL_SOLDAT_I_CHERT = 'https://nukadeti.ru/skazki/soldat_i_chert'

URL_TRI_MEDVEDYA = 'https://nukadeti.ru/skazki/tri_medvedya'
URL_ZIVAYA_SHLYAPA = 'https://nukadeti.ru/skazki/nosov_zhivaya_shlyapa'
URL_EZ = 'https://nukadeti.ru/skazki/prishvin-jozh'
URL_LISICHKIN_HLEB = 'https://nukadeti.ru/skazki/prishvin_lisichkin_khleb'
URL_VOLK_I_SEMERO_KOZLYAT = 'https://nukadeti.ru/skazki/bratya_grimm_volk_i_semero_kozlyat'

URL_DOCHGKA_PEKARYA = 'https://nukadeti.ru/skazki/dochka_pekarya'
URL_U_STRAHA_GLAZA_VELIKI = 'https://nukadeti.ru/skazki/u_strakha_glaza_veliki'
URL_O_MISHONKE = 'https://nukadeti.ru/skazki/marshak_skazka_o_glupom_myshonke'
URL_TRI_ZCHELANIYA = 'https://nukadeti.ru/skazki/tri_zhelaniya'
URL_OB_UMNOM = 'https://nukadeti.ru/skazki/skazka_ob_umnom_myshonke'

URL_KUROCHKA_RYABA = 'https://nukadeti.ru/skazki/kurochka_ryaba'
URL_LEV_I_SOBACHKA = 'https://nukadeti.ru/skazki/tolstoj-lev-i-sobachka'
URL_KOTENOK = 'https://nukadeti.ru/skazki/lev-tolstoj-kotenok'
URL_OGURCI = 'https://nukadeti.ru/skazki/nosov-ogurcy'
URL_TRI_COTENKA = 'https://nukadeti.ru/skazki/suteev_tri_kotjonka'

URL_MOIDODIR = 'https://nukadeti.ru/skazki/chukovskij_mojdodyr'
URL_FEDORINO_GORE = 'https://nukadeti.ru/skazki/chukovskij_fedorino_gore'
URL_VOT_KAKOI = 'https://nukadeti.ru/skazki/marshak-vot-kakoj-rasseyannyj'
URL_TIHAYA_SKAZKA = 'https://nukadeti.ru/skazki/marshak-tikhaya-skazka'


list_skazki = []


def parser(url):
    r = requests.get(url)
    soup = b4(r.text, 'html.parser')
    skazki = soup.find_all('div', class_="tale-text si-text")
    return [c.text for c in skazki]


bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_1 = types.KeyboardButton('Русские народные')
    item_2 = types.KeyboardButton('Волшебные сказки')
    item_3 = types.KeyboardButton('Сказки о животных')
    item_4 = types.KeyboardButton('Сказки для самых маленьких')
    item_5 = types.KeyboardButton('Короткие сказки ')
    item_6 = types.KeyboardButton('Сказки в стихах')
    markup.add(item_1,item_2, item_3, item_4, item_5, item_6)

    bot.send_message(message.chat.id, 'Привет,здесь собрана золотая коллекция детских сказок на все случаи жизни'.format(message.from_user),reply_markup=markup)

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_1 = types.KeyboardButton('Русские народные')
    item_2 = types.KeyboardButton('Волшебные сказки')
    item_3 = types.KeyboardButton('Сказки о животных')
    item_4 = types.KeyboardButton('Сказки для самых маленьких')
    item_5 = types.KeyboardButton('Короткие сказки ')
    item_6 = types.KeyboardButton('Сказки в стихах')
    markup.add(item_1,item_2, item_3, item_4, item_5, item_6)

    bot.send_message(message.chat.id, 'Выберите категорию сказок'.format(message.from_user),reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Русские народные':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Маша и медведь')
            item_2 = types.KeyboardButton('Теремок')
            item_3 = types.KeyboardButton('Колобок')
            item_4 = types.KeyboardButton('Репка')
            item_5 = types.KeyboardButton('Каша из топора')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, item_5, back)

            bot.send_message(message.chat.id,'Русские народные сказки'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Волшебные сказки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Гуси Лебеди')
            item_2 = types.KeyboardButton('Крошечка-Хаврошечка')
            item_3 = types.KeyboardButton('Правда и Кривда')
            item_4 = types.KeyboardButton('Три Брата')
            item_5 = types.KeyboardButton('Солдат и чёрт')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, item_5, back)

            bot.send_message(message.chat.id,'Волшебные сказки'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Сказки о животных':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Три Медведя')
            item_2 = types.KeyboardButton('Живая шляпа')
            item_3 = types.KeyboardButton('Ёж')
            item_4 = types.KeyboardButton('Лисичкин хлеб')
            item_5 = types.KeyboardButton('Волк и семеро козлят')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, item_5, back)

            bot.send_message(message.chat.id,'Сказки о животных'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Сказки для самых маленьких':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Дочка пекаря')
            item_2 = types.KeyboardButton('У страха глаза велики')
            item_3 = types.KeyboardButton('Сказка о глупом мышонке')
            item_4 = types.KeyboardButton('Три желания')
            item_5 = types.KeyboardButton('Сказка об умном мышонке')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, item_5, back)

            bot.send_message(message.chat.id,'Сказки для самых маленьких'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Короткие сказки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Курочка ряба')
            item_2 = types.KeyboardButton('Лев и Собачка')
            item_3 = types.KeyboardButton('Котёнок')
            item_4 = types.KeyboardButton('Огурцы')
            item_5 = types.KeyboardButton('Три котёнка')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, item_5, back)

            bot.send_message(message.chat.id,'Короткие сказки'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Сказки в стихах':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Мойдодыр')
            item_2 = types.KeyboardButton('Федорино горе')
            item_3 = types.KeyboardButton('Вот какой рассеянный')
            item_4 = types.KeyboardButton('Тихая сказка')
            back = types.KeyboardButton('Назад')
            markup.add(item_1,item_2, item_3, item_4, back)

            bot.send_message(message.chat.id, 'Сказки в стихах'.format(message.from_user), reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Русские народные')
            item_2 = types.KeyboardButton('Волшебные сказки')
            item_3 = types.KeyboardButton('Сказки о животных')
            item_4 = types.KeyboardButton('Сказки для самых маленьких')
            item_5 = types.KeyboardButton('Короткие сказки ')
            item_6 = types.KeyboardButton('Сказки в стихах')
            markup.add(item_1, item_2, item_3, item_4, item_5, item_6)

            bot.send_message(message.chat.id,'Вы вернулись в главное меню'.format(message.from_user), reply_markup=markup)
        elif message.text == 'Маша и медведь':
            bot.send_message(message.chat.id, parser(URL_MASHA_I_MEDVED))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Теремок':
            bot.send_message(message.chat.id, parser(URL_TEREMOK))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Колобок':
            bot.send_message(message.chat.id, parser(URL_KOLOBOK))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Репка':
            bot.send_message(message.chat.id, parser(URL_REPKA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Каша из топора':
            bot.send_message(message.chat.id, parser(URL_KASHA_IZ_TOPORA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')


        elif message.text == 'Гуси Лебеди':
            bot.send_message(message.chat.id, parser(URL_GUSI_LEBEDI))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Крошечка-Хаврошечка':
            bot.send_message(message.chat.id, parser(URL_KROSHECHKA_HAVROSHECHKA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Правда и Кривда':
            bot.send_message(message.chat.id, parser(URL_PRAVDA_I_KRIVDA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Три Брата':
            bot.send_message(message.chat.id, parser(URL_TRI_BRATA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Солдат и чёрт':
            bot.send_message(message.chat.id, parser(URL_SOLDAT_I_CHERT))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')


        elif message.text == 'Три Медведя':
            bot.send_message(message.chat.id, parser(URL_TRI_MEDVEDYA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Живая шляпа':
            bot.send_message(message.chat.id, parser(URL_ZIVAYA_SHLYAPA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Ёж':
            bot.send_message(message.chat.id, parser(URL_EZ))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Лисичкин хлеб':
            bot.send_message(message.chat.id, parser(URL_LISICHKIN_HLEB))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Волк и семеро козлят':
            bot.send_message(message.chat.id, parser(URL_VOLK_I_SEMERO_KOZLYAT))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')


        elif message.text == 'Дочка пекаря':
            bot.send_message(message.chat.id, parser(URL_DOCHGKA_PEKARYA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'У страха глаза велики':
            bot.send_message(message.chat.id, parser(URL_U_STRAHA_GLAZA_VELIKI))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Сказка о глупом мышонке':
            bot.send_message(message.chat.id, parser(URL_O_MISHONKE))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Три желания':
            bot.send_message(message.chat.id, parser(URL_TRI_ZCHELANIYA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Сказка об умном мышонке':
            bot.send_message(message.chat.id, parser(URL_OB_UMNOM))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')


        elif message.text == 'Курочка ряба':
            bot.send_message(message.chat.id, parser(URL_KUROCHKA_RYABA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Лев и Собачка':
            bot.send_message(message.chat.id, parser(URL_LEV_I_SOBACHKA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Котёнок':
            bot.send_message(message.chat.id, parser(URL_KOTENOK))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Огурцы':
            bot.send_message(message.chat.id, parser(URL_OGURCI))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Три котёнка':
            bot.send_message(message.chat.id, parser(URL_TRI_COTENKA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')


        elif message.text == 'Мойдодыр':
            bot.send_message(message.chat.id, parser(URL_MOIDODIR))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Федорино горе':
            bot.send_message(message.chat.id, parser(URL_FEDORINO_GORE))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Вот какой рассеянный':
            bot.send_message(message.chat.id, parser(URL_VOT_KAKOI))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')

        elif message.text == 'Тихая сказка':
            bot.send_message(message.chat.id, parser(URL_TIHAYA_SKAZKA))
            bot.send_message(message.chat.id, 'Если хотите прочитать еще одну сказку используйте команду /menu')






bot.polling(none_stop=True)



