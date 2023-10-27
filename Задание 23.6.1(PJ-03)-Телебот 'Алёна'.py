import telebot
from config import keys, TOKEN
from extentions import ConvertionExeption, FiatConverter
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать, введите команду в следующем формате:\n'
            '<Название валюты> \n'
            '<Название валюты перехода> \n'
            '<Количество переводимой валюты>\n'
            'Чтобы увидеть список доступных валют, нажмите: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeption('Должно быть ровно три параметра')

        quote, base, amount = values
        total_base = FiatConverter.get_price(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя \n {e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n {e}')
    else:
        text = f'Цена за {amount} {quote} в валюте "{base}" равна {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
