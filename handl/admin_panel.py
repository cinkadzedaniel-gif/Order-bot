from aiogram import Router, F
from aiogram.types import Message
from dotenv import load_dotenv
import os
from keyb import admin_panel, main_keyboard, admin_main_keyboard
from base import Session, User

load_dotenv()

admin_router = Router()

admin_id_env = os.getenv("ADMIN_ID")
ADMIN_ID = int(admin_id_env) if admin_id_env else 0


@admin_router.message(F.text == "🔐 Адмін-панель")
async def start_admin(message: Message):
    if message.from_user.id != ADMIN_ID:
        return
    await message.answer("Адмін панель відкрита! Оберіть дію:", reply_markup=admin_panel())


# Змінено з callback_query на message, оскільки це кнопка з Reply-клавіатури
@admin_router.message(F.text == "Усі користувачі")
async def all_user(message: Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ У вас немає прав доступу!")
        return

    session = Session()
    try:
        users = session.query(User).all()

        if not users:
            await message.answer("📭 У базі даних поки немає жодної заявки.")
            return

        response_text = "📋 <b>Список усіх залишених заявок:</b>\n\n"
        
        for item in users:
            response_text += (
                f"🆔 <b>ID:</b> <code>{item.id}</code>\n"
                f"👤 <b>Username:</b> {item.username}\n"
                f"📌 <b>Тип бота:</b> {item.types}\n"
                f"🛠 <b>Функціонал:</b> {item.func}\n"
                f"💰 <b>Бюджет:</b> {item.budget}\n"
                f"-----------------------------------\n"
            )

        await message.answer(response_text, parse_mode="HTML")

    except Exception as e:
        await message.answer(f"⚠️ Виникла помилка при читанні бази даних: {e}")
    finally:
        session.close()


@admin_router.message(F.text == "У головне меню")
async def back_menu(message: Message):
    await message.answer("Повертаємось у головне меню", reply_markup=admin_main_keyboard())