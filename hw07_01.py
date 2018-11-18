# -*- coding: utf-8 -*-
# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный
# и отсортированный массивы.
from random import randint

MIN = -100
MAX = 99
ARRAY_LEN = 10


def bubble_sort(array):
    n = 1
    trigger = True
    while trigger:
        trigger = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                trigger = True
        n += 1
    return array


init_array = [randint(MIN, MAX) for _ in range(ARRAY_LEN)]
print(f'Исходный массив:\n\t{init_array} \nОтсортированный массив:\n\t{bubble_sort(init_array)}')
