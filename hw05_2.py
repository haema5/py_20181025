# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
# каждое число представляется как массив, элементы которого это цифры числа.
#
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque, Counter

# hd = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
#       'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
hd = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
dh = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
      'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
answer = deque()
print(hd)

a = deque(str.upper('A2'))
a.reverse()
b = deque(str.upper('C4F'))
b.reverse()
print(a, b, sep=',\t')
zn = '+'
if a < b:
    b, a = a, b
    print(a, b, sep=',\t')

ost = 0
for d in range(len(a)):
    if d > len(b)-1:
        summa = hd[a[d]] + ost
        ost = 0
        if summa > 15:
            ost = summa // 15
            summa = summa % 15
    else:
        summa = hd[a[d]] + hd[b[d]] + ost
        ost = 0
        if summa > 15:
            ost = summa // 15
            summa = summa % 15
    answer.appendleft(summa)

print(answer)
for i in answer:
    print(i)
    print(answer.index(i))
    print(hd[str(i)])
    answer[answer.index(i)] = hd[i]
print(answer)