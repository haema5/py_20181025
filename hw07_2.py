# -*- coding: utf-8 -*-
# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.
from random import uniform

MIN = 0
MAX = 50
ARRAY_LEN = 10


def merge_sort(array):
    if len(array) > 1:
        splitter = len(array) // 2
        left_half = array[:splitter]
        right_half = array[splitter:]

        merge_sort(left_half)
        merge_sort(right_half)

        n = 0
        n1 = 0
        n2 = 0
        while n1 < len(left_half) and n2 < len(right_half):
            if left_half[n1] < right_half[n2]:
                array[n] = left_half[n1]
                n1 += 1
            else:
                array[n] = right_half[n2]
                n2 += 1
            n += 1

        while n1 < len(left_half):
            array[n] = left_half[n1]
            n1 += 1
            n += 1

        while n2 < len(right_half):
            array[n] = right_half[n2]
            n2 += 1
            n += 1

    return array


init_array = [uniform(MIN, MAX) for spam in range(ARRAY_LEN) if spam < MAX]
print(f'Исходный массив:\n\t{init_array} \nОтсортированный массив:\n\t{merge_sort(init_array)}')
