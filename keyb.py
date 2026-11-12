from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup



def main_keyboard():
  return ReplyKeyboardMarkup(
      keyboard=[
          [
              KeyboardButton(text="📝 Залишити заявку (ТЗ)"),
              KeyboardButton(text="📂 Приклади робіт"),
          ],
          [
              KeyboardButton(text="💰 Розрахувати вартість"),
              KeyboardButton(text="❓ Поширені питання"),
          ],
          [
            KeyboardButton(text = "📩 Підтримка")],
      ],
      resize_keyboard=True,
  )



def admin_main_keyboard():
  return ReplyKeyboardMarkup(
      keyboard=[
          [
              KeyboardButton(text="📝 Залишити заявку (ТЗ)"),
              KeyboardButton(text="📂 Приклади робіт"),
          ],
          [
              KeyboardButton(text="💰 Розрахувати вартість"),
              KeyboardButton(text="❓ Поширені питання"),
          ],
          [ KeyboardButton(text = "📩 Підтримка"), 
            KeyboardButton(text="🔐 Адмін-панель"),
         ],
      ],
      resize_keyboard=True,
  )



def roboty_keyboard():
  return ReplyKeyboardMarkup(
      keyboard=[
          [KeyboardButton(text="Бот для запису")],
          [KeyboardButton(text="Повернутись у головне меню")],
      ],
      resize_keyboard=True,
      one_time_keyboard=True,
  )


def bot_zapysy_choose():
  return ReplyKeyboardMarkup(
      keyboard=[
          [KeyboardButton(text="Інтерфейс для користувача")],
          [KeyboardButton(text="Інтерфейс для адміна")],  
          [KeyboardButton(text="Повернутись у головне меню")],
      ],
      resize_keyboard=True,
      one_time_keyboard=True,
  )


def inter_user():
  return ReplyKeyboardMarkup(
      keyboard=[
          [KeyboardButton(text="Записатись")],  
          [KeyboardButton(text="Мої записи")],
          [KeyboardButton(text="Повернутись у головне меню")],
      ],
      resize_keyboard=True,
      one_time_keyboard=True,
  )


def choose_service():
  return ReplyKeyboardMarkup(
      keyboard=[
          [KeyboardButton(text="Манікюр")],
          [KeyboardButton(text="Педикюр")],
          [KeyboardButton(text="Назад")],
      ],
      resize_keyboard=True,
      one_time_keyboard=True,
  )


def share_number():
  return ReplyKeyboardMarkup(
      keyboard=[
          [
              KeyboardButton(
                  text="📱 Поділитися номером", request_contact=True
              )
          ]
      ],
      resize_keyboard=True,
      one_time_keyboard=True,
  )


def time_keyboard():
    return ReplyKeyboardMarkup(
      keyboard = [
        [KeyboardButton(text = "09:00"),
        KeyboardButton(text = "10:00"),
        KeyboardButton(text = "11:00"),
        KeyboardButton(text = "12:00"),
        KeyboardButton(text = "13:00")],
        [KeyboardButton(text = "14:00"),
        KeyboardButton(text = "15:00"),
        KeyboardButton(text = "16:00"),
        KeyboardButton(text = "17:00"),
        KeyboardButton(text = "18:00")],


      ],
      resize_keyboard=True,
      one_time_keyboard=True,
    )



def inter_admin():
    return ReplyKeyboardMarkup(
       keyboard= [
          [KeyboardButton(text="Активні записи")],
          [KeyboardButton(text="Звʼязок з клієнтом")]
       ]
    )




def faq_keyboadr():
   return InlineKeyboardMarkup(
      inline_keyboard= [
         [InlineKeyboardButton(text = "⏱ Скільки часу займає розробка бота?", callback_data="howmany_time")],
         [InlineKeyboardButton(text = "💰 Скільки коштує створення Telegram-бота?", callback_data="howmany_money")],
         [InlineKeyboardButton(text = "🛠 Які технології ви використовуєте?", callback_data="which_tehnology")],
         [InlineKeyboardButton(text = "📝 Як замовити власного бота?", callback_data="how_orden")],
         [InlineKeyboardButton(text = "🤝 Чи є підтримка після запуску?", callback_data="have_support")],
      ]
   )
def back_faq():
    return InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(
            text="⬅️ Назад до питань", callback_data="back_to_faq"
        )
    ]]
)

def cancel():
   return ReplyKeyboardMarkup(
      keyboard= [
         [KeyboardButton(text = "Повернутись")],
      ],
      resize_keyboard= True
   )


def cancel_keyboard():
      return ReplyKeyboardMarkup(
      keyboard=[[KeyboardButton(text="❌ Скасувати")]],
      resize_keyboard=True,
  )




def service_keyboard():
  return InlineKeyboardMarkup(
      inline_keyboard=[
          [InlineKeyboardButton(text="🛒 Інтернет-магазин", callback_data="inter"), ],
          [InlineKeyboardButton(text="📅 Бот для запису",callback_data="zapys")],
          [InlineKeyboardButton(text="❌ Скасувати", callback_data="back")],
      ],
      resize_keyboard=True,
  )


def design_keyboard():
  return InlineKeyboardMarkup(
      inline_keyboard=[
          [InlineKeyboardButton(text="✨ Стандартний дизайн", callback_data="standart")],
          [InlineKeyboardButton(text="🎨 Індивідуальний унікальний дизайн", callback_data="indiv")],
          [InlineKeyboardButton(text="❌ Скасувати", callback_data="back")],
      ],
      resize_keyboard=True,
  )



def admin_panel():
   return ReplyKeyboardMarkup(
      keyboard= [ 
        [KeyboardButton(text="Усі користувачі")],
        [KeyboardButton(text="У головне меню")],
      ]
   )