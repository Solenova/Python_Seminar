from multiprocessing import context
from turtle import update
from telegram import Update
from telegram.ext import  Updater, CommandHandler, ContextTypes, CallbackContext
import telebot
from bot_keyboard import*
from bot_log import*
import logging

logging.basicConfig(format='%(asctime)s -%(levelname)s-%(message)s',
                    level=logging.INFO,
                    filename='db.csv'
                 )
logger = logging.getLogger(__name__)
# logging.basicConfig('%(asctime)s-%(name)s-%(levelname)s-%(message)s', filename='db.csv', level=logging.INFO)

bot = telebot.TeleBot('5581927683:AAG-R1WyXA8B4RIL0OLviN056e5a2_PNbtM')

value=''
old_value=''

@bot.message_handler(commands=['start','calculater'])
def getMessage(message):
    global value
    logger.info('Входные данные: %s: %s', update.message.from_user.first_name, update.message.text)
    # logger.info('Started')
    if value=='':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else: 
        bot.send_message(message.from_user.id, value, reply_markup=keyboard)
    
  
@bot.callback_query_handler(func=lambda call:True)
def callback_func(query):
    # logging.info('Выходные данные: %s: %s', update.message.from_user, update.message.text)
    global value, old_value
    data=query.data

    if data=='no':
        pass
    elif data=='C':
        value=''
    elif data=='<=':
        if value!='':
            value=value[:len(value)-1]
    elif data=='=':
        try:
            value=str(eval(value))
        except:
            value='Ошибка!'
    else:
        value+=data
    if (value!=old_value and value!='') or ('0'!=old_value and value==''):
        if value=='':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, 
            text='0', reply_markup=keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
             text=value, reply_markup=keyboard)
    old_value=value
    if value=='Ошибка!': value=''
  

bot.polling(none_stop=False,interval=0)
