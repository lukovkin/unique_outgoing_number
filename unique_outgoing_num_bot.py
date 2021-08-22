import os
import uuid

from flask import Flask

from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger()

token = os.environ.get('TOKEN')
logger.debug(token)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
def test(update, context):
    user = update.message.from_user
    logger.info(str(user))
    logger.info(str(context.__dict__))
    context.bot.send_message(chat_id=update.effective_chat.id, text="Test passed. User data: {}".format(str(context.user_data)))
    
def outgoing_id(update, context):
    out_id = uuid.uuid4()
    user = update.message.from_user['username']
    text = f"@{user}, Вашему исходящему присвоен № {str(out_id)}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    
start_handler = CommandHandler('start', start)
test_handler = CommandHandler('test', test)
outgoing_id_handler = CommandHandler('outgoing', outgoing_id)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(test_handler)
dispatcher.add_handler(outgoing_id_handler)

updater.start_polling()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    

