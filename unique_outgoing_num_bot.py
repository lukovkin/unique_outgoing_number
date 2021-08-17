import os

from flask import Flask

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

app = Flask(__name__)

@app.route("/")
def hello_world():
    updater.start_polling()
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    

