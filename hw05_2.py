# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
# каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque


def input_format(a, b):
    num_1 = deque(str.upper(a))
    num_2 = deque(str.upper(b))
    return num_1, num_2


def toDec(hexa):
    hex_dec = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    dec = 0
    deg = len(hexa) - 1
    for var in hexa:
        dec += hex_dec[var] * 16 ** deg
        deg -= 1
    return dec


def toHex(dec):
    dec_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hexa = ''
    if dec == 0:
        return '0'
    while dec != 0:
        hexa += dec_hex[dec % 16]
        dec = dec // 16
    return hexa[::-1]


def oper_sum(num_1, num_2):
    result = deque(toHex(toDec(num_1) + toDec(num_2)))
    return result


def oper_mul(num_1, num_2):
    result = deque(toHex(toDec(num_1) * toDec(num_2)))
    return result


a = input('Введите число А (HEX): ')
b = input('Введите число B (HEX): ')
num_1, num_2 = input_format(a, b)

summ = oper_sum(num_1, num_2)
mult = oper_mul(num_1, num_2)

print(f'\n{list(num_1)} + {list(num_2)} = {list(summ)};')
print(f'{list(num_1)} * {list(num_2)} = {list(mult)}.')
