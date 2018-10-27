# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

print('Введите три числа: ')
num_1 = float(input('  1: '))
num_2 = float(input('  2: '))
num_3 = float(input('  3: '))

if num_1 != num_2 and num_2 != num_3 and num_3 != num_1:
    if num_1 < num_2 < num_3 or num_1 > num_2 > num_3:
        s = num_2
    elif num_2 < num_3 < num_1 or num_2 > num_3 > num_1:
        s = num_3
    elif num_2 < num_1 < num_3 or num_2 > num_1 > num_3:
        s = num_1
    print(f'Число "{s}" является средним.')
else:
    print('Среднее найти невозможно!')
