import os


my_api_key = os.getenv('my_api_key')


from Adafruit_IO import Client
aio = Client('onlyhuman143','my_api_key')
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('bedroom-lights',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Lights turned on')

def demo2(bot,update):
  aio.send('bedroom-lights',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Lights turned off')

def demo3(bot,update):
  aio.send('fans',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fans turned on')

def demo4(bot,update):
  aio.send('fans',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fans turned off')    

def main(bot,update):
  a= bot.message.text
  if a=="Turn on light":
    demo1(bot,update)
  elif a=="Turn off light":
    demo2(bot,update)
  elif a=="Turn on fan":
    demo3(bot,update)
  elif a=="Turn off fan":
    demo4(bot,update)

bot_token = os.getenv('bot_token')
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
    
