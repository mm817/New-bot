import telebot
from telebot import types

# Replace with your Bot Token and your Telegram ID
BOT_TOKEN = '8224719724:AAH3koXkHsyNgy2ZTeLfkwASSjaHGtSRW-I'
ADMIN_ID = '1237435256'

bot = telebot.TeleBot(BOT_TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button = types.KeyboardButton("Share Phone Number 📞", request_contact=True)
    markup.add(button)
    bot.send_message(message.chat.id,
                     f"Hi {message.from_user.first_name}, please share your phone number to continue.",
                     reply_markup=markup)

# When contact is shared
@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    if message.contact is not None:
        name = message.contact.first_name
        phone = message.contact.phone_number
        user_id = message.from_user.id

        # Notify the user
        bot.send_message(message.chat.id, "Thanks! Your phone number has been received. ✅")

        # Send to admin
        bot.send_message(ADMIN_ID,
                         f"📥 New User Shared Contact:\n\n"
                         f"👤 Name: {name}\n"
                         f"📱 Phone: {phone}\n"
                         f"🆔 Telegram ID: {user_id}")
    else:
        bot.send_message(message.chat.id, "Something went wrong. Please try again.")

# Run the bot forever
bot.infinity_polling()