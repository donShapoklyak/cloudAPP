import telebot 
from telebot import types
import requests 
import sqlite3

key = "f2a40701e8ef05bfa364cde735b3435a"

token = "7544191388:AAGiXGETeEJ3tGbtpDmCeSy5RNnYWC8Gbsw"

bot = telebot.TeleBot(token)
def get_db_connection():
    conn = sqlite3.connect('my_database.db')
    return conn

def create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    chatid INTEGER NOT NULL,
    city TEXT
    )
    ''')
    connection.commit()
    connection.close()

create_table()
@bot.message_handler(commands=['start'])
def send_start(message):  
   bot.send_message(message.chat.id, "Привет, напиши свой город и я буду показывать погоду в твоем городе!")

@bot.message_handler(func=lambda message: True)
def get_weath(message):
    city = message.text 
    chat_id = message.chat.id 
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Users (chatid, city) VALUES (?, ?)', (chat_id, city))   
    connection.commit()
    connection.close()
    keyboard = telebot.types.InlineKeyboardMarkup()
    webAppTest = types.WebAppInfo("https://donshapoklyak.github.io/head/")
    one_butt = types.KeyboardButton(text="воспользоватся конструктором", web_app=webAppTest)
    keyboard.add(one_butt)
    bot.reply_to(message, "Запомнил! Давайте глянем погодку у вас сегодня. (город можно изменить /config)", reply_markup=keyboard)


bot.polling()
