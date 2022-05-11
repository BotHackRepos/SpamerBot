import telebot
# pip install pytelegrambotapi
token = 'токен'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def main(message):
     while True:
        bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')

@bot.message_handler(commands=["1"])
def foo(message):
     while True:
        bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
        while True:
           bot.send_message(message.chat.id, text='[][][][][[][][[][][]][[][][][][]]][[][][][][][]')
 
bot.polling()