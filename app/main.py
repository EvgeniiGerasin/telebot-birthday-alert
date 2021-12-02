from config.token import TOKEN
from config.messages import TextMessage
from db.action import DataBase

import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    match message.text:
        case '/help':
            bot.send_message(message.from_user.id, TextMessage.HELP)
        case '/all':
            records = DataBase.get_all_birthday()
            response = """"""
            for name, date in records.items():
                response = response + f"*{date}* *|* {name}\n"
            bot.send_message(message.from_user.id, response, parse_mode= "Markdown")
        case '/month':
            records = DataBase.get_current_month_birthday()
            response = """"""
            for name, date in records.items():
                response = response + f"*{date}* *|* {name}\n"
            bot.send_message(message.from_user.id, response, parse_mode= "Markdown")
        case _:
            bot.send_message(
                message.from_user.id, 
                f'Нет такой команды: "{message.text}" \n\t {TextMessage.HELP}'
            )


bot.polling(none_stop=True, interval=0)
