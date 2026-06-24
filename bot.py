import telebot

TOKEN = "BU_YERGA_BOT_TOKENINGNI_YOZ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Bot ishlayapti! 🤖")

print("Bot ishga tushdi...")
bot.infinity_polling()
