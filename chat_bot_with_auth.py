import csv
import telebot

token = '703375336:AAGr5sjJHIi8fmre-iv0C4ZWY91IJWoayRc'

CHANNEL_NAME = '@bot_expl'

bot = telebot.TeleBot(token)

strt = False
id = "0"
nik = ""
name = ''

@bot.message_handler(commands=['start'])
def register(message):
    global strt
    strt = True
    if proverka(message.chat.id):
        bot.send_message(message.chat.id, 'Извините, но Вы уже зарегистрированы в системе как ' + name)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста представьтесь')


@bot.message_handler(content_types=['text'])
def send_message(message):
    if proverka(message.chat.id):
        bot.send_message(CHANNEL_NAME, message.text + '\nP.S. ' + name)
    elif strt:
        global nik
        nik = message.text
        input_nik(message.chat.id)
    else:
        bot.send_message(message.chat.id,  'Сначала зарегистрируйтесь')



def input_nik(chat_id):
    if strt:
        f = open('niks.csv', "a", newline="")
        user = [chat_id, str(nik)]
        writer = csv.writer(f)
        writer.writerow(user)
        f.close()
        bot.send_message(chat_id, 'Вы успешно зарегистрированы, ' + nik)


def proverka(chat_id):
    f = open('niks.csv', "r", newline="")
    reader = csv.reader(f)
    for row in reader:
        if str(row[0]) == str(chat_id):
            global name
            name = row[1]
            return True
    return False
    f.close()

bot.polling(none_stop=True)