# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.

import cProfile


def sieve_era(i):
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


print(sieve_era(10))


# cProfile.run('sieve_era(10)')
# 1    0.000    0.000    0.000    0.000 hw04_2.py:41(sieve_era)
# cProfile.run('sieve_era(100)')
# 1    0.001    0.001    0.001    0.001 hw04_2.py:41(sieve_era)
# cProfile.run('sieve_era(1000)')
# 1    0.045    0.045    0.046    0.046 hw04_2.py:41(sieve_era)
# cProfile.run('sieve_era(10000)')
# 1    4.292    4.292    4.304    4.304 hw04_2.py:41(sieve_era)

# "hw04_2.sieve_era(10)"
# 100 loops, best of 5: 14.1 usec per loop
# "hw04_2.sieve_era(100)"
# 100 loops, best of 5: 532 usec per loop
# "hw04_2.sieve_era(1000)"
# 100 loops, best of 5: 42.5 msec per loop
# "hw04_2.sieve_era(10000)"
# 10 loops, best of 5: 4.15 sec per loop

def prime(i):
    primes = []
    n = 2
    while True:
        is_prime = True
        for num in range(2, n):
            if n % num == 0:
                is_prime = False

        if is_prime:
            primes.append(n)
        if len(primes) == i:
            break
        n += 1
    return primes[i - 1]

cProfile.run('prime(10000)')
print(prime(10))
