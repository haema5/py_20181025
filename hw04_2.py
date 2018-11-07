# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

def sieve_era(i):
    array_p = []
    h = 2
    k = 0
    while True:
        for j in range(2, h):
            if h % j == 0:
                k = k + 1
        if k == 0:
            array_p.append(h)
            if len(array_p) == i:
                break
        else:
            k = 0
        h += 1
    return array_p[i - 1]


print(sieve_era(10))
