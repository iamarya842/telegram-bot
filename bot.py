import telebot

TOKEN = "8798615501:AAEMrTHWsHpDggiYsqjeIFNAzJWSltFrI0g"
CHANNEL_ID = -1003843176537
BOT_USERNAME = "Ghopghop842_bot"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    args = message.text.split()

    if len(args) > 1:
        try:
            post_id = int(args[1])

            bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=post_id
            )
        except:
            bot.reply_to(message, "⚠️ Post nahi mila.")
    else:
        bot.reply_to(message, "Channel post link bhejo, main bot link bana dunga.")

@bot.message_handler(func=lambda message: True)
def generate_link(message):
    text = message.text

    if "t.me/c/" in text:
        try:
            post_id = text.split("/")[-1]

            bot_link = f"https://t.me/{BOT_USERNAME}?start={post_id}"

            bot.reply_to(
                message,
                f"✅ Bot Link Ready:\n\n{bot_link}"
            )
        except:
            bot.reply_to(message, "⚠️ Link galat hai.")
    else:
        bot.reply_to(message, "❌ Channel post link bhejo.")

print("Bot started...")
bot.infinity_polling()
