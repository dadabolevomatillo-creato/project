import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

TOKEN = "8902859945:AAHrLu47t8y4QFjKSlyuIjWavo3cxGkqsbg"

bot = Bot(token=TOKEN)
dp = Dispatcher()


class RegisterState(StatesGroup):
    name = State()
    surname = State()
    phone = State()
    age = State()
    kours = State()




@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum!\n"
        "Ro'yxatdan o'tish uchun /register ni bosing."
    )


@dp.message(Command("register"))
async def start_register(message: Message, state: FSMContext):
    await state.set_state(RegisterState.name)
    await message.answer("Ismingizni kiriting:")


@dp.message(RegisterState.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegisterState.phone)
    await message.answer("Telefon raqamingizni kiriting:")


@dp.message(RegisterState.phone)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(RegisterState.age)
    await message.answer("Yoshingizni kiriting:")


@dp.message(RegisterState.age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    data = await state.get_data()

    await message.answer(
        "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!\n\n"
        f"Ism: {data['name']}\n"
        f"Telefon: {data['phone']}\n"
        f"Yosh: {data['age']}"
    )
