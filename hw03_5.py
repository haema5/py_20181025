# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.

from random import randint

ARRAY_LEN = 10

array = []
for _ in range(ARRAY_LEN):
    array.append(randint(-100, 100))

print(f'Исходный массив: {array}')

min = array[0]
for i in array:
    if i < min:
        min = i

if min < 0:
    max = min
    for i in array:
        if max < i < 0:
            max = i
    print(f'Максимальный отрицательный элемент: {max}, его позиция в массиве: {array.index(max)}.')
else:
    print(f'В массиве нет отрицательных элементов.')
