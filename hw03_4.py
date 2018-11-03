# Определить, какое число в массиве встречается чаще всего.

from random import randint

ARRAY_LEN = 10

array = []
for _ in range(ARRAY_LEN):
    array.append(randint(0, 9))

max = 0
for i in array:
    if i > max:
        max = i

sum_ar = [0] * (max + 1)
for i in array:
    sum_ar[i] += 1

max = 0
for i in sum_ar:
    if i > max:
        max = i

print(f'Исходный массив: {array}')
print(f'Чаще остальных встречается {sum_ar.index(max)}')
