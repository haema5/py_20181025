# В одномерном массиве найти сумму элементов, находящихся между минимальным
# и максимальным элементами. Сами минимальный и максимальный элементы в сумму
# не включать.

from random import randint

ARRAY_LEN = 10

array = []
for _ in range(ARRAY_LEN):
    array.append(randint(-100, 100))

print(f'Исходный массив: {array}')

min_pos = 0
max_pos = 0
for i in range(1, len(array)):
    if array[i] < array[min_pos]:
        min_pos = i
    elif array[i] > array[max_pos]:
        max_pos = i

if min_pos > max_pos:
    min_pos, max_pos = max_pos, min_pos

summa = 0
for i in range(min_pos + 1, max_pos):
    summa += array[i]

print(f'Сумма элементов: {summa}')
