from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from keyb import faq_keyboadr, back_faq

faq_router = Router()


@faq_router.message(F.text =="❓ Поширені питання")
async def faq_start(message:Message):
    await message.answer("Оберіть питання, яке вас цікавить: 👇", reply_markup=faq_keyboadr())

@faq_router.callback_query(F.data == "howmany_time")
async def how_time(call:CallbackQuery):
    await call.message.edit_text(
        "У середньому простий бот-візитка або портфоліо розробляється від "
        "<b>2 до 5 днів</b>.\n\nБільш складні проєкти — від тижня і більше, залежно від ТЗ.", reply_markup=back_faq(),
        parse_mode="HTML"
    )
    await call.answer()

@faq_router.callback_query(F.data == "howmany_money")
async def howmany_money(call:CallbackQuery):
    await call.message.edit_text(
        "Вартість залежить від функціоналу. Прості демо-боти чи портфоліо мають фіксовану ціну.\n\n"
        "Повноцінні бізнес-боти розраховуються індивідуально після обговорення деталей.",reply_markup=back_faq()
    )
    await call.answer()

@faq_router.callback_query(F.data == "which_tehnology")
async def which_tehnology(call:CallbackQuery):
    await call.message.edit_text(
        "Проєкти пишуться мовою <b>Python</b> з використанням сучасної та швидкої "
        "асинхронної бібліотеки <b>aiogram 3</b>.\n\nЦе гарантує стабільну та високошвидкісну роботу.",reply_markup=back_faq(),
        parse_mode = "HTML"
        
    )
    await call.answer()

@faq_router.callback_query(F.data == "how_orden")
async def how_orden(call:CallbackQuery):
    await call.message.edit_text(
        "Натисніть кнопку <b>📝 Залишити заявку (ТЗ)</b> у головному меню, щоб залишити заявку.\n\n"
        "Ви зможете поставити будь-які запитання або описати свою ідею безпосередньо через бота.", reply_markup=back_faq(),
        parse_mode = "HTML"
    )
    await call.answer()

@faq_router.callback_query(F.data == "have_support")
async def have_support(call:CallbackQuery):
    await call.message.edit_text(
    "Так, звісно! Після передачі бота ви отримуєте допомогу з первинним налаштуванням, хостингом та гарантійну підтримку.\n\n"
        "Якщо виникнуть питання — просто скористайтеся кнопкою <b>📩 Підтримка</b>.",reply_markup=back_faq(),
        parse_mode = "HTML")
    await call.answer()


@faq_router.callback_query(F.data == "back_to_faq")
async def back_to_faq_handler(call: CallbackQuery):
  await call.message.edit_text(
      "Оберіть питання, яке вас цікавить: 👇", reply_markup=faq_keyboadr()
  )
  await call.answer()