import telebot
import time
import threading

# -------------------------
# SETUP — Replace with your own
TOKEN = 8381181264:AAE95B3hJENM0mkSHJupQq-VY6hkEtaTdaM
CHANNEL_ID = -1003789323635
# -------------------------

bot = telebot.TeleBot(TOKEN)

# Function to send posts from Telegram channel links
@bot.message_handler(func=lambda message: True)
def send_post(message):
    text = message.text

    if "t.me/c/" in text:  # Agar message me Telegram channel link hai
        try:
            post_id = int(text.split("/")[-1])
            msg = bot.copy_message(message.chat.id, CHANNEL_ID, post_id)

            # Delete after 20 minutes (1200 seconds)
            def delete_msg():
                time.sleep(1200)
                bot.delete_message(message.chat.id, msg.message_id)

            threading.Thread(target=delete_msg).start()

        except:
            bot.reply_to(message, "Post nahi mila ❌")

# Start the bot
print("Bot started… ✅")
bot.infinity_polling()
