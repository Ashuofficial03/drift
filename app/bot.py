import os
import telebot
from pymongo import MongoClient

# Fetch environment variables injected by Kubernetes
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')

# Initialize Bot and Database
bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = MongoClient(MONGO_URI)
db = client.airdrop_db

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Log the interaction in MongoDB to prove the database connection works
    db.users.insert_one({"chat_id": message.chat.id, "username": message.chat.username})
    bot.reply_to(message, "Bot is live and connected to MongoDB!")

if __name__ == '__main__':
    print("Starting bot...")
    bot.infinity_polling()
