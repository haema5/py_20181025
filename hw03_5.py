# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.

from random import randint

ARRAY_LEN = 10

array = []
for _ in range(ARRAY_LEN):
    array.append(randint(-100, 100))

print(f'Исходный массив: {array}')

min_el = array[0]
for i in array:
    if i < min_el:
        min_el = i

if min_el < 0:
    max_el = min_el
    for i in array:
        if max_el < i < 0:
            max_el = i
    print(f'Максимальный отрицательный элемент: {max}, его позиция в массиве: {array.index(max)}.')
else:
    print(f'В массиве нет отрицательных элементов.')
