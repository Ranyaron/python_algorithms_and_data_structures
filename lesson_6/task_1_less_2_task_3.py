"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""

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
# number = None
# turn = None


# def mirror(n):
#     global number
#     global turn
#     number = random.randint(1, n)
#     turn = ""
#     while number > 0:
#         turn += str(number % 10)
#         number = number // 10


# memory(mirror, mirror(100), number, turn)
# <function mirror at 0x01B1A610> = 68 байт
# None = 8 байт
# 0 = 12 байт
# 33 = 27 байт
# Всего 115 байт


# вариант 2
# number = None
# lst = None


# def mirror(n):
#     global number
#     global lst
#     number = random.randint(1, n)
#     lst = []
#     for i in str(number):
#         lst.append(i)
#     lst.reverse()
#     return lst


# memory(mirror, mirror(100), number, lst)
# <function mirror at 0x01D7A610> = 68 байт
# ['3', '8'] = 44 байт
# 83 = 14 байт
# ['3', '8'] = 44 байт
# Всего 170 байт


# вариант 3
number = None


def mirror(n):
    global number
    number = str(random.randint(1, n))
    number = number[::-1]
    return number


memory(mirror, mirror(100), number)
# <function mirror at 0x01BCA5C8> = 68 байт
# 18 = 27 байт
# 18 = 27 байт
# Всего 122 байт


# общий вывод:
# вариант 3 лучше остальных:
# - хорошая скорость выполнения
# - короткий код
# - занимает памяти меньше 2 варианта и немного больше 1 варианта
