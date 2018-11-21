# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть дана строка S длиной N. Например, состоящая только из маленьких
# латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля
# hashlib или встроенную функцию hash()

from random import choices
from string import ascii_lowercase

N = 100


def find_substrings(string):
    diff_subs = []
    len_str = len(string)
    for i in range(1, len_str):
        for j in range(0, len_str - i + 1):
            sub_string = string[j:j + i]
            hash_sub = hash(sub_string)
            if hash_sub not in diff_subs:
                diff_subs.append(hash_sub)
    subs = len(diff_subs)
    return subs


s = ''.join(choices(ascii_lowercase, k=N))
print(f'Исходная строка: {s}\n\nКоличество различных подстрок: {find_substrings(s)}')
