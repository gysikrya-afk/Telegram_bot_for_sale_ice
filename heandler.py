from aiogram import Router,F,types
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import os

from app.kb import menu,menu_result
from app.state import Ice

load_dotenv()
ID_CHAT = os.getenv('ID')

router = Router()

@router.message(F.text == '/start')
async def start(msg):
    await msg.answer('Привет!Мы компания Ice World которая производит лёд.',reply_markup=menu)

@router.message(F.text == 'О нас')
async def about(msg):
    await msg.answer('Продаём качественный лёд.Номер телефона:.Где мы работаем:.')

@router.message(F.text == 'Виды льда')
async def ice_text(msg):
    await msg.answer(
    'Лёд обычный-15 грн/шт.Это просто обычный лёд,тоесть замороженная вода\n' \
    'Лёд для напитков-20 грн/шт.Специальный лёд для напитков если вам жарко\n' \
    'Лёд премиум-25 грн/шт.Есклюзив.Натуральный лёд(имееться ввиду сделана природой)')

@router.message(F.text == 'Заказать лёд')
async def ice_start(msg,state:FSMContext):
    await msg.answer('Для заказа льда вам будет нужно пройти регистрацию.')
    await msg.answer('Как вас зовут?')
    await state.set_state(Ice.name)

@router.message(Ice.name)
async def ice_name(msg:types.Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer('Из сообщение Виды льда выберите лёд')
    await state.set_state(Ice.ice)

@router.message(Ice.ice)
async def ice_variable(msg:types.Message,state:FSMContext):
    await state.update_data(ice=msg.text)
    await msg.answer('Какое количество льда вы хотите купить')
    await state.set_state(Ice.ice_number)

@router.message(Ice.ice_number)
async def ice_number_ice(msg:types.Message,state:FSMContext):
    await state.update_data(ice_number=msg.text)
    await msg.answer('Теперь я должен узнать откуда вы.Из какого вы города?')
    await state.set_state(Ice.city)

@router.message(Ice.city)
async def ice_city(msg:types.Message,state:FSMContext):
    await state.update_data(city=msg.text)
    await msg.answer('Какая ваша улица?')
    await state.set_state(Ice.street)

@router.message(Ice.street)
async def ice_street(msg:types.Message,state:FSMContext):
    await state.update_data(street=msg.text)
    await msg.answer('Номер вашего дома или квартиры')
    await state.set_state(Ice.house)

@router.message(Ice.house)
async def ice_name(msg:types.Message,state:FSMContext):
    await state.update_data(house=msg.text)
    await msg.answer('Хотите ввести ваш номер телефона?Если да то введите,а если нет напиши Нет')
    await state.set_state(Ice.phone)

@router.message(Ice.phone)
async def ice_name(msg:types.Message,state:FSMContext):
    await state.update_data(phone=msg.text)
    await msg.answer('Введите ваш email(Его вводить обезательно!).')
    await state.set_state(Ice.email)

@router.message(Ice.email)
async def ice_name(msg:types.Message,state:FSMContext):
    await state.update_data(email=msg.text)
    data = await state.get_data()
    name = data.get('name','Не указоно')
    ice = data.get('ice','Не указоно')
    ice_number = data.get('ice_number','Не указоно')
    city = data.get('city','Не указоно')
    street = data.get('street','Не указоно')
    house = data.get('house','Не указоно')
    phone = data.get('phone','Не указоно')
    email = data.get('email','Не указоно')
    await msg.bot.send_message(ID_CHAT,f'Имя:{name}\nВид льда:{ice}\nКоличество льда:{ice_number}\nГород:{city}\nУлица:{street}\nНомер дома(квартиры):{house}\nНомер телефона:{phone}\nEmail:{email}\nID пользователя:{msg.from_user.id}')
    await msg.answer('Спасибо за заполнение формы.',reply_markup=menu_result)

@router.message(F.text == 'Узнать мои данные')
async def my_database(msg,state:FSMContext):
    data = await state.get_data()
    name = data.get('name','Не указоно')
    ice = data.get('ice','Не указоно')
    ice_number = data.get('ice_number','Не указоно')
    city = data.get('city','Не указоно')
    street = data.get('street','Не указоно')
    house = data.get('house','Не указоно')
    phone = data.get('phone','Не указоно')
    email = data.get('email','Не указоно')
    await msg.answer(
        f'Имя:{name}\n \
        Вид льда:{ice}\n \
        Количество льда:{ice_number}\n \
        Город:{city}\n \
        Улица:{street}\n \
        Номер дома(квартиры):{house}\n \
        Номер телефона:{phone}\n \
        Email:{email}')
    
@router.message(F.text == 'Повторно написать форму')
async def ice_restart(msg,state:FSMContext):
    await state.clear()
    await ice_start(msg,state)
