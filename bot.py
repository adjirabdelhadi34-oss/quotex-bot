import telebot

# حط هنا التوكن الخاص بالبوت تاعك من BotFather
TOKEN = "8552655222:AAGUu8HNJ2aLf2GiNrBGVSQqJUOSaBEy0sI"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلا بيك 😎! أنا بوت التداول الذكي تاع Quotex 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"📩 استقبلت: {message.text}")

bot.polling()
