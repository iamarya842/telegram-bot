import telebot
import time
import threading

TOKEN = 8381181264:AAE95B3hJENM0mkSHJupQq-VY6hkEtaTdaM
CHANNEL_ID = -1003725954968

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def send_post(message):
    text = message.text
    
    if "t.me/c/" in text:
        try:
            post_id = int(text.split("/")[-1])
            msg = bot.copy_message(message.chat.id, CHANNEL_ID, post_id)

            # 20 minute baad delete
            def delete_msg():
                time.sleep(1200)
                bot.delete_message(message.chat.id, msg.message_id)

            threading.Thread(target=delete_msg).start()

        except:
            bot.reply_to(message, "Post nahi mila ❌")

bot.infinity_polling()
