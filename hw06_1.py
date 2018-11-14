from random import randint
from sys import getsizeof


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

    return array, show_total_size(locals())


def show_total_size(dictionary):
    def get_size(x):
        size = getsizeof(x)
        if type(x) is int:
            print(f'Size of {x} = {size}')
        if type(x) is list:
            print(f'Size of {x} = {size}')
            for i in x:
                size_i = getsizeof(i)
                size += size_i
                print(f'\tSize of {i} = {size_i}')
            print(f'\n\tTotal size of list = {size}')
        return size

    print('Используемые переменные: ')
    [print('\t', x, '=', dictionary[x]) for x in dictionary]
    print()

    total_size = 0
    for x in dictionary:
        total_size += get_size(dictionary[x])
    return total_size


answer = min_max(10)
print(f'Для выполнения кода потребовалось: {answer[1]} bytes\n\nИтог выполнения кода: {answer[0]}')