# По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print('Введите координаты точки А: ')
x1 = float(input('  x1 = '))
y1 = float(input('  y1 = '))

print('Введите координаты точки B: ')
x2 = float(input('  x2 = '))
y2 = float(input('  y2 = '))

a = y1 - y2
b = x2 - x1
c = x1 * y2 - x2 * y1

if a != 0 or b != 0:
    print(f'Уравнение прямой, проходящей через эти точки:\n'
          f'  {a}x + {b}y + {c} = 0')
else:
    print('Уровнение не имеет смысла.')
