# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
#
# 1
# ( hw03_2 )
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


# 2
# ( hw03_3 - Первый способ)
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


# 2
# ( hw03_3 - Второй способ)
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

# 3
# ( hw03_5 - Первый способ)
# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.


def hw03_5(arr_len):
    arr = [randint(-100, 100) for _ in range(arr_len)]
    min_el = arr[0]
    for i in arr:
        if i < min_el:
            min_el = i

    if min_el < 0:
        max_el = min_el
        for i in arr:
            if max_el < i < 0:
                max_el = i
        return max_el, arr.index(max_el)
    else:
        return 'Ошибка. В массиве нет отрицательных элементов.'


# cProfile.run('hw03_5(100000)')
# 1    0.007    0.007    0.171    0.171 hw04_1.py:8(hw03_5)
# cProfile.run('hw03_5(1000000)')
# 1    0.067    0.067    1.632    1.632 hw04_1.py:8(hw03_5)
# cProfile.run('hw03_5(10000000)')
# 1    0.670    0.670   16.003   16.003 hw04_1.py:8(hw03_5)
#
# "hw04_1.hw03_5(100000)"
# 10 loops, best of 3: 103 msec per loop
# "hw04_1.hw03_5(1000000)"
# 10 loops, best of 3: 1.06 sec per loop
# "hw04_1.hw03_5(10000000)"
# 10 loops, best of 3: 10.6 sec per loop


# ( hw03_5 - Второй способ)

def hw03_5_modify(arr_len):
    arr = [randint(-100, 100) for _ in range(arr_len)]
    new_arr = [i for i in arr if i < 0]
    if len(new_arr) > 0:
        max_el = max(new_arr)
        return max_el, arr.index(max_el)
    else:
        return 'Ошибка. В массиве нет отрицательных элементов.'

# cProfile.run('hw03_5_modify(100000)')
# 1    0.000    0.000    0.154    0.154 hw04_1.py:25(hw03_5_modify)
# cProfile.run('hw03_5_modify(1000000)')
# 1    0.000    0.000    1.589    1.589 hw04_1.py:25(hw03_5_modify)
# cProfile.run('hw03_5_modify(10000000)')
# 1    0.000    0.000   16.096   16.096 hw04_1.py:25(hw03_5_modify)
#
# "hw04_1.hw03_5_modify(100000)"
# 10 loops, best of 3: 101 msec per loop
# "hw04_1.hw03_5_modify(1000000)"
# 10 loops, best of 3: 1.05 sec per loop
# "hw04_1.hw03_5_modify(10000000)"
# 10 loops, best of 3: 10.6 sec per loop

# Вывод:
# На тестируемых объемах массивов разница не принципиальна.
