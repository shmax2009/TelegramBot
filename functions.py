import telebot

import time

import pprint

from Nod_func import find_nod

from Nok_func import find_nok

from middle import middle


text = open("password.txt", "r")
BOT_TOKEN = text.read()

bot = telebot.TeleBot(BOT_TOKEN)

COMMANDS = ['Nod', 'Nok', '+', '-', '*', '/', '//']

#commands = ['+', '-', '*', '/', 'div', 'mod', '**']
#def cmd_calc(cmd):
    # msg = bot.send_message(cmd.chat.id, f'Введите числа.')
    # bot.register_next_step_handler(msg, next_step)
    


@bot.message_handler(commands = ['start'])
def send_welcome(cmd):
    print(f'cmd.text: {cmd.from_user.first_name}')
    bot.send_message(cmd.chat.id, f'Привет, {cmd.from_user.first_name}.')
    bot.send_message(cmd.chat.id, f'Я бот-помощник для решения математики. Если нужно больше информации, то введите /help.')

@bot.message_handler(commands = ['help'])
def cmd_help(cmd):
    print(f'cmd.text: {cmd.from_user.first_name}')
    bot.send_message(cmd.chat.id, f"Вот все команды которые я знаю:")
    for cmd_printer in COMMANDS:
        bot.send_message(cmd.chat.id, f'\t*| {cmd_printer}')
    bot.send_message(cmd.chat.id, f"Если хотите чтоб я что-то выполнил, например, НОД, то введите nod x y. Или сложение: 1 + 2. Ваш ответ: 3. И другое.")
    # начнём тут!!!
    
#--------------------------------------------------------

@bot.message_handler(content_types=["sticker"])
def echo_sticker(message):
    bot.send_sticker(
        message.chat.id,
        # message.sticker.file_id,
        "CAACAgQAAxkBAAMeXp2RtBeha7c1zGSRXhMEtaPzZhMAAgcBAAKXa4YEykm6GWPFwCoYBA",
    )
@bot.message_handler()
def next_step(cmd):
    print(f'cmd.text: {cmd.from_user.first_name}')
    x = cmd.text.split(" ")
    a = b = c = ''
            
    if len(x) > 3:
        if c == '+': 
            a, b = x[0], x[2]
            res = int(a) + int(b)
        elif c == '-':
            a, b = x[0], x[2]
            res = int(a) - int(b)
        elif c == '*':
            a, b = x[0], x[2]
            res = int(a) * int(b)
        elif c == '/':
            a, b = x[0], x[2]
            res = int(a) / int(b)
        elif c == 'div':
            a, b = x[0], x[2]
            res = int(a) // int(b)
        elif c == 'mod':
            a, b = x[0], x[2]
            res = int(a) % int(b)
        elif c == '**':
            a, b = x[0], x[2]
            res = int(a) ** int(b) 
        elif a == 'nod':
            a, b = x[0], x[2]
            res = find_nod(int(c), int(b))   
        elif a == 'nok':
            a, b = x[0], x[2]
            res = find_nok(int(c), int(b)) 
        elif a =='middle':
            del x[0]
            res = middle(x)
        else:
        
        # bot.send_photo(cmd.chat.id, 'error.png')
            bot.reply_to(cmd, f"Ваш ответ: {res}")


    

#--------------------------------------------------------
