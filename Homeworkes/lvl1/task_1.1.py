# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# Узнаем какие есть методы у списков
# from pprint import pprint
# pprint(dir(my_favorite_songs))
newplaylist = my_favorite_songs.split(', ')
print(newplaylist[0], newplaylist[4], newplaylist[1], newplaylist[3])

# Отлично!
# Без нареканий
