"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random
import sys


def memory(*args):
    my_sum = 0
    for i in args:
        print(f"{i} = {sys.getsizeof(i)} байт")
        my_sum += sys.getsizeof(i)
    print(f"Всего {my_sum} байт")


print(sys.version, sys.platform)
# 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] win32


# вариант 1
# min_ = None
# max_ = None
# lst = None
# new_lst = None
# x = None
# n = None
# my_sum = None


# def array_sum(my_range):
#     global min_
#     global max_
#     global lst
#     global new_lst
#     global x
#     global n
#     global my_sum
#     min_ = -100
#     max_ = 100
#     lst = [random.randint(min_, max_) for _ in range(my_range)]
#     new_lst = []
#     x = min_
#     n = 0
#     for i in lst:
#         if i > x:
#             x = i
#         for j in lst:
#             if j is not None and x > j:
#                 x = j
#         lst.remove(x)
#         lst.insert(n, None)
#         new_lst.append(x)
#         x = min_
#         n += 1
#     new_lst = new_lst[1:-1]
#     my_sum = 0
#     for e in new_lst:
#         my_sum += e
#     return my_sum


# memory(array_sum, array_sum(100), min_, max_, lst, new_lst, x, n, my_sum)
# <function array_sum at 0x00B0B5C8> = 68 байт
# 18 = 14 байт
# -100 = 14 байт
# 100 = 14 байт
# [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None] = 452 байт
# [-96, -88, -88, -84, -80, -79, -79, -78, -77, -77, -77, -75, -73, -73, -71, -69, -68, -66, -65, -64, -62, -60, -57,
# -57, -56, -52, -48, -47, -46, -42, -42, -41, -40, -40, -40, -36, -35, -33, -30, -27, -25, -22, -17, -14, -7, -6, -3,
# -3, -2, 0, 1, 4, 5, 5, 6, 6, 12, 22, 22, 27, 28, 28, 28, 29, 29, 31, 32, 41, 45, 45, 46, 49, 49, 53, 53, 55, 56, 61,
# 66, 67, 69, 71, 72, 73, 75, 82, 84, 86, 86, 87, 87, 88, 91, 93, 97, 97, 98, 98] = 420 байт
# -100 = 14 байт
# 100 = 14 байт
# 18 = 14 байт
# Всего 1024 байт


# вариант 2
# min_ = None
# max_ = None
# lst = None


# def array_sum(my_range):
#     global min_
#     global max_
#     global lst
#     min_ = -100
#     max_ = 100
#     lst = [random.randint(min_, max_) for _ in range(my_range)]
#     lst.sort()
#     lst = sum(lst[1:-1])
#     return lst


# memory(array_sum, array_sum(100), min_, max_, lst)
# <function array_sum at 0x0120A610> = 68 байт
# 218 = 14 байт
# -100 = 14 байт
# 100 = 14 байт
# 218 = 14 байт
# Всего 124 байт


# вариант 3
min_ = None
max_ = None
lst = None


def array_sum(my_range):
    global min_
    global max_
    global lst
    min_ = -100
    max_ = 100
    lst = [random.randint(min_, max_) for _ in range(my_range)]
    lst = sum(lst) - max(lst) - min(lst)
    return lst


memory(array_sum, array_sum(100), min_, max_, lst)
# <function array_sum at 0x019AA610> = 68 байт
# -291 = 14 байт
# -100 = 14 байт
# 100 = 14 байт
# -291 = 14 байт
# Всего 124 байт


# общий вывод:
# вариант 3 лучше остальных:
# - хорошая скорость выполнения
# - короткий и понятный код
# - занимает меньше памяти
