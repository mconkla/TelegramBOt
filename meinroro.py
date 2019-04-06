
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
from telegram.inline.inlinekeyboardbutton import InlineKeyboardButton
from telegram.inline.inlinekeyboardmarkup import InlineKeyboardMarkup
import logging
import telegram



def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Willkommen bei meinem Bot")

def gamelink(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="http://t.me/MconklaBot?game=numberguess")

def end(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Bot wird geschlossen)")



def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def caps(bot, update, args):
    if args != []:
        text_caps = ' '.join(args).upper()
        bot.send_message(chat_id=update.message.chat_id, text=text_caps)
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Bitte Text mitgeben!")

def inline_caps(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='http://t.me/MconklaBot?game=numberguess',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    bot.answer_inline_query(update.inline_query.id, results)

def button(bot, update):
    bot.answerCallbackQuery(update.callback_query.id, url="http://127.0.0.1:8000/part1.html")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Command doesn't exist!")


#def options_cmd(bot, update):
#    option_1_button = InlineKeyboardButton(text="1", callback_data="op_1")
#    option_2_button = InlineKeyboardButton(text="2", callback_data="op_2")
#    option_3_button = InlineKeyboardButton(text="3", callback_data="op_3")
#    option_4_button = InlineKeyboardButton(text="4", callback_data="op_4")
#    opt_keyboard = InlineKeyboardMarkup([[option_1_button,option_2_button], [option_3_button,option_4_button]])
#
#    bot.sendMessageText(chat_id='@channelusername',reply_markup=opt_keyboard)
  #  db = DBwrapper.get_instance()

    #if update.callback_query:
        # TODO maybe text user in private instead of group!
        #lang_id = db.get_lang_id(update.callback_query.from_user.id)
        #bot.editMessageText(chat_id=update.callback_query.message.chat_id, text=translate("Option Select", lang_id),
    #                        reply_markup=opt_keyboard, message_id=update.callback_query.message.message_id)
	#opt_id = get_lang_id(update.message.from_user.id)
	#bot.sendMessage(chat_id=update.message.chat_id, text=translate("langSelect", lang_id),
     #                   reply_markup=opt_keyboard, message_id=update.message.message_id)




logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token='798864969:AAHwe5If69BM0g94YUZwT3GrQ38zdzTyz94')

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

end_handler = CommandHandler('end', end)
dispatcher.add_handler(end_handler)

gamelink_handler = CommandHandler('gamelink', gamelink)
dispatcher.add_handler(gamelink_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

#options_handler = CommandHandler('options', options_cmd)
#dispatcher.add_handler(options_handler)

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

callback_handler = CallbackQueryHandler(button)
dispatcher.add_handler(callback_handler)




updater.start_polling()
updater.idle()

