import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand
import aiohttp
import logging
import config

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Токен вашего бота
token = config.token

# Инициализация бота
bot = Bot(token=token)

# Инициализация диспетчера
dp = Dispatcher(bot)

# Функции

async def send_welcome(message: types.Message):
    await message.answer("Привет! Я твой бот.")

async def send_help(message: types.Message):
    await message.answer("Список доступных команд: /start, /help")

async def provide_lessons(message: types.Message):
    # Здесь будет логика для предоставления уроков
    await message.answer("Вот ваш урок на сегодня...")

async def send_notifications(message: types.Message):
    # Здесь будет логика для отправки уведомлений
    await message.answer("У вас запланирован урок...")

async def suggest_exercises(message: types.Message):
    # Здесь будет логика для предложения заданий
    await message.answer("Попробуйте выполнить это упражнение...")

async def select_difficulty(message: types.Message):
    # Здесь будет логика для выбора уровня сложности
    await message.answer("Выберите уровень сложности: Начинающий, Средний, Продвинутый.")

async def search_topics(message: types.Message):
    # Здесь будет логика для поиска по темам
    await message.answer("Введите тему, по которой вы хотите получить материалы...")

async def rewards_system(message: types.Message):
    # Здесь будет логика для системы наград и достижений
    await message.answer("Вы заработали новую награду!")

async def support_languages(message: types.Message):
    # Здесь будет логика для поддержки множества языков
    await message.answer("Выберите язык для изучения из списка...")

async def personalized_recommendations(message: types.Message):
    # Здесь будет логика для персонализированных рекомендаций
    await message.answer("На основе ваших успехов, мы рекомендуем вам...")


# Регистрация обработчиков сообщений
dp.register_message_handler(send_welcome, commands=['start'])
dp.register_message_handler(send_help, commands=['help'])
dp.register_message_handler(provide_lessons, commands=['lessons'])
dp.register_message_handler(send_notifications, commands=['notifications'])
dp.register_message_handler(suggest_exercises, commands=['exercises'])
dp.register_message_handler(select_difficulty, commands=['difficulty'])
dp.register_message_handler(search_topics, commands=['search'])
dp.register_message_handler(rewards_system, commands=['rewards'])
dp.register_message_handler(support_languages, commands=['languages'])
dp.register_message_handler(personalized_recommendations, commands=['recommendations'])

# Функция для закрытия асинхронных ресурсов
async def close_resources():
    await bot.session.close()

async def on_startup(dispatcher: Dispatcher):

    # Установка команд бота
        await bot.set_my_commands([
        BotCommand(command="/start", description="Начать работу с ботом"),
        BotCommand(command="/help", description="Показать помощь"),
        BotCommand(command="/lessons", description="Получить уроки"),
        BotCommand(command="/notifications", description="Настройка уведомлений"),
        BotCommand(command="/exercises", description="Получить задания для практики"),
        BotCommand(command="/difficulty", description="Выбрать уровень сложности уроков"),
        BotCommand(command="/search", description="Поиск по темам уроков"),
        BotCommand(command="/rewards", description="Система наград и достижений"),
        BotCommand(command="/languages", description="Выбрать язык обучения"),
        BotCommand(command="/recommendations", description="Получить персонализированные рекомендации"),
    ])
        # Добавьте здесь новые команды

# # Запуск бота
async def main():
    # Выполнение функции on_startup
    await on_startup(dp)
    # Запуск опроса бота
    await dp.start_polling()

async def close_resources():
    await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped manually")
    finally:
        asyncio.run(close_resources())

