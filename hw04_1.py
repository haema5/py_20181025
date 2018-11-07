# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
#
# 1 ( hw03_2 )
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй
# массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если
# индексация начинается с нуля), т.к. именно в этих позициях первого
# массива стоят четные числа.

import cProfile
from random import randint


def s_even(array_len):
    array = [randint(-100, 100) for _ in range(array_len)]

    evens = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            evens.append(i)

    return array, evens


# cProfile.run('s_even(100)')
# 1    0.000    0.000    0.000    0.000 hw04_1.py:16(s_even)
# cProfile.run('s_even(1000)')
# 1    0.000    0.000    0.003    0.003 hw04_1.py:16(s_even)
# cProfile.run('s_even(10000)')
# 1    0.002    0.002    0.029    0.029 hw04_1.py:16(s_even)
#
# "hw04_1.s_even(100)"
# 100 loops, best of 5: 199 usec per loop
# "hw04_1.s_even(1000)"
# 100 loops, best of 5: 1.91 msec per loop
# "hw04_1.s_even(10000)"
# 100 loops, best of 5: 19.6 msec per loop


# 2 ( hw03_3 - Первый способ)
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def min_max(array_len):
    array = [randint(0, 99) for _ in range(array_len)]

    min_pos = 0
    max_pos = 0
    for i in range(1, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
        elif array[i] > array[max_pos]:
            max_pos = i

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array


# cProfile.run('min_max(100)')
# 1    0.000    0.000    0.000    0.000 hw04_1.py:45(min_max)
# cProfile.run('min_max(1000)')
# 1    0.000    0.000    0.003    0.003 hw04_1.py:45(min_max)
# cProfile.run('min_max(10000)')
# 1    0.002    0.002    0.028    0.028 hw04_1.py:45(min_max)

# "hw04_1.min_max(100)"
# 100 loops, best of 5: 188 usec per loop
# "hw04_1.min_max(1000)"
# 100 loops, best of 5: 1.94 msec per loop
# "hw04_1.min_max(10000)"
# 100 loops, best of 5: 19.6 msec per loop


# 2 ( hw03_3 - Второй способ)
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

def min_max_inc(array_len):
    array = [randint(0, 99) for _ in range(array_len)]

    min_pos = array.index(min(array))
    max_pos = array.index(max(array))

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array

# cProfile.run('min_max_inc(100)')
# 1    0.000    0.000    0.000    0.000 hw04_1.py:75(min_max_inc)
# cProfile.run('min_max_inc(1000)')
# 1    0.000    0.000    0.003    0.003 hw04_1.py:75(min_max_inc)
# cProfile.run('min_max_inc(10000)')
# 1    0.000    0.000    0.027    0.027 hw04_1.py:75(min_max_inc)

# "hw04_1.min_max_inc(100)"
# 100 loops, best of 5: 182 usec per loop
# "hw04_1.min_max_inc(1000)"
# 100 loops, best of 5: 1.76 msec per loop
# "hw04_1.min_max_inc(10000)"
# 100 loops, best of 5: 18 msec per loop

#