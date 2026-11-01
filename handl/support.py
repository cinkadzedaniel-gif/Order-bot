import os
import re
from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from keyb import cancel, main_keyboard

load_dotenv()

# Переводимо ADMIN_ID в число (int), щоб коректно порівнювати з ID користувача
ADMIN_ID = int(os.getenv("ADMIN_ID"))

support_router = Router()


class Support(StatesGroup):
  waiting_problems = State()


# 1. Запуск звернення до підтримки
@support_router.message(F.text == "📩 Підтримка")
async def support(message: Message, state: FSMContext):
  await message.answer(
      "Опишіть ваше питання або проблему нижче, і ми зв'яжемося з вами:",
      reply_markup=cancel(),
  )
  await state.set_state(Support.waiting_problems)


# 2. Отримання питання від користувача та надсилання адміністратору
@support_router.message(Support.waiting_problems)
async def user_support_message(message: Message, state: FSMContext, bot):
  user_info = (
      f"@{message.from_user.username}"
      if message.from_user.username
      else "Немає username"
  )

  # Надсилаємо тобі картку звернення з чітко вказаним ID
  await bot.send_message(
      chat_id=ADMIN_ID,
      text=(
          f"📩 <b>Нове звернення від користувача!</b>\n"
          f"👤 Користувач: {user_info}\n"
          f"🆔 ID: <code>{message.from_user.id}</code>\n\n"
          f"💬 <b>Повідомлення:</b>\n{message.text}"
      ),
      parse_mode="HTML",
  )

  await message.answer(
      "Дякуємо! Ваше повідомлення передано адміністратору. Очікуйте на"
      " відповідь.",
      reply_markup=main_keyboard(),  # Повертаємо головне меню користувачу
  )
  await state.clear()


# 3. Кнопка скасування / повернення
@support_router.message(F.text == "Повернутись")
async def back_to_menu(message: Message, state: FSMContext):
  await state.clear()
  await message.answer("Повертаємось у головне меню", reply_markup=main_keyboard())


# 4. Відповідь адміністратора через Reply на картку звернення
@support_router.message(F.from_user.id == ADMIN_ID)
async def admin_reply_handler(message: Message, bot):
  # Перевіряємо, чи адміністратор зробив «реплай» (відповідь) на повідомлення бота
  if message.reply_to_message and message.reply_to_message.text:
    target_text = message.reply_to_message.text

    # Шукаємо ID користувача за допомогою регулярного виразу всередині тексту картки
    match = re.search(r"ID:\s*(\d+)", target_text)

    if match:
      user_id = int(match.group(1))

      try:
        # Відправляємо відповідь користувачу від імені бота
        await bot.send_message(
            chat_id=user_id,
            text=(
                "<b>💬 Відповідь від служби підтримки BotStudio:</b>\n\n"
                f"{message.text}"
            ),
            parse_mode="HTML",
        )
        await message.answer("✅ Відповідь успішно надіслано користувачу!")
      except Exception as e:
        await message.answer(f"❌ Не вдалося надіслати: {e}")
    else:
      await message.answer(
          "⚠️ Не вдалося знайти ID користувача в повідомленні, на яке ви"
          " відповіли."
      )