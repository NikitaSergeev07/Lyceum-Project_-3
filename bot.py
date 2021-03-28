# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram.ext import CommandHandler
import sqlite3
from telegram import ReplyKeyboardMarkup

reply_keyboard = [['/help', '/delete', '/start']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def start(update, context):
    update.message.reply_text(
        "Привет хозяин! Я предназначен для уведомления о проблемах в веб приложении - барахолка.рф",
        reply_markup=markup)


def help(update, context):
    con = sqlite3.connect("db/blogs.db")

    # Создание курсора
    cur = con.cursor()

    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT * FROM contact""").fetchall()
    if result:
        update.message.reply_text('Поступили новые сообщения о проблемах\n')
        for elem in result:
            update.message.reply_text(f'Username - {elem[1]}\n'
                  f'Email - {elem[2]}\n'
                  f'Message - {elem[3]}',
                    reply_markup=markup)
    else:
        update.message.reply_text('Новых сообщений о проблемах не поступало')
    con.commit()
    con.close()

def delete(update, context):
    con = sqlite3.connect("db/blogs.db")

    # Создание курсора
    cur = con.cursor()

    cur.execute("""DELETE FROM contact""").fetchall()
    update.message.reply_text('Очистка прошла успешно!',
                              reply_markup=markup)
    con.commit()
    con.close()

def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater("1770974631:AAGVtOfujSLRF_oj71o7nk4I37G5dBLeIXg", use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("delete", delete))
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()