import telebot
# pip install pytelegrambotapi
token = 'токен'
bot = telebot.TeleBot(token)

chat_id = '5077197358'


@bot.message_handler(commands=["start"])
def main(message):
     while True:
           if (message.chat.id == chat_id):
              print('No! This is developer bot')
           else:
             print('Spam attack started')
             bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')

@bot.message_handler(commands=["1"])
def foo(message):
     while True:
           if (message.chat.id == chat_id):
              print('No! This is developer bot')
           else:
             print('Spam attack started')
             bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
        while True:
           if (message.chat.id == chat_id):
              print('No! This is developer bot')
           else:
             print('Spam attack started')
             bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')
 
bot.polling()
