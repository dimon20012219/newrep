import telebot
import constants
bot = telebot.TeleBot(constants.token)

#bot.send_message(398870828,"ногу высоси дура")
#upd = bot.get_updates()
#print (upd)
#last_upd  = upd[-1]
#message_from_user = last_upd.message
#prit(message_from_user)
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "ногу соси":
        bot.send_message(message.chat.id, "сам высоси дура тупая")
    elif message.text == "не ну ты и дура":
        bot.send_message(message.chat.id,"да как ты заебал")
    else:
        bot.send_message(message.chat.id, "ВИ ВИ СУКА")

bot.polling(none_stop=True, interval=0)