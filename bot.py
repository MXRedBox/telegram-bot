from elproblemo import token
import telebot

bot = telebot.Telebot(token["TOKEN"])

@bot.message_handler(commands=["start"])
def start_func(message):
    bot.send_message(message.chat.id, "Как тебя зовут?")

@bot.message_handler(content_types=["text"])
def hello(message):
    msg = bot.send_message(message.chat.id, f"Привет, {message.text}")
    bot.register_next_step_handler(msg, name)

@bot.message_handler(content_types=["text"])
def name(message):
    bot.send_message(message.chat.id, "Как дела?")

if __name__ == '__main__':
    bot.polling(none_stop=True)
# print(token["TOKEN"])