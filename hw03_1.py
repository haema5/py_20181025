# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому
# из чисел в диапазоне от 2 до 9.

MIN_D = 2
MAX_D = 99
MIN_N = 2
MAX_N = 9

print(f'В диапазоне чисел от {MIN_D} до {MAX_D}: ')
answer = [0] * (MAX_N - MIN_N + 1)
for n in range(MIN_N, MAX_N + 1):
    for d in range(MIN_D, MAX_D + 1):
        if d % n == 0:
            answer[n - MIN_N] += 1
    print(f'\t - кратных числу {n} - {answer[n - 2]}')