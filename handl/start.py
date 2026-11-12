import os
from dotenv import load_dotenv
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyb import main_keyboard, admin_panel, admin_main_keyboard

load_dotenv()

start_router = Router()

# Безпечне зчитування ADMIN_ID: якщо змінна відсутня, підставляється 0
admin_id_env = os.getenv("ADMIN_ID")
ADMIN_ID = int(admin_id_env) if admin_id_env else 0

@start_router.message(CommandStart())
async def start(message: Message):

    text = (
        "👋 <b>Вітаю у BotStudio!</b>\n\n"
        "Ми створюємо <i>сучасних Telegram-ботів</i>, які працюють на твій бізнес 24/7: "
        "залучають клієнтів, приймають замовлення та автоматизують рутину.\n\n"
        "⚡ <b>Що ми пропонуємо:</b>\n\n"
        "🛍 <b>Боти-каталоги та Магазини</b> — прийом замовлень, оплат та онлайн-вітрина прямо в Telegram.\n"
        "📅 <b>Запис на послуги</b> — автоматичне бронювання часу для салонів, майстрів та консультантів.\n"
        "📥 <b>Лидогенерація та Видача контенту</b> — автоматична видача файлів, гайдів, курсів за підписку або оплату.\n"
        "⚙️ <b>Кастомні рішення</b> — унікальна логіка під будь-які задачі вашого бізнесу.\n\n"
        "🎯 <b>Чому обирають нас:</b>\n"
        "• Сучасний та інтуїтивний дизайн\n"
        "• Швидкі сповіщення про нові заявки\n"
        "• Підтримка та допомога з запуском\n\n"
        "🔽 <b>Обери потрібну опцію нижче, щоб розрахувати вартість або оформити заявку:</b>"
    )

    if message.from_user.id != ADMIN_ID:
        await message.answer(text, parse_mode="HTML", reply_markup=main_keyboard())
    else:
        await message.answer("Вітаю, адміне!", parse_mode="HTML", reply_markup=admin_main_keyboard())