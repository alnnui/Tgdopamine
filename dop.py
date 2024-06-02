import requests
import telebot
import time
import sqlite3
from telebot import types


bot = telebot.TeleBot('7172170151:AAEzKCdYnpViCiS0_F-3ESUt6zAa-VY18pE')


def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, last_name TEXT)''')
    conn.commit()
    conn.close()


def add_user(user_id, username, first_name, last_name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR IGNORE INTO users (id, username, first_name, last_name)
                      VALUES (?, ?, ?, ?)''', (user_id, username, first_name, last_name))
    conn.commit()
    conn.close()


@bot.message_handler(commands=['start'])
def start_message(message):
    user = message.from_user
    add_user(user.id, user.username, user.first_name, user.last_name)
    bot.send_message(message.chat.id, 'Привет, это Дофамин 🙂\n\nМы поможем найти подходящее именно вам (или вашему ребенку) внеклассное занятие в г.Астана 🤩\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях\n\n')


@bot.message_handler(commands=['brob'])
def brob_message(message):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT username, first_name, last_name FROM users''')
    users = cursor.fetchall()
    conn.close()

    if users:
        users_list = '\n'.join([f'{user[1]} {user[2]} (@{user[0]})' for user in users])
        bot.send_message(message.chat.id, f'Список пользователей:\n{users_list}')
    else:
        bot.send_message(message.chat.id, 'Нет пользователей.')

# Команда /sport
@bot.message_handler(commands=['sport'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽', callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)

    bot.send_message(message.chat.id, 'Выберите вид спорта:', reply_markup=markup)


if __name__ == '__main__':
    init_db()
    


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'move1':
        send_move1_message(callback.message.chat.id)
    elif callback.data == 'move9':
        send_move9_message(callback.message.chat.id)
    elif callback.data == 'move10':
        send_move10_message(callback.message.chat.id)
    elif callback.data == 'move11':
        send_move11_message(callback.message.chat.id)
    elif callback.data == 'move12':
        send_move12_message(callback.message.chat.id)
    elif callback.data == 'move13':
        send_move13_message(callback.message.chat.id)
    elif callback.data == 'move2':
        send_move2_message(callback.message.chat.id)
    elif callback.data == 'move3':
        send_move3_message(callback.message.chat.id)
    elif callback.data == 'move5':
        send_move5_message(callback.message.chat.id)
    elif callback.data == 'move6':
        send_move6_message(callback.message.chat.id)
    elif callback.data == 'move8':
        send_move8_message(callback.message.chat.id)
    elif callback.data == 'move14':
        send_move14_message(callback.message.chat.id)
    elif callback.data == 'move15':
        send_move15_message(callback.message.chat.id)
    elif callback.data == 'move16':
        send_move16_message(callback.message.chat.id)
    elif callback.data == 'move17':
        send_move17_message(callback.message.chat.id)
    elif callback.data == 'move18':
        send_move18_message(callback.message.chat.id)
    elif callback.data == 'move19':
        send_move19_message(callback.message.chat.id)
    elif callback.data == 'move20':
        send_move20_message(callback.message.chat.id)
    elif callback.data == 'move21':
        send_move21_message(callback.message.chat.id)
    elif callback.data == 'move22':
        send_move22_message(callback.message.chat.id)
    elif callback.data == 'move23':
        send_move23_message(callback.message.chat.id)
    elif callback.data == 'move24':
        send_move24_message(callback.message.chat.id)
    elif callback.data == 'move25':
        send_move25_message(callback.message.chat.id)
    elif callback.data == 'move26':
        send_move26_message(callback.message.chat.id)
    elif callback.data == 'move27':
        send_move27_message(callback.message.chat.id)
    elif callback.data == 'move28':
        send_move28_message(callback.message.chat.id)
    elif callback.data == 'move29':
        send_move29_message(callback.message.chat.id)
    elif callback.data == 'move30':
        send_move30_message(callback.message.chat.id)
    elif callback.data == 'move31':
        send_move31_message(callback.message.chat.id)
    elif callback.data == 'move32':
        send_move32_message(callback.message.chat.id)
    elif callback.data == 'move33':
        send_move33_message(callback.message.chat.id)
    elif callback.data == 'move34':
        send_move34_message(callback.message.chat.id)
    elif callback.data == 'move35':
        send_move35_message(callback.message.chat.id)
    elif callback.data == 'move36':
        send_move36_message(callback.message.chat.id)
    elif callback.data == 'move37':
        send_move37_message(callback.message.chat.id)
    elif callback.data == 'move38':
        send_move38_message(callback.message.chat.id)
    elif callback.data == 'move39':
        send_move39_message(callback.message.chat.id)
    elif callback.data == 'move40':
        send_move40_message(callback.message.chat.id)
    elif callback.data == 'move41':
        send_move41_message(callback.message.chat.id)
    elif callback.data == 'move42':
        send_move42_message(callback.message.chat.id)
    elif callback.data == 'move43':
        send_move43_message(callback.message.chat.id)
    elif callback.data == 'move44':
        send_move44_message(callback.message.chat.id)
    elif callback.data == 'move45':
        send_move45_message(callback.message.chat.id)
    elif callback.data == 'move46':
        send_move46_message(callback.message.chat.id)
    elif callback.data == 'move47':
        send_move47_message(callback.message.chat.id)
    elif callback.data == 'move48':
        send_move48_message(callback.message.chat.id)
    elif callback.data == 'move49':
        send_move49_message(callback.message.chat.id)
    elif callback.data == 'move50':
        send_move50_message(callback.message.chat.id)
    elif callback.data == 'move51':
        send_move51_message(callback.message.chat.id)
    elif callback.data == 'move52':
        send_move52_message(callback.message.chat.id)
    elif callback.data == 'move53':
        send_move53_message(callback.message.chat.id)
    elif callback.data == 'move54':
        send_move54_message(callback.message.chat.id)
    elif callback.data == 'move55':
        send_move55_message(callback.message.chat.id)
    elif callback.data == 'move56':
        send_move56_message(callback.message.chat.id)
    



def send_move1_message(chat_id):
    photo_url = "https://ekip-sport.ru/assets/images/resources/picture10680346611277131754.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбол, который также часто называют футболом за пределами Великобритании и ассоциативным футболом по всей Европе, представляет собой игру двух команд и одного мяча — футбола. В каждой команде 11 игроков, и, используя все части своего тела, кроме рук и кистей, они должны попытаться забить мяч в ворота другой команды.\n\nФутбол – командная игра. Вместе с единомышленниками развивается ловкость, повышается координация движений, постепенно уходит лишний вес и как следствие, улучшается настроение. Чтобы быть физически здоровым и крепким, целеустремленным и коммуникабельным, рекомендуется играть в футбол.\n\nДофамин поможет вам(либо вашему ребенку) начать профессиональную футбольную карьеру в футбольной команде в г.Астана')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn9 = types.InlineKeyboardButton('Вперед!', callback_data='move9')
    markup.row(btn9)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move9_message(chat_id):

    photo_url = "https://avatars.mds.yandex.net/get-altay/12813969/2a0000018e03bb18f69f65f2ff29300f0991/XXL_height"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбольный клуб "FC Union"\nОбъявляет набор детей\n\n-возраст от 5-15 лет\n\nНаши преимущества:\n\n-профессиональные тренера\n\n-предоставляем форму\n\n-помимо тренировок мы даём возможность участвовать в соревнованиях, турнирах.\n\n- ваши дети почувствуют себя настоящими футболистами\n\n-тренировки проходят в интересной игровой форме\n\n-индивидуальный подход к каждому ребёнку\n\n-благоприятная атмосфера учит ваших детей работать в команде\n\n-первая тренировка бесплатно\n\nЗапись по номеру\n8-778-132-17-00\n\nМестоположение тренировочного поля\nПушкина 35/1\nDostyk Arena')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn10 = types.InlineKeyboardButton('Далее', callback_data='move10')
    markup.row(btn10)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move10_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRO3ltlaWiuLmcJRRewpjQy7GUmQE0VC_MYj87_fc8m3g&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбольный Центр "Тұмар"\n\nГруппы от 6 до 16 лет\n\nГруппа девочек от 10 лет и старше\n\nАдаптивная группа\n\nЛьготные скидки\n\nInstagram: fc.tumar \n\nWhatsApp: +7 702 850 8881')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn11 = types.InlineKeyboardButton('Далее', callback_data='move11')
    markup.row(btn11)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move11_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRUA38EGQKFCXtPfWNtUIjjgTMlDofu6DwVbE-TrI30Q&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбольный клуб “Royal”\n\nот 5 до 15лет\n\nПробное занятие БЕСПЛАТНО ®️ \n\nПодробнее:\n\n8-747-788-80-23\n\nНаши филиалы :\n\nОйтоган 14 (р-н парк Жеруйык )\n\nНациональная Академия (р-н Экспо)\n\n77 школа (р-н ГенПрокуратура)\n\nШ.Айманова 24 (р-н Шапагат)\n\nКарасаз 3 (р-н Хазрет Султан)')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn12 = types.InlineKeyboardButton('Далее', callback_data='move12')
    markup.row(btn12)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move12_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-Jh5Axo7aBsaFd1MYe-5Ucdkt856Gf_k3EtQXELaePg&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбольный Клуб “Elita”\n\nДетская футбольная школа\n\nГотовим к большому футболу\n\nИндивидуальные тренировки\n\nНабор с 6 до 16 лет\n\nInstagram: fc_elita.kz\n\nWhatsApp: +7 747 415 9598')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn13 = types.InlineKeyboardButton('Далее', callback_data='move13')
    markup.row(btn13)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move13_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYJwbfDJdOfpGewLG6_6tzzBItCRbHSmTk6TpD-EhcGA&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption='Футбольный клуб “Sparta”\n\nНабор детей 5 -12 лет\n\nИндивидуальный подход каждому ребёнку\n\nОпытные тренеры\n\nРастим будущих чемпионов\n\nПробная тренировка бесплатная\n\nInstagram: mfc.sparta\n\nWhatsApp: +7 747 732 2839 ')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!)')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')

def send_move2_message(chat_id):
    photo_url = "https://www.medved-sport.ru/upload/medialibrary/bdd/istlovo7l4hs3n72gw8jww51u2t53mmb.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= 'Бокс - это вид единоборства, в котором два участника сражаются друг с другом, используя только кулаки, защищенные перчатками.\n\nЭтот спортивный вид требует от участников высокой физической подготовки, силы, выносливости, координации и скорости.\n\nДля ребенка занятия боксом могут иметь несколько положительных аспектов.\n\nВо-первых, бокс способствует развитию физических качеств, таких как выносливость, сила, гибкость и скорость, что полезно для общего здоровья и физической формы ребенка.\n\nКроме того, бокс тренирует дисциплину, самоконтроль и уважение к тренеру и партнеру по тренировкам. Этот вид спорта также способствует развитию уверенности в себе, умения принимать решения и стратегического мышления.\n\nВ целом, занятия боксом могут помочь ребенку развиться как физически, так и морально.\n\nДофамин поможет вам найти секции по боксу в г.Астана')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn14 = types.InlineKeyboardButton('Вперед!', callback_data='move14')
    markup.row(btn14)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move14_message(chat_id):
    photo_url = "https://static.tildacdn.com/tild6336-6339-4932-b032-336230316466/0K9A9085.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Bronx Astana boxing club>\n\nАдрес: Улица Достык, 18\n\n Улица Касым Аманжолов, 28\n\n Улица Алихан Бокейхан,38\n\nПодробнее: https://www.instagram.com/bronxastana \n\nНомер телефона:+7(707)-130-88-88')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn15 = types.InlineKeyboardButton('Далее', callback_data='move15')
    markup.row(btn15)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move15_message(chat_id):
    photo_url = "https://lh6.googleusercontent.com/proxy/bE6wxzzqausnl_7WrVRIaqOXeg4pm5ENvMZJpzCTRl2i1D2bV_I_061GfIQD99RKxIVM-bdrBLO3SAfo0cdDmTyju0Pm8cTFk0cYdco--mP8AkVd5EG6MeQOsITANQ"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Astana Boxing club >\n\nАдрес: Улица Кордай, 21\n\nПодробнее: https://www.instagram.com/astana_boxing_club \n\nНомер телефона:+7(701)-762-00-05')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn16 = types.InlineKeyboardButton('Далее', callback_data='move16')
    markup.row(btn16)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move16_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR3Fa2bjwKTi69WGUchEtk96iK36KeD-pSgkzUTB03BA&s "
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<King Kong>\n\nАдрес: Улица Санжара Асфендиярова, 6\n\nУлица Калибек Куанышбаев, 11 \n\nПодробнее: https://www.instagram.com/kingkong_premium ')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn17 = types.InlineKeyboardButton('Далее', callback_data='move17')
    markup.row(btn17)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move17_message(chat_id):
    photo_url = "https://avatars.mds.yandex.net/get-altay/10926933/2a0000018bd288c2f6ab7d6b27ec05e7041f/L_height"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Alash Boxing club>\n\nАдрес: Проспект Туран, 40/2\n\nПодробнее: https://www.instagram.com/alash_box \n\nНомер телефона:+7(702)-733-09-90')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn18 = types.InlineKeyboardButton('Далее', callback_data='move18')
    markup.row(btn18)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move18_message(chat_id):
    photo_url = "https://avatars.mds.yandex.net/get-altay/224414/2a00000185787adc44d69a6acac2ed5eb2bc/L_height"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Kamal boxing>\n\nАдрес: Улица Сауран, 10в\n\n Улица Кайым Мухамедханов, 17\n\nПодробнее: https://www.instagram.com/kamal.boxing \n\nНомер телефона: +7(778)-010-10-39')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')

def send_move3_message(chat_id):
    photo_url = "https://www.nure.info/uploads/posts/2017-06/1498289800_sportivnyy-klub-sportivnye-sekcii-v-hnure-sekciya-basketbol.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= 'Баскетбол - это командный вид спорта, в котором две команды пытаются забросить мяч в корзину соперника, находясь на площадке, разделенной на две части.\n\nДля школьника или подростка занятия баскетболом также имеют множество позитивных сторон.\n\nВо-первых, это помогает улучшить физическую форму, развить выносливость, скорость, гибкость и координацию движений. Баскетбол способствует развитию командного духа, умения работать в коллективе и эффективно взаимодействовать с партнерами на площадке. Этот вид спорта также учит дисциплине, самоконтролю и управлению эмоциями в стрессовых ситуациях. Баскетбол помогает развить такие качества, как стратегическое мышление, принятие решений и аналитические способности.\n\nДофамин поможет вам найти подходящую секцию баскетбола в г.Астана')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn19 = types.InlineKeyboardButton('Вперед!', callback_data='move19')
    markup.row(btn19)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move19_message(chat_id):
    photo_url = "https://athlet.kz/images/logo_og.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Steppe Dunk>\n\nАдрес: Улица Сауран, 11\n\n Улица Толе би, 42 \n\n Улица Туркистан,2/1\n\n Улица Алихан Бокейхан, 34\n\n еще 10 адресов…\n\nПодробнее: https://www.instagram.com/steppe.dunk \n\nНомер телефона: +7(707)-563-95-27')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn20 = types.InlineKeyboardButton('Далее', callback_data='move20')
    markup.row(btn20)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move20_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8kmtwd825xnzatz_UXL-66JQDzuW4aRfIt5RPmzmvgg&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<All Basket>\n\nАдрес: Улица Халел Досмухамедулы, 14\n\nПодробнее: https://www.instagram.com/allbasket.ball \n\nНомер телефона: +(707)-684-96-88')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')


def send_move5_message(chat_id):
    photo_url = "https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_xl_2x/f_auto/primary/ibpokfosda2aubwn30tz"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= 'Дзюдо - это японское боевое искусство, которое выделяется своей уникальной философией и методами тренировки. Основной принцип дзюдо - использование технических приемов и бросков для подавления противника, а не применение силы напрямую. Ученики дзюдо развивают физическую силу, гибкость, координацию движений и тактическое мышление. Это искусство способствует формированию дисциплинированности, уважения к сопернику и самодисциплины. Практика дзюдо также способствует улучшению здоровья, развитию мышц и костной системы.\n\nДля школьников и подростков занятия дзюдо могут быть особенно полезными. Они помогают детям развить физическую активность, улучшить координацию движений и гибкость. Дзюдо также способствует развитию самодисциплины, контролю над собой и уважению к другим.\n\nУчитывая, что дзюдо не требует специального оборудования и может быть практиковано в любом возрасте, это отличный спортивный выбор для детей и подростков.\n\nДофамин поможет вам найти подходящие секции дзюдо в г.Астана')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn21 = types.InlineKeyboardButton('Вперед!', callback_data='move21')
    markup.row(btn21)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move21_message(chat_id):
    photo_url = "https://static.tildacdn.pro/tild3338-3331-4435-a139-626264386136/_.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<SANA Sport>\n\nАдрес:Улица Кажымукан, 5\n\nПодробнее: https://www.instagram.com/sanasportkz \n\nНомер телефона:+7(747)-094-72-11\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn22 = types.InlineKeyboardButton('Далее', callback_data='move22')
    markup.row(btn22)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move22_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrtbG5wYsFsU4_AwtmB5C4avBnteez-IuAn7Q_ptzaDA&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Орда дзюдо>\n\nАдрес:Улица Айтеке би, 16\n\nУлица Габит Мусрепов, 4/2\n\nПодробнее: https://www.instagram.com/judo_orda\n\nНомер телефона:+7(701)-524-03-24\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn23 = types.InlineKeyboardButton('Далее', callback_data='move23')
    markup.row(btn23)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move23_message(chat_id):
    photo_url = "https://yt3.googleusercontent.com/ytc/AIdro_lN8GRICYL8wUIt2p421bT7we6LmCq1Kk60V_j07MFafw=s900-c-k-c0x00ffffff-no-rj"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Ortus.kz>\n\nАдрес:VIP-городок, 1/1\n\nПроспект Кабанбай Батыр, 43\n\nУлица Чингиз Айтматов, 36\n\nПодробнее: https://www.instagram.com/ortus.kz\n\nНомер телефона:+7(708)-931-16-92 ')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn24 = types.InlineKeyboardButton('Далее', callback_data='move24')
    markup.row(btn24)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move24_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdJ8jTOh2UPQc1Q1AkxfVYRFyVoN-Op5YCrIBY7vaMTA&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<KazTuran Sport>\n\nАдрес:Проспект Сарыарка, 33/1\n\nПодробнее: https://www.instagram.com/kazturan_sport\n\nНомер телефона:+7(747)-673-73-90')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn25 = types.InlineKeyboardButton('Далее', callback_data='move25')
    markup.row(btn25)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move25_message(chat_id):
    photo_url = "https://avatars.mds.yandex.net/get-altay/7742431/2a000001846c38fa2634ea231841ca5ebd33/orig"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Qazaq Batyry>\n\nАдрес:Проспект Мангилик ел, 17а\n\n Улица Туркистан, 34а\n\n Улица Алексея Петрова, 28\n\nПодробнее: https://www.instagram.com/qazaqbatyryacademy\n\nНомер телефона: +7(707)-521-55-56')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')

def send_move6_message(chat_id):
    photo_url = "https://orda.kz/uploads/sites/2/2022/02/detail_dd4f6717751e82ae04f16080e2a7b9c3-1440x810.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= 'Шахматы - это стратегическая настольная игра, в которой два игрока соревнуются на доске размером 8х8 клеток. Цель игры - объявить шах и мат королю противника, либо добиться патовой ситуации.\n\nШахматы развивают логическое мышление, стратегическое мышление, умение принимать решения и предвидеть ходы соперника. Это игра, которая требует терпения, концентрации и умения планировать несколько шагов вперед.\n\nДля школьников занятия шахматами также могут быть очень полезными.\n\nОни помогают развить аналитические способности, улучшить память и концентрацию внимания.\n\nШахматы также способствуют формированию стратегического мышления, умению анализировать ситуацию и принимать решения в условиях ограниченного времени.\n\nКроме того, шахматы способствуют развитию терпения, уважения к сопернику и способности к сотрудничеству.\n\nДофамин поможет вам найти секции шахмат в г.Астана')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn26 = types.InlineKeyboardButton('Вперед!', callback_data='move26')
    markup.row(btn26)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move26_message(chat_id):
    photo_url = "https://avatars.mds.yandex.net/get-altay/10216747/2a0000018a031309267413f1a11f6bde0b50/L_height"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Академия шахмат “GMCA”>\n\nАдрес: Улица Айтеке би, 15\n\n Улица Улы-Дала, 65/2\n\n Улица Толе би, 42\n\nПодробнее: https://www.instagram.com/gmca.kz/ \n\nНомер телефона:+7(771)-231-45-49\n +7(702)-728-37-11\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn27 = types.InlineKeyboardButton('Далее', callback_data='move27')
    markup.row(btn27)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move27_message(chat_id):
    photo_url = "https://dknews.kz/storage/news/2022-08/wDodSaco8L2eduZmC9QmF5mcrZCDxaL9Mk6jNndg.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Академия шахмат Динары Садуакасовой>\n\nАдрес:Улица Сауран, 9 \n\nПроспект Тауелсиздик, 57\n\nУлица Ахмета Байтурсынулы, 14n\nНомер телефона:+7(700)-541-51-51\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn28 = types.InlineKeyboardButton('Далее', callback_data='move28')
    markup.row(btn28)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move28_message(chat_id):
    photo_url = "https://chess-astana.kz/assets/images/logo-main.png"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Ход конём>\n\nАдрес:Улица Сауран, 1\n\nУлица Габит Мусрепов, 6\n\nПроспект Улы Дала, 65/1\n\nПроспект Ракымжан Кошкарбаев, 40/1\n\n Проспект Сарыарка, 17\n\n Улица Бейбитшилик, 25\n\nПроспект Богенбай Батыра, 56а\n\n Улица Бегазы-Данбыбай, 31/1\n\nПодробнее: https://www.instagram.com/schoolhodkonem \n\nНомер телефона:+7(700)-836-81-84\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn29 = types.InlineKeyboardButton('Далее', callback_data='move29')
    markup.row(btn29)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move29_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJDw1X2v1bMJUgcafUGhT8WZ0FESZCFO9UjaGWTdNaOw&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<SANA Jana Urpaq Ortalygy>\n\nАдрес:Проспект Туран,34в\n\nПодробнее: https://www.instagram.com/sanabilim.kz\n\nНомер телефона: :+7(708)-010-77-88\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn30 = types.InlineKeyboardButton('Далее', callback_data='move30')
    markup.row(btn30)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move30_message(chat_id):
    photo_url = "https://baigenews.kz/storage/storage/news/2023/01/20/mainphoto/116715/1200xauto_F6h1EzrEbeUFxbYKI8jH9mkNLuFjWuPPAdjz0g7d.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Будущие миллионеры>\n\nАдрес:Проспект Ракымжан Кошкарбаев, 34\n\n Улица Алихан Бокейхан, 10\n\n Улица ахмет Байтурсынулы, 49а\n\n Улица Шафика Чокина, 5\n\n Проспект Туран, 4/2\n\n Аль-Фараби проспект, 40а\n\n VIP-городок,22а\n\n Аль-Фараби проспект,9/5\n\nПодробнее: https://www.instagram.com/chessleader_school \n\nНомер телефона:+7(747)-467-23-12\n\n')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')

def send_move8_message(chat_id):
    photo_url = "https://img.olympics.com/images/image/private/t_s_pog_staticContent_hero_xl_2x/f_auto/primary/rc3qie4h9qbf87c0sl6g"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= 'Гимнастика - это вид спорта, который включает в себя различные упражнения, направленные на развитие гибкости, силы, координации и выносливости. Она может быть представлена в различных форматах, включая художественную гимнастику, спортивную гимнастику, акробатику, ритмическую гимнастику и другие.\n\nГимнастика помогает улучшить физическую форму, развивает мышечный корсет, повышает гибкость и координацию движений.\n\nДля школьников занятия гимнастикой могут быть очень полезными. Они способствуют укреплению мышц, улучшению осанки, развитию координации движений и гибкости.\n\nГимнастика также помогает улучшить дисциплину, выражать эмоции через движение и повышает самооценку.\n\nКроме того, занятия гимнастикой способствуют формированию уверенности в себе, сосредотачивают внимание и помогают расслабиться после учебы или стрессовых ситуаций.')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn31 = types.InlineKeyboardButton('Вперед!', callback_data='move31')
    markup.row(btn31)
    bot.send_message(chat_id, 'Хотите начать?', reply_markup=markup)

def send_move31_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv7zy_ixqXFdY9IFfqsirUHM8866Ex0vwmWGKm4465Nw&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Izumrud>\n\nАдрес: 219-переулок, 12\n\n Велотрек Сарыарка \n\n Проспект Мангилик ел, 17а\n\n Шоссе Коргалжын, 2\n\n еще 14 адресов… \n\nПодробнее: https://www.instagram.com/izumrud_gymnastics_astana/ \n\nНомер телефона: +7(700)-355-88-68')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn32 = types.InlineKeyboardButton('Далее', callback_data='move32')
    markup.row(btn32)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move32_message(chat_id):
    photo_url = "https://avatars.mds.yandex.net/get-altay/1583613/2a0000016f94296aeccbd8b53269e9dd2294/L_height"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<DreamWay Dance&Art Lab>\n\nАдрес: Проспект Ракымжан Кошкарбаев,2 С3 блок\n\nПодробнее: https://www.instagram.com/dreamway.dc \n\nНомер телефона:+7(775)-380-31-41')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn33 = types.InlineKeyboardButton('Далее', callback_data='move33')
    markup.row(btn33)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move33_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQczGjDqIfC3TB6iBwMR-mUX1wzoX7sHT534ozFduJWnQ&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Cool Space>\n\nАдрес: Проспект Ракымжан Кошкарбаев, 10Е 2-5 блок\n\nПодробнее: https://www.instagram.com/coolspace_ds \n\nНомер телефона: +7(747)-722-92-22')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn34 = types.InlineKeyboardButton('Далее', callback_data='move34')
    markup.row(btn34)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move34_message(chat_id):
    photo_url = "https://static.tildacdn.pro/tild3638-3433-4333-a435-376166343634/__.png"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Sana Jana Urpaq Ortalygy>\n\nАдрес: Проспект Туран,34в\n\nПодробнее: https://www.instagram.com/sanabilim.kz \n\nНомер телефона: +7(708)-010-77-88')
    time.sleep(3)
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Футбол ⚽',callback_data='move1')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Бокс 🥊', callback_data='move2')
    markup.row(btn2)
    btn3 = types.InlineKeyboardButton('Баскетбол 🏀', callback_data='move3')
    markup.row(btn3)
    btn5 = types.InlineKeyboardButton('Дзюдо 🥋', callback_data='move5')
    markup.row(btn5)
    btn6 = types.InlineKeyboardButton('Шахматы ♟️', callback_data='move6')
    markup.row(btn6)
    btn8 = types.InlineKeyboardButton('Гимнастика 🤸', callback_data='move8')
    markup.row(btn8)
    
    bot.send_message(chat_id, 'Предлагаем вам поискать другие виды спорта:', reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')

@bot.message_handler(commands=['tutor'])
def prodolzhit(message):
    markup = types.InlineKeyboardMarkup()
    btn35 = types.InlineKeyboardButton('Английский язык',callback_data='move35')
    markup.row(btn35)
    btn36 = types.InlineKeyboardButton('Математика',callback_data='move36')
    markup.row(btn36)
    btn37 = types.InlineKeyboardButton('Физика',callback_data='move37')
    markup.row(btn37)

    bot.send_message(message.chat.id, 'Выберите предмет:', reply_markup=markup)

def send_move35_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/d3w5qaevqr6g-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Zhapbaraly Aisha >\n\nРепетитор английского языка \n\nАдрес: Мухамедханова 12 \n\n Возраст 16+\n\n Подготовка к IELTS\n\nНомер телефона: :+7(707)-908-29-73\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn38 = types.InlineKeyboardButton('Далее', callback_data='move38')
    markup.row(btn38)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move38_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/l0qkbud0223r3-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Nurila >\n\nРепетитор английского языка \n\nАдрес: Алматинский район\n\n Возраст без ограничений \n\nНомер телефона: :+7(776)-876-73-77\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn39 = types.InlineKeyboardButton('Далее', callback_data='move39')
    markup.row(btn39)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move39_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/d4y2vi1v7yvh2-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Damesh >\n\nРепетитор английского языка \n\nПодготовка к IELTS\n\nАдрес: Есильский район\n\n Возраст  от 15 лет\n\nНомер телефона: :+7(705)-671-42-77\n\n')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn35 = types.InlineKeyboardButton('Английский язык',callback_data='move35')
    markup.row(btn35)
    btn36 = types.InlineKeyboardButton('Математика',callback_data='move36')
    markup.row(btn36)
    btn37 = types.InlineKeyboardButton('Физика',callback_data='move37')
    markup.row(btn37)
    
    bot.send_message(chat_id, 'Предлагаем обратить внимание и на другие предметы):',reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях\n\n')
    
def send_move36_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/jx37t4ffw9222-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Диас>\n\nРепетитор по математике\n\nАдрес: Есильский район \n\n Возраст  без ограничений\n\n Подготовка к Экзаменам НИШ, РФМШ, КТЛ, SAT, ЕНТ\n\nНомер телефона: :+7(747)-808-59-27\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn40 = types.InlineKeyboardButton('Далее', callback_data='move40')
    markup.row(btn40)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move40_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/yg4z5yl8pn1s3-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Sayat>\n\nРепетитор по математике\n\nАдрес: Алматинский район\n\n Возраст  6-18 лет\n\n Подготовка к Экзаменам НИШ , КТЛ, ЕНТ\n\nНомер телефона: :+7(707)-674-36-58\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn41 = types.InlineKeyboardButton('Далее', callback_data='move41')
    markup.row(btn41)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move41_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/lls1q6ntqm9j2-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Korganbekov Toktar>\n\nРепетитор по математике\n\nАдрес: Есильский район \n\n Возраст  от 11-13 лет\n\n Подготовка к Экзаменам НИШ, РФМШ, КТЛ\n\nНомер телефона: :+7(771)-012-60-20\n\n')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn35 = types.InlineKeyboardButton('Английский язык',callback_data='move35')
    markup.row(btn35)
    btn36 = types.InlineKeyboardButton('Математика',callback_data='move36')
    markup.row(btn36)
    btn37 = types.InlineKeyboardButton('Физика',callback_data='move37')
    markup.row(btn37)
    
    bot.send_message(chat_id, 'Предлагаем обратить внимание и на другие предметы):',reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях\n\n')
    

def send_move37_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/5vzp8sxj9xk31-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Даулет>\n\nРепетитор по физике \n\nОнлайн\n\n Возраст  без ограничений\n\n Подготовка к олимпиадам\n\nНомер телефона: :+7(747)-559-10-36\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn42 = types.InlineKeyboardButton('Далее', callback_data='move42')
    markup.row(btn42)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move42_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/1imdsylkm7xe-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Гульмира>\n\nРепетитор по физике \n\nАдрес: Қабанбай Батыр 39\n\n 5-19 лет\n\n Подготовка к олимпиадам, решения СОР СОЧ, Поступление в Казахстанские и Российские Вузы\n\nНомер телефона: :+7(707)-904-69-32\n\n')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn43 = types.InlineKeyboardButton('Далее', callback_data='move43')
    markup.row(btn43)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)

def send_move43_message(chat_id):
    photo_url = "https://frankfurt.apollo.olxcdn.com/v1/files/3kao7qj8jg65-KZ/image;s=1000x700"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '< Арысланов Алихан>\n\nРепетитор по физике \n\nАдрес: Қабанбай Батыр 53\n\n 5-19 лет\n\n Подготовка к экзаменам , Поступление в Вузы\n\nНомер телефона: :+7(771)-429-64-84\n\n')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(2)
    markup = types.InlineKeyboardMarkup()
    btn35 = types.InlineKeyboardButton('Английский язык',callback_data='move35')
    markup.row(btn35)
    btn36 = types.InlineKeyboardButton('Математика',callback_data='move36')
    markup.row(btn36)
    btn37 = types.InlineKeyboardButton('Физика',callback_data='move37')
    markup.row(btn37)
    
    bot.send_message(chat_id, 'Предлагаем обратить внимание и на другие предметы):',reply_markup=markup)
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях\n\n')
    

@bot.message_handler(commands=['university'])
def prodolzhit1(message):
    markup = types.InlineKeyboardMarkup()
    btn44 = types.InlineKeyboardButton('Погнали!',callback_data='move44')
    markup.row(btn44)
   

    bot.send_message(message.chat.id, 'Хотите ли вы поступить в университет мечты😍?', reply_markup=markup)

def send_move44_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMJBAY5BHGxjz6hWxOkGb7dUTTqcxF1MMFIRT9qrDstA&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<GC education>\n\nПодробнее: @gc_eduteam за годы работы обеспечил 100-процентный результат поступления!\n\nНаши студенты уже учатся в: Stanford, KAIST, NYUAD, UofT, PolyU, University of British Columbia, CITY U, HKUST и многие другие.\n\nБез потери времени и лишнего стресса мы поможем тебе на каждом шагу поступления 💛\n\nМы — это не просто помощь с эссе и документами, наши менторы буду рядом на всем пути поступления!')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn45 = types.InlineKeyboardButton('Далее', callback_data='move45')
    markup.row(btn45)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move45_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5oQc_DqzSUbzkXU9LtmTKX1y5drMug6ti_-Agp96Llw&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Generation Centre>\n\nАдрес: Улица Сауран, 1\n\nПодробнее: Добро пожаловать в наш образовательный центр! Мы с гордостью представляем себя на рынке с 2017 года. Наш опыт и энтузиазм помогают нашим студентам успешно справиться с экзаменами IELTS и SAT, достигая высоких баллов. Наши профессиональные учителя, с опытом работы от 5 лет и выше, гарантируют эффективное обучение.\n\nВысокие баллы на экзаменах открывают двери в лучшие учебные заведения мира. Наши студенты поступают в престижные университеты в США, Малайзии, Италии, Великобритании и других странах. Мы предоставляем полную поддержку на каждом этапе поступления, начиная с подготовки документов и заканчивая успешным зачислением.\n\nПрисоединяйтесь к нам, чтобы осуществить вашу мечту об образовании за рубежом!')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn46 = types.InlineKeyboardButton('Далее', callback_data='move46')
    markup.row(btn46)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move46_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkVDKzhzVRv5J48gLorDz_nY-ffvXq_K49Rsz3wK6m6g&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Tumar Academy>\n\nПодробнее: 🌱Онлайн консультаци по поступлению в НУ\n\n🌱100+ студентов с IELTS 7.0 и NUET 150 \n\n🌱поддержка учеников с регионов/многодетных/малоимущих семей\n\n https://www.instagram.com/tumar.academy/')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn47 = types.InlineKeyboardButton('Далее', callback_data='move47')
    markup.row(btn47)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move47_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqGRHpZgzWNtdYnHJ_f9c2yGeRpRHnOmE80rc2cP7P6g&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Talan>\n\nАдрес:Vip-городок, 7\n\nУлица Динмухамед Конаева, 33\n\nПроспект Республика,34а\n\nПодробнее: https://www.instagram.com/talan.edu.kz/\n\nНомер телефона:+7(707)-940-90-55 ')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях\n\n')
    

@bot.message_handler(commands=['school'])
def prodolzhit2(message):
    markup = types.InlineKeyboardMarkup()
    btn48 = types.InlineKeyboardButton('Погнали!',callback_data='move48')
    markup.row(btn48)
   

    bot.send_message(message.chat.id, 'Хотите ли вы поступить в школу мечты😍?', reply_markup=markup)
    

def send_move48_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3xX2zc7_6PGDE52dqJK5sY0gVAI31aSZzM17MgptAqQ&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Aiplus>\n\nЦентр подготовки к экзаменам НИШ, КТЛ, РФМШ\n\nДо 12 учеников в группе\n\nОт  12  до  14 лет\n\nТренеры прошедшие трехэтапный отбор и с опытом преподавания от 3 лет\n\nЛьготные скидки\n\nInstagram:  iplus.kz\n\nНомер +7 700 836 9833')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn49 = types.InlineKeyboardButton('Далее', callback_data='move49')
    markup.row(btn49)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move49_message(chat_id):
    photo_url = "https://cdn.obyavleniya.kaspi.kz/webp/40/4015f4a9-ef70-4016-9b72-b660a9ee0779/4-full.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Zerdeli>\n\nЦентр подготовки экзаменам НИШ, КТЛ, РФМШ, ЕНТ, NUFYPET, SAT\n\nОт 7 до 19 лет\n\nАдаптивная группа\n\nInstagram: zerdeli.kz\n\nНомер +7 776 109 11 11')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn50 = types.InlineKeyboardButton('Далее', callback_data='move50')
    markup.row(btn50)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move50_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtpIgR4kZvLfq0BBFEyLV34VqLYOS8Fw_3pyxvF6mNiw&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<INTELLECT>\n\nВ основном поступление в НИШ\n\nПодготовка ко всем предметам\n\nОт 5 до 19 лет\n\nАдаптивная группа\n\nНомер +7 705 447 3644\n\nInstagram:  @fiz_mat_intellect')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn51 = types.InlineKeyboardButton('Далее', callback_data='move51')
    markup.row(btn51)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move51_message(chat_id):
    photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcST88PECMwS1IHVE_LdhQJbE_m4kelrLkdTpbGrtfZoJw&s"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Tesla Education>\n\nОбщая подготовка\n\nПоступление в НИШ КТЛ РФМШ\n\nОт 4 до 19 лет\n\nАдаптивная группа\n\nНомер +7 707 77 13 113\n\nInstagram: tesla.education')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn52 = types.InlineKeyboardButton('Далее', callback_data='move52')
    markup.row(btn52)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move52_message(chat_id):
    photo_url = "https://b2b.ivest.kz/downloads/bz/logo/20180622120808811.jpg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Mega Study Education>\n\nязыки: английский, корейский, казахский, русский, французский, турецкий, китайский\n\nматематика\n\nподготовка к магистратуре\n\nподготовка к IELTS.\n\nАдаптивная группа\n\nЛьготные скидки\n\nОт 5 до 19 лет\n\n8 705 518 47 42, 8 708 425 13 33\n\nInstagram: megastudy_astana')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/volunteering" если хотите заниматься волонтерством и состоять в волонтерских организациях')
    

@bot.message_handler(commands=['volunteering'])
def prodolzhit3(message):
    markup = types.InlineKeyboardMarkup()
    btn53 = types.InlineKeyboardButton('Да!Вперед!',callback_data='move53')
    markup.row(btn53)
   

    bot.send_message(message.chat.id, 'Хотите ли вы стать частью волонтерских организаций?', reply_markup=markup)   
    
def send_move53_message(chat_id):
    photo_url = "https://communicarehc.org/wp-content/uploads/2023/06/volunteer-image-5.png"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Umnie Detki>\n\n✨️ UMNIE DETKY ✨️\n\nДорогие друзья! Представляем вам наш волонтёрский проект "Umnie Detky" 📚🌟\n\n🌟 Цель этой инициативы - помочь детям с ограниченными возможностями получить качественное образование и развиваться в полной мере. Мы верим, что каждый ребёнок заслуживает яркого будущего, и мы можем сделать это вместе.\n\n💡 Проект "Umnie Detky" предоставляет возможность стать частью чего-то большего, подарив детям навыки и знания, необходимые для их успешного развития. Волонтёры этой инициативы вдохновляют и учат детей, помогая им раскрыть свой потенциал.\n\n🙋‍♀️ Присоединяйтесь к нам, и давайте вместе делать мир лучше!\n\nПодробнее: https://www.instagram.com/umnie_detky/')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn54 = types.InlineKeyboardButton('Далее', callback_data='move54')
    markup.row(btn54)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move54_message(chat_id):
    photo_url = "https://chance.su/uploads/posts/2023-04/1680733852_43_1510-e1671973203528-min.jpeg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Национальная Волонтерская Сеть>\n\nНеправительственная добровольная организация, целью которой является формирование, поддержка и развитие культуры волонтерства. Национальная волонтерская сеть реализует социальные, культурные, экологические, событийные проекты волонтерства. Поддержать организацию можно став волонтером и подав заявку на проект, в котором вы хотите принять участие. \n\n Подробнее: qazvolunteer.kz\n\nНомер телефона: +7(708)-706-42-42')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn55 = types.InlineKeyboardButton('Далее', callback_data='move55')
    markup.row(btn55)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move55_message(chat_id):
    photo_url = "https://www.snta.ru/upload/iblock/482/48253e68b713c6dd1d943302e52b31a5.jpeg"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<Благотворительный фонд “Истоки Добра”>\n\n Подробнее: Некоммерческий благотворительный фонд помощи пожилым людям, людям с ограниченными возможностями и малоимущим семьям. Фонд оказывает помощь в виде продуктов, горячих обедов, медикаментов, теплой одежды. Поддержать благотворительный фонд можно материально.')
    time.sleep(3)
    markup = types.InlineKeyboardMarkup()
    btn56 = types.InlineKeyboardButton('Далее', callback_data='move56')
    markup.row(btn56)
    bot.send_message(chat_id, 'Хотите продолжить поиск?', reply_markup=markup)
    
def send_move56_message(chat_id):
    photo_url = "https://i.work.ua/article/1031b.jpg?v=1713862772"
    photo = requests.get(photo_url)
    bot.send_photo(chat_id, photo.content, caption= '<New Wave>\n\n🌊NEW WAVE - это клуб по охране окружающей среды. \n\n🌊Основатели клуба - ученики Назарбаев интеллектуальной школы химико-биологического направления города Шымкент, которым не безразлично экологическое состояние нашей планеты.\n\nЧем мы занимаемся?\n\n🌐Мы организовываем различного рода мероприятия, разрабатыем проекты, направленные на улучшение экологии. \n\n🌐Наша цель - улучшить экологию города и призвать людей жить в гармонии с природой.\n\nПодробнее: https://www.instagram.com/newwave_ngo/')
    time.sleep(3)
    bot.send_message(chat_id, 'На этом пока что все:( Ожидайте еще больше информации и возможностей в дальнейшем!')
    time.sleep(1)
    bot.send_message(chat_id, 'Если же вы хотите поискать другое, то:\n\nНапишите команду "/sport" если вы искали спортивные секции для себя (или для своего ребенка)\n\nНапишите команду "/tutor" если вы (или ваш ребенок) хотите восполнить пробелы в учебе 📚\n\nНапишите команду "/university" если хотите поступить в топ 10 вузов мира 🤩\n\nНапишите команду "/school" если желаете поступить в топовые школы нашей страны(НИШ, БИЛ, РФМШ)')
    
@bot.message_handler(commands=['stop'])
def handle_stop(message):
    
    bot.reply_to(message, "Надеюсь Дофмаин помог вам. Спасибо вам за то что пользуетесь Дофамином❤️")
    
    bot.stop_bot()



    

    
    
    
bot.polling(none_stop=True)



    

    
    
