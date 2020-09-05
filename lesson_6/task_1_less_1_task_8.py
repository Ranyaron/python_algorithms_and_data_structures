"""8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого)."""

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
# a = None
# b = None
# c = None


# def average_number(n):
#     global a
#     global b
#     global c
#     a = random.randint(1, n)
#     b = random.randint(1, n)
#     c = random.randint(1, n)
#     if a > b:
#         if a < c:
#             # print(f"Среднее {a}")
#             return a
#         else:
#             if b > c:
#                 # print(f"Среднее {b}")
#                 return b
#             else:
#                 # print(f"Среднее {c}")
#                 return c
#     else:
#         if a > c:
#             # print(f"Среднее {a}")
#             return a
#         else:
#             if b < c:
#                 # print(f"Среднее {b}")
#                 return b
#             else:
#                 # print(f"Среднее {c}")
#                 return c


# memory(average_number, average_number(100), a, b, c)
# <function average_number at 0x01E7C5C8> = 68 байт
# 53 = 14 байт
# 53 = 14 байт
# 64 = 14 байт
# 29 = 14 байт
# Всего 124 байт


# вариант 2
a = None
b = None
c = None


def average_number(n):
    global a
    global b
    global c
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)
    if b < a < c or c < a < b:
        # print(f"Среднее {a}")
        return a
    elif a < b < c or c < b < a:
        # print(f"Среднее {b}")
        return b
    else:
        # print(f"Среднее {c}")
        return c


memory(average_number, average_number(100), a, b, c)
# <function average_number at 0x00BCB5C8> = 68 байт
# 68 = 14 байт
# 62 = 14 байт
# 80 = 14 байт
# 68 = 14 байт
# Всего 124 байт


# вариант 3
# numbers = None


# def average_number(n):
#     global numbers
#     numbers = [random.randint(1, n) for _ in range(3)]
#     if numbers[1] < numbers[0] < numbers[2] or numbers[2] < numbers[0] < numbers[1]:
#         return numbers[0]
#     elif numbers[0] < numbers[1] < numbers[2] or numbers[2] < numbers[1] < numbers[0]:
#         return numbers[1]
#     else:
#         return numbers[2]


# memory(average_number, average_number(100), numbers)
# <function average_number at 0x0091C5C8> = 68 байт
# 61 = 14 байт
# [83, 61, 61] = 44 байт
# Всего 126 байт


# общий вывод:
# вариант 2 лучше остальных:
# - хорошая скорость выполнения
# - короткий и понятный код
# - занимает меньше памяти
