from aiogram import Router, F
import os 
from dotenv import load_dotenv
from bot import bot
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyb import main_keyboard, service_keyboard, design_keyboard

load_dotenv()

canlc_router = Router()

ADMIN_ID = int(os.getenv("ADMIN_ID"))


class Calcul (StatesGroup):
    waiting_for_type = State()
    waiting_for_disign = State()

@canlc_router.message(F.text.contains("Розрахувати вартість"))
async def start_calc(message: Message, state: FSMContext):
    await message.answer("🧮 <b>Калькулятор вартості</b>\n\n"
      "Оберіть тип бота, який вам потрібен:",
      reply_markup=service_keyboard(),
      parse_mode="HTML", 
      )

    await state.set_state(Calcul.waiting_for_type)


@canlc_router.message(
    F.text == "❌ Скасувати"
)
async def cancel_calc(message: Message, state: FSMContext):
  await state.clear()
  await message.answer("❌ Розрахунок скасовано.", reply_markup=main_keyboard())




@canlc_router.message(Calcul.waiting_for_type)
async def waiting_type(message:Message, state:FSMContext):
    await state.update_data(service = message.text)
    await message.answer("Оберіть бажаний варіант дизайну:",
      reply_markup=design_keyboard(),)
    await state.set_state(Calcul.waiting_for_disign)


@canlc_router.message(Calcul.waiting_for_disign)
async def waiting_disign(message:Message, state: FSMContext):
    await state.update_data(design = message.text)


    data = await state.get_data()


    service = data.get("service")
    design = data.get("design")

    price = "від 100$"
    if "Інтернет-магазин" in service:
        price = "від 200$"

    elif " Бот для запису" in service:
        price = "від 250$"

    if "Індивідуальний" in design:
        price = "оцінюється індивідуально (від $300)"


    username = (
        f"@{message.from_user.username}"
        if message.from_user.username
        else "Не вказано"
    )

    await message.answer(
      f"📊 <b>Результат попереднього розрахунку:</b>\n\n"
      f"📌 <b>Тип:</b> {service}\n"
      f"🎨 <b>Дизайн:</b> {design}\n"
      f"💰 <b>Орієнтовна вартість:</b> <b>{price}</b>\n\n"
      "Ми надіслали ваші дані адміністратору, він зв'яжеться з вами для"
      " уточнення деталей!",
      reply_markup=main_keyboard(),
      parse_mode="HTML",
  )
    admin_text = (
      f"🧮 <b>НОВИЙ ПРОРАХУНОК З КАЛЬКУЛЯТОРА!</b>\n\n"
      f"👤 <b>Користувач:</b> {username} (ID: <code>{message.from_user.id}</code>)\n"
      f"📌 <b>Тип:</b> {service}\n"
      f"🎨 <b>Дизайн:</b> {design}\n"
      f"💰 <b>Орієнтовно:</b> {price}"
  )


    await bot.send_message(chat_id=ADMIN_ID, text=admin_text, parse_mode="HTML")

    await state.clear()

