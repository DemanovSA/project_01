import random

# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

# my_favorite_songs = [
#     ['Waste a Moment', 3.03],
#     ['New Salvation', 4.02],
#     ['Staying\' Alive', 3.40],
#     ['Out of Touch', 3.03],
#     ['A Sorta Fairytale', 5.28],
#     ['Easy', 4.15],
#     ['Beautiful Day', 4.04],
#     ['Nowhere to Run', 2.58],
#     ['In This World', 4.02],
# ]
# threesongs = random.sample(my_favorite_songs, 3)
# ans = threesongs[0][1] + threesongs[1][1] + threesongs[2][1]
# print(threesongs)
# print(f'Три песни звучат {ans} минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# my_favorite_songs_list = list(my_favorite_songs_dict.items())
# threesongs = random.sample(my_favorite_songs_list, 3)
# ans = threesongs[0][1] + threesongs[1][1] + threesongs[2][1]
# print(threesongs)
# print(f'Три песни звучат {round(ans, 2)} минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# threesongs = random.sample(my_favorite_songs, 1)
# ans = threesongs[0][1]
# print(*threesongs)
# print(f'Случайная песня звучит {ans} минут')

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

import datetime
my_favorite_songs_list = list(my_favorite_songs_dict.items())
threesongs = random.sample(my_favorite_songs_list, 3)
ans = threesongs[0][1] + threesongs[1][1] + threesongs[2][1]
hour = int(ans/60)
minutes = int(ans)
seconds = round(((ans)-int(ans))*60)
print(threesongs)
print(f'Три песни звучат {round(ans, 2)} минут')
print(datetime.time(hour, minutes, seconds).strftime('%H:%M:%S'))
print(datetime.time(hour, minutes, seconds).strftime('%M:%S'))
print(datetime.time(hour, minutes, seconds).strftime('%M минут %S секунд'))

# Супер
# у меня был следующий вариант решения задачи (на примере списка)
from datetime import timedelta
from math import modf
from random import random

total_time = timedelta()

for song in sample(my_favorite_songs, 3):
    s, m = modf(song[1])
    total_time += timedelta(minutes=int(m), seconds=int(s * 100))

print(f'Три песни звучат {total_time} минут')
