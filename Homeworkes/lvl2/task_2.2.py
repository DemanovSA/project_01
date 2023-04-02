# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')

month = int(input('Введите номер месяца:  '))
def quarter_of(month):
    while month > 12 or month < 1:
        print('Такого месяца не существует')
        month = int(input('Введите номер месяца '))
    namemonth = datetime.date(2023, month, 1).strftime('%B')
    if month >= 1 and month <= 3:
        return(f'{month} ({namemonth.lower()}) является частью первого квартала;')
    elif month >= 4 and month <= 6:
        return(f'{month} ({namemonth.lower()}) является частью второго квартала;')
    elif month >= 7 and month <= 9:
        return(f'{month} ({namemonth.lower()}) является частью третьего квартала;')
    elif month >= 10 and month <= 12:
        return(f'{month} ({namemonth.lower()}) является частью четвертого квартала;')     
print(f'месяц {quarter_of(month)}')
        



    
