# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее
# эффективным использованием памяти.

from random import randint
from sys import getsizeof

ARRAY_LEN = 10


def show_total_size(dictionary):
    def get_size(x):
        size = getsizeof(x)
        if type(x) is int:
            # print(f'Size of {x} = {size} bytes')
            pass
        elif type(x) is list:
            # print(f'Size of {x} = {size} bytes')
            for i in x:
                size_i = getsizeof(i)
                size += size_i
            #     print(f'\tSize of {i} = {size_i} bytes')
            # print(f'\tОбщий размер массива = {size} bytes')
        return size

    print('\nИспользуемые переменные: ')
    [print('\t', x, '=', dictionary[x], type(dictionary[x])) for x in dictionary]
    print()

    total_size = 0
    for x in dictionary:
        total_size += get_size(dictionary[x])
    return total_size


# 1 hw03_3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
# Первый способ:
def hw03_3(array):
    min_pos = 0
    max_pos = 0
    for i in range(1, len(array)):
        if array[i] < array[min_pos]:
            min_pos = i
        elif array[i] > array[max_pos]:
            max_pos = i

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array, show_total_size(locals())


# Второй способ:
def hw03_3_modify(array):
    min_pos = array.index(min(array))
    max_pos = array.index(max(array))

    array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

    return array, show_total_size(locals())


# 2 hw03_5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его
# значение и позицию в массиве.
# Первый способ:
def hw03_5(array):
    min_el = array[0]
    for i in array:
        if i < min_el:
            min_el = i

    if min_el < 0:
        max_el = min_el
        for i in array:
            if max_el < i < 0:
                max_el = i
        return max_el, array.index(max_el), show_total_size(locals())
    else:
        return 'Ошибка. В массиве нет отрицательных элементов.'


# Второй способ:
def hw03_5_modify(array):
    new_arr = [i for i in array if i < 0]
    if len(new_arr) > 0:
        max_el = max(new_arr)
        return max_el, array.index(max_el), show_total_size(locals())
    else:
        return 'Ошибка. В массиве нет отрицательных элементов.'


array_1 = [randint(0, 99) for _ in range(ARRAY_LEN)]
array_2 = [randint(-99, 99) for _ in range(ARRAY_LEN)]

answer = hw03_3(array_1)
print(f'Для выполнения кода потребовалось {answer[1]} bytes памяти\n')
# print(f'Итог выполнения кода: {answer[0]}')

    # Используемые переменные:
    #      array = [83, 63, 14, 38, 84, 32, 28, 12, 60, 44] <class 'list'>
    #      min_pos = 4 <class 'int'>
    #      max_pos = 7 <class 'int'>
    #      i = 9 <class 'int'>
    #
    # Для выполнения кода потребовалось 556 bytes памяти

print('#' * 51)

answer = hw03_3_modify(array_1)
print(f'Для выполнения кода потребовалось {answer[1]} bytes памяти\n')
# print(f'Итог выполнения кода: {answer[0]}')

    # Используемые переменные:
    #      array = [83, 63, 14, 38, 12, 32, 28, 84, 60, 44] <class 'list'>
    #      min_pos = 7 <class 'int'>
    #      max_pos = 4 <class 'int'>
    #
    # Для выполнения кода потребовалось 528 bytes памяти

print('#' * 51)

answer = hw03_5(array_2)
print(f'Для выполнения кода потребовалось {answer[2]} bytes памяти\n')
# print(f'Итог выполнения кода: {answer[0], answer[1]}')

    # Используемые переменные:
    #      array = [17, 32, -75, -66, -96, -77, -32, 48, 20, -15] <class 'list'>
    #      min_el = -96 <class 'int'>
    #      i = -15 <class 'int'>
    #      max_el = -15 <class 'int'>
    #
    # Для выполнения кода потребовалось 556 bytes памяти

print('#' * 51)

answer = hw03_5_modify(array_2)
print(f'Для выполнения кода потребовалось {answer[2]} bytes памяти\n')
# print(f'Итог выполнения кода: {answer[0], answer[1]}')

    # Используемые переменные:
    #      array = [17, 32, -75, -66, -96, -77, -32, 48, 20, -15] <class 'list'>
    #      new_arr = [-75, -66, -96, -77, -32, -15] <class 'list'>
    #      max_el = -15 <class 'int'>
    #
    # Для выполнения кода потребовалось 796 bytes памяти


# Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
# Тип системы: 64-разрядная операционная система