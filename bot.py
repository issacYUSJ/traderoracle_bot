import telebot

TOKEN = '7829418438:AAFoV7baZWl5VRjhQR4UO6iQRDE4joS0EQI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! TradeOracle bot is ready.")

bot.polling()
