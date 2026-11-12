import os
from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from bot import bot
from dotenv import load_dotenv
from keyb import cancel_keyboard, main_keyboard, share_number
from base import User, Session

load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID"))

tz_router = Router()


class TZ(StatesGroup):
  waiting_for_type = State()
  waiting_for_func = State()
  waiting_for_money = State()
  waiting_for_contact = State()


@tz_router.message(
    F.text == "❌ Скасувати",)
async def cancel_order(message: Message, state: FSMContext):
  await state.clear()
  await message.answer(
      "❌ Формування заявки скасовано.", reply_markup=main_keyboard()
  )


@tz_router.message(F.text.contains("Залишити заявку"))
async def start_tz(message: Message, state: FSMContext):
  await message.answer(
      "Чудово! Давайте сформуємо коротке ТЗ.\n\n"
      "<b>Крок 1/4:</b> Опишіть коротко тему та мету бота (наприклад: бот для"
      " запису в салон, інтернет-магазин тощо):",
      parse_mode="HTML",
      reply_markup=cancel_keyboard(),
  )
  await state.set_state(TZ.waiting_for_type)


@tz_router.message(TZ.waiting_for_type)
async def waiting_type(message: Message, state: FSMContext):
  await state.update_data(types=message.text)
  await message.answer(
      "<b>Крок 2/4:</b> Які основні функції має виконувати бот? (Оплати,"
      " Google Таблиці, сповіщення тощо):",
      parse_mode="HTML",
      reply_markup=cancel_keyboard(),
  )
  await state.set_state(TZ.waiting_for_func)


@tz_router.message(TZ.waiting_for_func)
async def waiting_func(message: Message, state: FSMContext):
  await state.update_data(func=message.text)
  await message.answer(
      "<b>Крок 3/4:</b> Вкажіть бажані терміни та орієнтовний бюджет (якщо є):",
      parse_mode="HTML",
      reply_markup=cancel_keyboard(),  # Додали клавіатуру скасування сюди
  )
  await state.set_state(TZ.waiting_for_money)


@tz_router.message(TZ.waiting_for_money)
async def waiting_busget(message: Message, state: FSMContext):
  await state.update_data(budget=message.text)
  await message.answer(
      "<b>Крок 4/4:</b> Поділіться контактом для зв'язку (натисніть кнопку"
      " нижче) або напишіть свій номер/Telegram handle у повідомленні:",
      reply_markup=share_number(),  # Залишили лише одну клавіатуру без дублювання
      parse_mode="HTML",
  )
  await state.set_state(TZ.waiting_for_contact)

@tz_router.message(TZ.waiting_for_contact)
async def waiting_contact(message: Message, state: FSMContext):
    phone = message.contact.phone_number if message.contact else message.text

    user_data = await state.get_data()
    types = user_data.get("types")
    func = user_data.get("func")
    budget = user_data.get("budget")

    username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else "Не вказано"
    )
    user_id = message.from_user.id

    # 1. Створюємо сесію для роботи з базою даних
    db_session = Session()
    try:
        # 2. Створюємо запис користувача
        new_user = User(
            id=user_id, 
            username=username, 
            types=types, 
            func=func, 
            budget=budget
        )
        
        # 3. Додаємо в сесію та зберігаємо в базу даних
        db_session.add(new_user)
        db_session.commit()
    except Exception as e:
        print(f"Помилка збереження в БД: {e}")
        db_session.rollback()
    finally:
        db_session.close() # Обов'язково закриваємо сесію

    admin_text = (
        f"📋 <b>НОВА ЗАЯВКА НА РОЗРОБКУ (ТЗ)!</b>\n\n"
        f"👤 <b>Замовник:</b> {username} (ID: <code>{message.from_user.id}</code>)\n"
        f"📞 <b>Контакт:</b> {phone}\n"
        f"📌 <b>Тип бота:</b> {types}\n"
        f"🛠 <b>Функціонал:</b> {func}\n"
        f"💰 <b>Бюджет/Терміни:</b> {budget}"
    )

    await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")

    await message.answer(
        "Дякуємо! Ваша заявка успішно прийнята. Ми зв'яжемося з вами найближчим часом!",
        reply_markup=main_keyboard(),
    )
    await state.clear()