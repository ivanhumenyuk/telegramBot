import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 'Приветствую! Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для помощи Ивану Дмитриевичу!'.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def word(message):
    bot.send_message(message.chat.id, message.text)


# run
bot.polling(none_stop=True)
