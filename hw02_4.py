# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n)
# вводится с клавиатуры.

n = int(input('n = '))

num = 1
summ = 0

while n > 0:
    num *= -0.5
    summ += num
    n -= 1

print(f'Сумма n элементов = {summ}')