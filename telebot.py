import telegram
from telegram.ext import Updater, CommandHandler

# Вставьте токен вашего бота Telegram
TOKEN = '6169348067:AAGYY9rYKYU-Tyq2_X1VNxOjJUCN2It0bMg'

# Функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот Telegram!")

# Создание объекта бота Telegram
bot = telegram.Bot(token=TOKEN)

# Создание объекта Updater для получения обновлений от Telegram API
updater = Updater(token=TOKEN, use_context=True)

# Создание объекта диспетчера и добавление обработчика команды /start
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))

# Запуск бота
updater.start_polling()
updater.idle()

