from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyb import cancel, main_keyboard
from dotenv import load_dotenv
import os
from bot import bot

load_dotenv()

ADMIN_ID = os.getevn("ADMIN_ID")

support_router = Router()


class Support(StatesGroup):
    waiting_problems = State()
    

@support_router.message(F.text == "Повернутись")
async def back_to_menu(message:Message):
    await message.answer("Повертаємось у головне меню", reply_markup=main_keyboard())

@support_router.message(F.text == "📩 Підтримка")
async def support(message:Message, state:FSMContext):
    await message.asnwer("Опишіть ваше питання або проблему нижче, і ми зв'яжемося з вами:", reply_markup = cancel()) 
    await state.set_state(Support.waiting_problems)

@support_router.message(Support.waiting_problems)
async def waiting_probllem(message:Message, state: FSMContext):
    problem = message.text

    await bot.forward_message(
      chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id
  )

    await bot.send_message(
      chat_id=ADMIN_ID,
      text=(
          f"📩 Нове звернення до підтримки!\nВід: @{message.from_user.username}"
          f"Проблема: {problem}"
      ),
  )
    
    await message.answer("Ваше повідомлення надіслано адміністратору! Очікуйте"
                       " відповіді.")
    await state.clear()