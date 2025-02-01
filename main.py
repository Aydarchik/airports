import telebot
import sqlite3
conn = sqlite3.connect('example.db')
bot = telebot.TeleBot('7959406471:AAGpdv5jyH6OEH5tKoNJE-rUsQb-g_8pHS0')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать! Напишите команду "get_data_button" чтобы вывести данные.')
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'get_data':
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        for row in data:
            bot.send_message(call.message.chat.id, f'id: {row[0]}, name: {row[1]}')
@bot.message_handler(commands=['get_data_button'])
def get_data_button(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button = telebot.types.InlineKeyboardButton(text='Получить данные', callback_data='get_data')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Нажмите кнопку, чтобы вывести данные.', reply_markup=keyboard)
bot.polling()