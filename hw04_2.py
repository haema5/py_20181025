# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile


# Первый
def new_arr(ar_le):
    def del_n_pri(sieve):
        for i in range(2, len(sieve)):
            if sieve[i] != 0:
                j = i + i
                while j < len(sieve):
                    sieve[j] = 0
                    j += i
        return sieve

    sieve = [_ for _ in range(ar_le + 1)]
    sieve[1] = 0
    sieve = del_n_pri(sieve)
    return sieve


def first(n):
    def check_ar(sieve, n):
        k = 0
        for i in sieve:
            if i != 0:
                k += 1
            if k == n:
                return i
        return k

    result = 0
    k = n
    while result < n:
        sieve = new_arr(k)
        result = check_ar(sieve, n)
        k += 1
    return result


# cProfile.run('first(10)')
# 1    0.000    0.000    0.000    0.000 hw04_2.py:26(first)
#
# cProfile.run('first(100)')
# 1    0.001    0.001    0.082    0.082 hw04_2.py:26(first)
#
# cProfile.run('first(1000)')
# 1    0.121    0.121   18.916   18.916 hw04_2.py:26(first)
#
#
#
# "hw04_2.first(10)"
# 100 loops, best of 3: 124 usec per loop
#
# "hw04_2.first(100)"
# 100 loops, best of 3: 46.9 msec per loop
#
# "hw04_2.first(1000)"
# 10 loops, best of 3: 12.7 sec per loop

# Второй

def second(i):
    arr_pri = []
    n = 2
    while True:
        is_prime = True
        for j in arr_pri:
            if n % j == 0:
                is_prime = False
                break
        if is_prime:
            arr_pri.append(n)
        if len(arr_pri) == i:
            break
        n += 1
    return arr_pri[i - 1]

# cProfile.run('second(10)')
# 1    0.000    0.000    0.000    0.000 hw04_2.py:64(second)
#
# cProfile.run('second(100)')
# 1    0.000    0.000    0.000    0.000 hw04_2.py:64(second)
#
# cProfile.run('second(1000)')
# 1    0.024    0.024    0.025    0.025 hw04_2.py:64(second
#
#
#
# "hw04_2.second(10)"
# 100 loops, best of 3: 7.2 usec per loop
#
# "hw04_2.second(100)"
# 100 loops, best of 3: 290 usec per loop
#
# "hw04_2.second(1000)"
# 100 loops, best of 3: 24.5 msec per loop

# Вывод:
# Второй способ получился значительно быстрее и менее ресурсозатратным
# за счет прямого наполнения массива простыми числами.
