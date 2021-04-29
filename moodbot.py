import telebot
import config
import os

from telebot import types
from sqlighter import sqlighter
from chart import save
from randomly import RandomMoods as r_moods

BASE_DIR = str(os.path.dirname(os.path.abspath(__file__)))
bot = telebot.TeleBot(config.TOKEN)
db = sqlighter('db.db')


# проверка пользователя
@bot.message_handler(commands=['start'])
def new_user(message):
	db = sqlighter('db.db')
	if(not db.subscriber_exists(message.from_user.id)):
		bot.send_message(message.from_user.id, 'Привет, начинаем записывать твое настроение.\nНе забывай отмечать когда оно изменится! Для этого напиши комманду /mood\n Нужна помощь? Пиши /help')
		# если юзера нет в базе, добавляем его
		db.add_subscriber(message.from_user.id)
	else:
		# если он уже есть, то просто обновляем ему статус подписки
		bot.send_message(message.from_user.id, 'Привет, твое настроение уже считаем.\nНе забывай отмечать когда оно изменится! Для этого напиши комманду /mood\n Нужна помощь? Пиши /help')


@bot.message_handler(commands=['help'])
def help_message(message):
	bot.send_message(message.from_user.id, 'Все просто!\nКомманды:\n /mood - Вызывает меню работы с настроением.\n /dell - Удалить данные (в разработке)')


# создаем кнопки
@bot.message_handler(commands=['mood'])
def add_mood_data(message):
	makrup_Inline = types.InlineKeyboardMarkup()
	yes_bt = types.InlineKeyboardButton(text='ДОБАВИТЬ', callback_data='yes')
	no_bt = types.InlineKeyboardButton(text='ГРАФИК', callback_data='print')
	makrup_Inline.add(yes_bt, no_bt)
	bot.send_message(message.chat.id, 'Что хочешь сделать?',reply_markup=makrup_Inline)


# создаем кнопки под полем ввода
@bot.callback_query_handler(func=lambda call: True)
def count_mood(call):
	db = sqlighter('db.db')
	if call.data == 'yes':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
		happy_bt = types.KeyboardButton('Счастливый')
		unhappy_bt = types.KeyboardButton('Несчастный')
		marry_bt = types.KeyboardButton('Веселый')
		sorry_bt = types.KeyboardButton('Расстроенный')
		angry_bt = types.KeyboardButton('Злой')
		sad_bt = types.KeyboardButton('Грустный')
		cheerful_bt = types.KeyboardButton('Бодрый')
		high_spirited_bt = types.KeyboardButton('Энергичный')
		low_spirited_bt = types.KeyboardButton('Вялый')


		markup_reply.add(happy_bt, unhappy_bt, marry_bt, sorry_bt, angry_bt, sad_bt, cheerful_bt, high_spirited_bt, low_spirited_bt)
		bot.send_message(call.message.chat.id, 'Выбери настроение',reply_markup=markup_reply) # обращение к message в обработчике call
	elif call.data == 'print':
		bot.send_message(call.message.chat.id, 'График будет сейчас будет отправлен')
		save(call.message.chat.id)
		bot.send_photo(call.message.chat.id, open(f'{BASE_DIR}/img/{call.message.chat.id}.png','rb'))


# считаем настроение
@bot.message_handler(content_types = ['text'])
def mood_calc(message):
	db = sqlighter('db.db')
	if message.text == 'Счастливый':
		score = db.get_data(message.from_user.id)[0][2]
		score += 1
		mood_name = 'happy'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_positive())
	elif message.text == 'Несчастный':
		score = db.get_data(message.from_user.id)[0][3]
		score += 1
		mood_name = 'unhappy'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_negative())
	elif message.text == 'Веселый':
		score = db.get_data(message.from_user.id)[0][4]
		score += 1
		mood_name = 'marry'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_positive())
	elif message.text == 'Расстроенный':
		score = db.get_data(message.from_user.id)[0][5]
		score += 1
		mood_name = 'sorry'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_negative())
	elif message.text == 'Злой':
		score = db.get_data(message.from_user.id)[0][7]
		score += 1
		mood_name = 'angry'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_negative())
	elif message.text == 'Грустный':
		score = db.get_data(message.from_user.id)[0][8]
		score += 1
		mood_name = 'sad'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_negative())
	elif message.text == 'Бодрый':
		score = db.get_data(message.from_user.id)[0][9]
		score += 1
		mood_name = 'cheerful'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_positive())
	elif message.text == 'Энергичный':
		score = db.get_data(message.from_user.id)[0][10]
		score += 1
		mood_name = 'high_spirited'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_positive())
	elif message.text == 'Вялый':
		score = db.get_data(message.from_user.id)[0][-1]
		score += 1
		mood_name = 'low_spirited'
		db.mood_update(mood_name, score, message.from_user.id)
		bot.send_message(message.chat.id, r_moods.random_negative())


bot.polling(none_stop=True)