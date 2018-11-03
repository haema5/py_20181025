# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

ARRAY_LEN = 10

array = []
for _ in range(ARRAY_LEN):
    array.append(randint(0, 99))

min_pos = 0
max_pos = 0
for i in range(1, len(array)):
    if array[i] < array[min_pos]:
        min_pos = i
    elif array[i] > array[max_pos]:
        max_pos = i

print(f'Исходный массив: {array}')

array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

print(f'Новый массив:    {array}')