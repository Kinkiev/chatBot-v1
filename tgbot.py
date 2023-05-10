import os
import config 
import telebot

from telebot import types

bot = telebot.TeleBot(config.TOKEN1)
sti2 = open('static/shto.webp', 'rb')

@bot.message_handler(commands=['start'])


def send_welcome(message):
   sti = open('static/1welcome.webp', 'rb')
   bot.send_sticker(message.chat.id, sti)
   
   markup = types.InlineKeyboardMarkup(row_width=2)
   item1 = types.InlineKeyboardButton('Ілля', callback_data='illa')
   item2 = types.InlineKeyboardButton('Богдан', callback_data='bogdan')
   
   markup.add(item1, item2)
   
   #bot.reply_to(message, "Хто ти, воїн?")
   
   bot.send_message(message.chat.id, "\nЯ - <b>{1.first_name}</b>, бот створений щоб ти отримав відповіді, але спочатку скажи мені, хто ти, воїн?".format(message.from_user, bot.get_me()), 
                    parse_mode='html', reply_markup=markup)
   
   @bot.callback_query_handler(func=lambda call: True)
      
   def callback_inline(call):
      try:
          if call.message:
             if call.data == 'illa':
               bot.send_message(call.message.chat.id, 'Привіт Ілля')
             elif call.data == 'bogdan':
               bot.send_message(call.message.chat.id, 'Привіт Богдан')
               
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отже",
               reply_markup=None)
             #else:
             #  bot.send_sticker(message.chat.id, sti2)
              # bot.send_message(message.chat.id, 'Я не поняв')
               
            
      except Exception as e:
         print(repr(e))
         
@bot.message_handler(content_types=['text'])       
   
   
#SHTO  
#@bot.message_handler(content_types=['text'])
#def send_text_message(message):
#      bot.send_sticker(message.chat.id, sti2)
  
# ДАЛІ НІЧОГО НЕ ВІДБУВАЄТЬСЯ. ПОТРІБЕН НАСТУПНИЙ КРОК 

def send_text_message(message):
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    item3 = types.InlineKeyboardButton('Працювати', callback_data='work')
    item4 = types.InlineKeyboardButton('Працювати більше', callback_data='work_more')
      
    markup2.add(item3, item4)
    lalala = 'Що ти хочеш воїне?'

    bot.send_message(message.chat.id, lalala, parse_mode='html', reply_markup=markup2)
      
    @bot.callback_query_handler(func=lambda call: True)
    
    def callback_inline(call):
      try:
          if call.message:
             if call.data == 'work':
               bot.send_message(call.message.chat.id, 'спробуй працювати більше')
             elif call.data == 'work_more':
               bot.send_message(call.message.chat.id, 'молодець, продовжуй')
               
             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тоді",
               reply_markup=None)
             
      except Exception as e:
       print(repr(e))
            
# bot.infinity_polling()  
bot.polling(none_stop=True) 


#@bot.message_handler(content_types=['text'])
#def get_text_messages(message):
#   if message.text == "Ілля":
 #     bot.send_message(message.from_user.id, "Зарплата тобі не потрібна")
  # elif message.text == "Илья":
   #   bot.send_message(message.from_user.id, "Напиши своє імʼя державною, воїне")
#   elif message.text == "Іван":
#      bot.send_message(message.from_user.id, "Грошей нема, занотуй собі")
#   elif message.text == "Иван":
#      bot.send_message(message.from_user.id, "Напиши своє імʼя державною, воїне")
 #  elif message.text == "Богдан":
#      bot.send_message(message.from_user.id, "Нехай тік-ток платить")
 #  elif message.text == "Костя":
  #    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
  #    user_markup.ReplyKeyboardMarkup('Зарплату')
  #    user_markup.ReplyKeyboardMarkup('Бабло')
  #    bot.send_message(message.from_user.id, "Що ти хочеш отримати?")
  # elif message.text == "Зарплату":
  #      bot.send_message(message.from_user.id, "Зарплату зараховано")
  # else:
  #    bot.send_message(message.from_user.id, "Я тебе не знаю. Напиши правильне імʼя.")
  

