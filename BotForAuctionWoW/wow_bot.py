from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, CallbackContext
import json
from telegram import Update
import logging
import aiohttp

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

bot_token = '6300969863:AAHLEuZRlc7lHF3e6Qc6eUmm52xnmgEi7QQ'

api_url = 'http://127.0.0.1:8000/search_item/'


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Вітаю тебе у тестовому аукціонному боті "
                                                                          "World of Warcraft! Я все ще находжусь у "
                                                                          "розробці, проте ти вже можеш скористатися "
                                                                          "функцією /search_item, яка продемонструє "
                                                                          "тобі предмет за назвою, його ціну, дату коли"
                                                                          " його виставляли та сервер, на якому був цей"
                                                                          " лот! \n\nWelcome to the World of Warcraft "
                                                                          "test auction bot! I'm still under "
                                                                          "development, but you can already use the "
                                                                          "/search_item feature to see item by its "
                                                                          "name, price, listing date, and server!")


async def search_item(update: Update, context: CallbackContext) -> None:
    item_name = " ".join(context.args)
    print('item_name', item_name)
    if not item_name:
        message = "Необхідно вказати назву предмета через пробіл після команди /search_item. \n\nThe item name must " \
                  "be specified after /search_item and a space. "
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return
    data = {'item_name': item_name}
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(api_url, data=json.dumps(data), headers={'Content-Type': 'application/json'}) as \
                    response:
                results = await response.json()
            if 'results' in results:
                items = results['results']
                if items:
                    message = "Лоти з наступною\The lots with the specified name:\n"
                    for item in items:
                        item_info = f"Назва: {item['name']}, \nЦіна: {item['price']}, \nКількість предметів в одному " \
                                    f"лоті: {item['quantity']}, \nДата та час добавлення: {item['datetime']}, \n" \
                                    f"Сервер: {item['server']} \n____"
                        message += "\n" + item_info
                else:
                    message = "Предмет з такою назвою не знайдено. \n\nThe item with such name was not found."
            else:
                message = "Предмет з такою назвою не знайдено. \n\nThe item with such name was not found."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        except Exception as e:
            logging.error(f"Помилка під час виконання запиту пошуку предмета: {e}")
            message = "Сталася помилка під час виконання запиту пошуку предмета. Будь ласка, спробуйте ще раз " \
                      "пізніше. \n\nAn error occurred while executing the item search request. Please try again later."
            await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


if __name__ == '__main__':
    updater = ApplicationBuilder().token(token=bot_token).build()
    start_handler = CommandHandler('start', start)
    search_items_handler = CommandHandler('search_item', search_item)
    updater.add_handler(start_handler)
    updater.add_handler(search_items_handler)
    updater.run_polling()


