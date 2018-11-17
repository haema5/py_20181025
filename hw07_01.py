# -*- coding: utf-8 -*-
# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Вывести на экран исходный
# и отсортированный массивы.
import random


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


arr = [random.randint(-100, 99) for _ in range(10)]
print(f'Исходный массив:\n\t{arr} \nОтсортированный массив:\n\t{bubble_sort(arr)}')
