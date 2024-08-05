import asyncio
from asyncio import sleep
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram import Router
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.enums import ParseMode
from aiogram.types import LinkPreviewOptions

router: Router = Router()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = ''
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

async def main():
    await dp.start_polling(bot)

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!\n" "<b>Разыграем сеанс массажа?</b>!", parse_mode=ParseMode.HTML)
    await sleep(1)
    await message.answer("Жду вариант ответа:\n" "да или нет")

@router.message(F.text.lower() == "нет")
async def cmd_not(message: types.Message):
    await message.reply("<b>Плохой выбор...</b>", parse_mode=ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove())
    await message.answer("<b>До новых встреч!<b>", parse_mode=ParseMode.HTML)

@router.message(F.text.lower() == "да")
async def cmd_yes(message: types.Message):
    await message.reply("<b>Отличный выбор!!!</b>", parse_mode=ParseMode.HTML, reply_markup=types.ReplyKeyboardRemove())
    await message.answer("Чтобы продолжить напиши команду: /schitalka")

@router.message(Command("schitalka"))
async def schitalka(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="эники",callback_data="s~1"))
    builder.add(types.InlineKeyboardButton(text="бэники",callback_data="s~2"))
    builder.add(types.InlineKeyboardButton(text="ели",callback_data="s~3"))
    builder.add(types.InlineKeyboardButton( text="вареники",callback_data="s~4"))
    await message.answer('Выбери и нажми на одну из кнопок!', reply_markup=builder.as_markup())

@router.callback_query(F.data)
async def x_random_value(callback: types.CallbackQuery):
    data = callback.data.split('~')[1]
    if data == '1': return await callback.message.answer('Вы выиграли парный массаж!\n'
    'Чтобы продолжить напишите в формате: /inf номер телефона имя')
    if data == '2': return await callback.message.answer('Вы выиграли массаж всего тела!\n'
    'Чтобы продолжить напишите в формате: /inf номер телефона имя')
    if data == '3': return await callback.message.answer('Вы выиграли скидку 50% на любой вид массажа!\n'
    'Чтобы продолжить напишите в формате: /inf номер телефона имя')
    if data == '4': return await callback.message.answer('Вы выиграли массаж спины!\n' 
    'Чтобы продолжить напишите в формате: /inf <номер телефона> <имя>')

@router.message(Command("inf"))
async def cmd_set(message: types.Message, command):
    if command.args is None:
        await message.answer("Ошибка: неправильный формат команды!")
        return
    try:
        number, name = command.args.split(" ", maxsplit=1)
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/inf +3753345757 Иван"
        )
        return
    await message.answer(
        "Ваши данные:\n"
        f"номер телефона: {number}\n"
        f"имя: {name}"
    )
    await message.answer("В ближайшее время мы с Вами свяжемся\n""<b>Спасибо за уделенное время!</b>!", parse_mode=ParseMode.HTML)
    await sleep(3)
    await message.answer("Если хотите ознакомится с салоном и записаться самостоятельно перейдите по комманде: /link")
    await message.answer("<b>До новых встреч!<b>", parse_mode=ParseMode.HTML)

@router.message(Command("link"))
async def cmd_link(message: types.Message):
    l_text = (
        "https://dikidi.ru/1636053?p=0.pi\n"
        "https://n423614.yclients.com/company/401067/personal/menu?o=m-1"
    )
    options_4 = LinkPreviewOptions(
        url="https://kstudio.by/?fbclid=PAZXh0bgNhZW0CMTEAAaZl4diuB1GTt_eeSbuDcLz_kmjzWfIu_7XC69WQ0u_ECIHjIqzQCgtoUsc_aem_uz94wqUX8f-ooNkFL8H6kw",
        prefer_small_media=True, show_above_text=True
    )
    await message.answer(f"Ссылки для записи:\n{l_text}", link_preview_options=options_4)

@router.message()
async def cmd_v(message: types.Message):
    await message.reply("Посмотри внимательно как нужно ответить!")

if __name__ == "__main__":
    asyncio.run(main())