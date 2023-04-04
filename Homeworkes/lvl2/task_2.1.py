# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

arr = [4,6,2,1,9,63,-134,566]
arr1 = [-52, 56, 30, 29, -54, 0, -110]
arr2 = [42, 54, 65, 87, 0]
arr3 = [5]
def minimum(arr):
    minarr = arr[0]
    for i in range(len(arr)):
        if arr[i] < minarr:
            minarr = arr[i]
    return(minarr)

def maximum(arr):
    maxarr = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxarr:
            maxarr = arr[i]
    return(maxarr)

print(f'{arr}   -> min = {minimum(arr)}, max = {maximum(arr)}')
print(f'{arr1}  -> min = {minimum(arr1)}, max = {maximum(arr1)}')
print(f'{arr2}\t\t -> min = {minimum(arr2)}, \t max = {maximum(arr2)}')
print(f'{arr3}\t\t\t\t -> min = {minimum(arr3)}, \t max = {maximum(arr3)}')

# Хорошо) можно например использовать быструю сортировку
def quicksort(arr):
    if len(arr) < 2:
        # базовый случай, массив с 0 или 1 элементом уже отсортирован
        return arr
    else:
        # рекурсивный случай. выберем опорный элемент pivot
        pivot = arr[0]
        # подмассив всех элементов, меньших, чем опорный элемент pivot
        less = [i for i in arr[1:] if i <= pivot]
        # подмассив всех элементов, превышающих опорный элемент pivot
        greater = [i for i in arr[1:] if i > pivot]
        # обединяем в порядке "сортировка для меньшего подмассива – опорный элемент – сортировка для большего подмассив"
        return quicksort(less) + [pivot] + quicksort(greater)

# Максимум - это последний элемент отсортированного списка
def maximum(arr):
    return quicksort(arr)[-1]

 # Минимум - это первый элемент отсортированного списка
def minimum(arr):
    return quicksort(arr)[0]
print('\nБыстрая сортировка')
print('min =', minimum([4,6,2,1,9,63,-134,566]))
print('max =', maximum([4,6,2,1,9,63,-134,566]))
