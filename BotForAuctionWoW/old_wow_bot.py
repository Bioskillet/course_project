import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.http import JsonResponse
import requests
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

django_url = "http://127.0.0.1:8000/search_item/"


async def start(message: types.Message):
    text = "Вітаю тебе у тестовому аукціонному боті World of Warcraft! Я все ще находжусь у розробці, проте ти вже " \
           "можеш скористатися функцією /search_item, яка продемонструє тобі предмет за назвою, його ціну, дату коли " \
           "його виставляли та сервер, на якому був цей лот! \n\n Welcome to the World of Warcraft test auction bot! " \
           "I'm still under development, but you can already use the /search_item feature to see item by its name, " \
           "price, listing date, and server!"
    await message.reply(text)


# async def search_item(message: types.Message):
#     text = "Введіть назву шуканого предмета. \n\nEnter the name of the item you are looking for."
#     await message.reply(text)

# async def search_item(message: types.Message):
#     await message.reply("Введіть назву шуканого предмета. \n\nEnter the name of the item you are looking for.")
#     item_name = message.text.replace('/search_item', '').strip()
#     items = Item.objects.filter(name=item_name)
#     if items.exists():
#         response_message = ""
#         for item in items:
#             response_message += f"Назва: {item.name}\nЦіна: {item.price}\nКількість: {item.quantity}\nЧас: " \
#                                 f"{item.datetime}\n\n"
#     else:
#         response_message = "Немає результатів для введеної назви предмету."
#     await message.reply(response_message)

bot_token = "6300969863:AAHLEuZRlc7lHF3e6Qc6eUmm52xnmgEi7QQ"
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['search'])
async def search_command(message: types.Message):
    # Отримуємо параметри пошуку з повідомлення користувача
    search_query = message.text.split('/search ', maxsplit=1)[1]

    # Виконуємо пошукову логіку
    search_results = perform_search(search_query)

    # Відправляємо результати пошуку користувачу
    for result in search_results:
        await message.reply(result)


# Функція для виконання пошуку
def perform_search(query):
    # Ваша логіка пошуку тут
    # Наприклад, можна використати сторонню бібліотеку для пошуку даних

    # Повертаємо список результатів
    return ['Result 1', 'Result 2', 'Result 3']


# async def search_item_command(message: types.Message):
#     await message.reply("Введіть назву шуканого предмета.")
#     item_name = message.text.replace('/search_item', '').strip()
#     search_url = django_url + "search-item/?name=" + item_name
#     response = requests.get(search_url)
#     if response.status_code == 200:
#         items_data = response.json()
#         if items_data:
#             response_message = "Результати пошуку:\n\n"
#             for item in items_data:
#                 item_info = f"Назва: {item['name']}\nЦіна: {item['price']}\nКількість: {item['quantity']}\nЧас: " \
#                             f"{item['datetime']}\n\n"
#                 response_message += item_info
#         else:
#             response_message = "Немає результатів для введеної назви предмету."
#     else:
#         response_message = "Під час пошуку сталася помилка. Спробуйте ще раз пізніше."
#     await message.reply(response_message)


async def main():
    # bot_token = "6300969863:AAHLEuZRlc7lHF3e6Qc6eUmm52xnmgEi7QQ"
    # bot = Bot(token=bot_token)
    # storage = MemoryStorage()
    # dp = Dispatcher(bot, storage=storage)

    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(search_command, commands="search_item")

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())






# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
#
#
# async def search_item_handler(message: types.Message):
#     # Відправлення повідомлення з запитом назви предмету
#     await message.reply("Введіть назву шуканого предмету.\n\nEnter the name of the item you are looking for.")
#
#     # Очікування відповіді з назвою предмету
#     response = await bot.wait_for('message')
#     item_name = response.text.strip()
#
#     # Пошук предмету за назвою в таблиці Django
#     items = Item.objects.filter(name=item_name)
#
#     # Якщо знайдено відповідні записи
#     if items.exists():
#         response_message = "Результати пошуку:\n"
#         for item in items:
#             # Витягнення необхідної інформації з записів
#             item_info = f"Назва: {item.name}\nЦіна: {item.price}\nКількість: {item.quantity}\nЧас: {item.datetime}\n"
#             response_message += item_info + "\n"
#     else:
#         response_message = "Немає результатів для введеної назви предмету."
#
#     # Відправлення повідомлення з результатами назад до користувача
#     await message.reply(response_message)
#
# async def main():
#     bot_token = "6300969863:AAHLEuZRlc7lHF3e6Qc6eUmm52xnmgEi7QQ"
#     bot = Bot(token=bot_token)
#     storage = MemoryStorage()
#     dp = Dispatcher(bot, storage=storage)
#
#     dp.register_message_handler(search_item_handler, commands="search_item")
#
#     await dp.start_polling()
#
# if __name__ == '__main__':
#     asyncio.run(main())

# from django.http import JsonResponse
# async def search_item_command(message: types.Message):
#     await message.reply("Введіть назву шуканого предмета.")
#
#     item_name = message.text.replace('/search_item', '').strip()
#
#     search_url = django_url + "search-item/?name=" + item_name
#
#     # Здійснюємо GET-запит до Django сервера
#     response = requests.get(search_url)
#
#     # Отримуємо результати запиту
#     if response.status_code == 200:
#         # Якщо отримано успішний відповідь, отримуємо дані з відповіді
#         items_data = response.json()
#
#         if items_data:
#             # Якщо є дані про предмети, формуємо відповідь
#             response_message = "Результати пошуку:\n\n"
#             for item in items_data:
#                 item_info = f"Назва: {item['name']}\nЦіна: {item['price']}\nКількість: {item['quantity']}\nЧас: {item['datetime']}\n\n"
#                 response_message += item_info
#         else:
#             # Якщо немає даних про предмети
#             response_message = "Немає результатів для введеної назви предмету."
#     else:
#         # Якщо отримано невдалу відповідь
#         response_message = "Під час пошуку сталася помилка. Спробуйте ще раз пізніше."
#
#     # Відправляємо повідомлення з результатами пошуку
#     await message.reply(response_message)

   # 6300969863:AAHLEuZRlc7lHF3e6Qc6eUmm52xnmgEi7QQ
