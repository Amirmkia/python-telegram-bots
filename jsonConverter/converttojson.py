import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update, chat
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler
)
from flask import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove

startingbot , cancelbot = range(2)
def start(update: Update, context: CallbackContext) -> int:
    username = update.message.from_user['first_name']
    update.message.reply_text(
        f"سلام بر ستون تریدهای نامنطم {username} متن رو برام بفرست تا مثل هلو برات تبدیلش کنم "
    )
    return startingbot
def convert(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(
       '{"content":' + f'"{text}"' + "}"
    )
    return cancel(update , context)

def cancel(update: Update, context: CallbackContext):
    return ConversationHandler.END
    
def main() :
    '''main section , mother of functions :D  , bot keep run and state was run in this section'''
    updater = Updater("5102326875:AAE8rynkU9ew5q5cuwu9X9W0RLS5qjEAi2w")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[
        CommandHandler('start', start),
        ],
        states = {
           startingbot : [MessageHandler(Filters.text & ~Filters.command, convert)],
           cancelbot : [ MessageHandler(Filters.regex('^(تبدیل متن)$'), start),]
        },
        fallbacks=[CommandHandler('cancel', cancel),],
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()