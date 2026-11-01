from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from keyb import bot_zapysy_choose, choose_service, inter_user, share_number, roboty_keyboard, main_keyboard, time_keyboard, inter_admin
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


manik_router = Router()

user_bookings = { }

class Zapys(StatesGroup):
  waiting_service = State()
  waiting_data = State()
  waiting_time = State()
  waiting_number = State()
  waiting_name = State()


@manik_router.message(F.text == "📂 Приклади робіт")
async def for_exeple(message:Message):
    await message.answer("Оберіть тип бота:",reply_markup=roboty_keyboard())


@manik_router.message(F.text == "Бот для запису")
async def menu(message: Message):
    await message.answer("Оберіть вид", reply_markup=bot_zapysy_choose())


@manik_router.message(F.text == "Інтерфейс для користувача")
async def start_user(message: Message):
  await message.answer("Оберіть дію:", reply_markup=inter_user())





@manik_router.message(F.text == "Записатись")
async def start_zapys(message: Message, state: FSMContext):
  await message.answer(
      "Вітаю у салоні [НАЗВА САЛОНА], оберіть послугу:",
      reply_markup=choose_service(),
  )
  await state.set_state(Zapys.waiting_service)


@manik_router.message(Zapys.waiting_service)
async def waiting_service(message: Message, state: FSMContext):
  await state.update_data(service=message.text)
  await message.answer("Оберіть дату:")
  await state.set_state(Zapys.waiting_data)


@manik_router.message(Zapys.waiting_data)
async def waiting_data(message: Message, state: FSMContext):
  await state.update_data(date = message.text)
  await message.answer("Оберіть час:", reply_markup=time_keyboard())
  await state.set_state(Zapys.waiting_time)


@manik_router.message(Zapys.waiting_time)
async def waiting_time(message: Message, state: FSMContext):
  await state.update_data(time=message.text)
  await message.answer(
      "Задля того щоб з вами звʼязався адміністратор, поділіться своїм номером",
      reply_markup=share_number(),
  )
  await state.set_state(Zapys.waiting_number)


@manik_router.message(Zapys.waiting_number, F.contact)
async def waiting_number(message: Message, state: FSMContext):
  phone_number = message.contact.phone_number
  await state.update_data(number=phone_number)

  await message.answer(
      "Введіть своє імʼя:", reply_markup=ReplyKeyboardRemove()
  )
  await state.set_state(Zapys.waiting_name)


@manik_router.message(Zapys.waiting_name)
async def waiting_name(message: Message, state: FSMContext):
  await state.update_data(name=message.text)

  user_data = await state.get_data()

  service = user_data.get("service")
  data = user_data.get("date")
  time = user_data.get("time")
  number = user_data.get("number")
  name = user_data.get("name")


  user_bookings[message.from_user.id] = {
    "service": service,
    "data": data,
    "time": time,
    "name": name,
    "number": number,
}

  await message.answer(
      f"Чудово, реєстрація завершена!\n\n"
      f"💅 Послуга: {service}\n"
      f"📅 Дата: {data}\n"
      f"⏰ Час: {time}\n"
      f"👤 Ім'я: {name}\n"
      f"📞 Телефон: {number}\n\n"
      f"Ми повідомимо адміністраторів!",
      reply_markup=inter_user()
  )


  await state.clear()


@manik_router.message(F.text == "Мої записи")
async def my_zapys(message:Message):
  user_id = message.from_user.id
  if user_id in user_bookings:
    booking = user_bookings[  
        user_id
    ]  # Дістаємо словник з даними цього користувача
    await message.answer(
        f"Ваш поточний запис!\n\n"
        f"💅 Послуга: {booking['service']}\n"
        f"📅 Дата: {booking['data']}\n"
        f"⏰ Час: {booking['time']}\n"
        f"👤 Ім'я: {booking['name']}\n"
        f"📞 Телефон: {booking['number']}\n\n"
        f"Вам прийде нагадування за день до запису"
    )
  else:
    await message.answer("Наразі у вас немає активних записів.")



@manik_router.message(F.text == "Повернутись у головне меню")
async def backtomenu(message:Message):
    await message.answer("Повертаємось у головне меню", reply_markup=main_keyboard())

@manik_router.message(F.text == "Назад")
async def backtomenu(message:Message, state:FSMContext):
    await state.clear()
    await message.answer("Повертаємось у головне меню", reply_markup=inter_user())





@manik_router.message(F.text == "Інтерфейс для адміна")
async def show_admin_interface(message: Message):
  # Створюємо інлайн-кнопку зв'язку з клієнтом (в даному випадку з тим, хто тестує)
  client_id = message.from_user.id

  keyboard = InlineKeyboardMarkup(
      inline_keyboard=[[
          InlineKeyboardButton(
              text="💬 Написати клієнту", url=f"tg://user?id={client_id}"
          )
      ]]
  )

  await message.answer(
      "📊 **Демо-панель адміністратора**\n\n"
      "Ось як адмін бачить активні записи:\n\n"
      "1️⃣ **Запис #101**\n"
      "• **Послуга:** Манікюр (Комплекс)\n"
      "• **Дата та час:** Завтра о 14:00\n"
      f"• **Клієнт:** {message.from_user.full_name}\n\n"
      "👇 Натисніть кнопку нижче, щоб перевірити функцію зв'язку:",
      reply_markup=keyboard,
      parse_mode="Markdown",
  )