# -*- coding: utf-8 -*-
# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
# части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.
#
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

from random import randint

MIN = 0
MAX = 99


def find_median(array):
    def gnome_sort(array):
        n1 = 1
        n2 = 2
        while n1 < len(array):
            if array[n1 - 1] < array[n1]:
                n1 = n2
                n2 += 1
            else:
                array[n1 - 1], array[n1] = array[n1], array[n1 - 1]
                n1 -= 1
                if n1 == 0:
                    n1 = n2
                    n2 += 1
        return array

    mid = len(array) // 2
    sorted_array = gnome_sort(array)
    median = sorted_array[mid]
    return median


def find_median_wo_sort(array):
    if len(array) > 1:
        for i in array:
            less_i = 0
            more_i = 0
            for n in array:
                if n < i:
                    less_i += 1
                elif n > i:
                    more_i += 1
                else:
                    less_i += 1
                    more_i += 1
            if less_i == more_i:
                return i
    else:
        return array[0]


m = randint(0, 10)
array_len = 2 * m + 1
init_array = [randint(MIN, MAX) for _ in range(array_len)]

print(
    f'm = {m}\nИсходный массив: {init_array}'
    f'\nМедиана: {find_median(init_array)}, '
    f'\nМедиана (без сортировки): {find_median_wo_sort(init_array)}')
