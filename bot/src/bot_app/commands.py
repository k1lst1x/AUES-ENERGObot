from aiogram import types
from datetime import datetime

from .app import bot, dp, db, scheduler
from . keyboards import langMenu, mainMenu
from .translations import _
from . local_settings import ADMIN_IDS, TEXT_MESSAGE
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, UserDeactivated

# Функция рассылки сообщений
async def send_test_message():
    users = db.get_users()
    print(users)
    i = 0
    for user_tuple in users:
        user_id = user_tuple[0]
        try:
            username = await get_username(user_id)
            text_message = TEXT_MESSAGE.format(username=username)
            await bot.send_message(user_id, text_message, disable_web_page_preview=True)
        except (BotBlocked, ChatNotFound, UserDeactivated):
            print(f"Не удалось отправить сообщение пользователю с ID {user_id}. Бот заблокирован или чат не найден.")
        except Exception as e:
            print(f"Произошла ошибка при отправке сообщения пользователю с ID {user_id}: {e}")

async def get_username(user_id: int) -> str:
    user = await bot.get_chat(user_id)
    return user.first_name if user.first_name else "Пользователь"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        await message.answer('🌟 Пожалуйста, выберите предпочитаемый язык интерфейса 🌐\n\n🌍 Интерфейстің тілін таңдауыңызды сұраймыз 📣\n\n🌟 Please select your preferred interface language 🌐', reply_markup=langMenu)
    else:
        lang = db.get_lang(message.from_user.id)
        await message.answer(_('Добро пожаловать!', lang), reply_markup=mainMenu(lang))

@dp.message_handler(commands=['sendall'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMIN_IDS:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                await bot.send_message(row[0], text)
            await bot.send_message(message.from_user.id, "Успешная рассылка")

# Функция для получения текущего месяца и года
def get_current_month_and_year():
    now = datetime.now()
    return now.strftime("%B"), now.year

# Обработчик команды /statistics
@dp.message_handler(commands=['stat'])
async def statistics(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id in ADMIN_IDS:
            try:
                # Получение текущего месяца и года
                current_month, current_year = get_current_month_and_year()

                # Получение общего числа пользователей из базы данных
                total_users = len(db.get_users())

                # Формирование сообщения со статистикой
                statistics_message = f"📊 Statistics for {current_month} {current_year} 📊\n\n"
                statistics_message += f"Total Users: {total_users}\n"

                # Отправка сообщения с статистикой
                await message.reply(statistics_message)

            except Exception as e:
                await message.reply(f"An error occurred: {str(e)}") 

@dp.callback_query_handler(text_contains="lang_")
async def setLanguage(callback: types.CallbackQuery):
    await bot.delete_message(callback.from_user.id, callback.message.message_id)
    lang = callback.data[5:]

    if not db.user_exists(callback.from_user.id):
        db.add_user(callback.from_user.id, lang)
        await bot.send_message(callback.from_user.id, _('Успешная регистрация!', lang), reply_markup=mainMenu(lang))
    else:
        db.update_lang(callback.from_user.id, lang)
        await bot.send_message(callback.from_user.id, _('Язык успешно изменен!', lang), reply_markup=mainMenu(lang))


'''
# Планирование рассылки каждые 10 секунд
scheduler.add_job(send_test_message, 'interval', seconds=100)
'''
#scheduler.add_job(send_test_message, 'cron', day_of_week='mon', hour=8)
scheduler.add_job(send_test_message, 'interval', weeks=1)
