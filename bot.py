import telebot
import time

# 당신의 봇 토큰으로 교체하세요
TOKEN = '7829418438:AAFoV7baZWl5VRjhQR4UO6iQRDE4joS0EQI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Hello! TradeOracle bot is ready.")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, "Just type /start to begin.")

# 기타 커맨드 추가 가능
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# 폴링 시작
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print("Error:", e)
            time.sleep(15)
