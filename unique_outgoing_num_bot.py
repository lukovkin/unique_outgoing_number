from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='1942145754:AAHp8-mw7lOIBKCwvSDywe3usrlmGzmok0k', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    
def test(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Test passed")   
    
start_handler = CommandHandler('start', start)
test_handler = CommandHandler('test', test)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(test_handler)

updater.start_polling()
