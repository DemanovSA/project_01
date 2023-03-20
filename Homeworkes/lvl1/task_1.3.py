# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

numbermonth = int(input('Введите номер месяца:  '))
if numbermonth < 1 or numbermonth > 12:
    print('Нет такого месяца')
else:
    namemonth = datetime.date(2023, numbermonth, 1).strftime('%B')
    if int(numbermonth) == 2:
        days_in_month = 28
        print(f'Вы ввели {namemonth.lower()}. {days_in_month} дней')
    elif int(numbermonth) == 4 or int(numbermonth) == 6 or int(numbermonth) == 9 or int(numbermonth) == 11:
        days_in_month = 30
        print(f'Вы ввели {namemonth.lower()}. {days_in_month} дней')
    else:
        days_in_month = 31
        print(f'Вы ввели {namemonth.lower()}. {days_in_month} день')
        
# Ну можно было и без datetime) но все ок)
