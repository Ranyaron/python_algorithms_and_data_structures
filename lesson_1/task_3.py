"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random

print("Укажите границы для генерации")
a = int(input("Первое целое число: "))
b = int(input("Второе целое число: "))
c = float(input("Первое вещественное число: "))
d = float(input("Второе вещественное число: "))
e = input("Первый символ: ")
f = input("Второй символ: ")

random_integer = random.randint(a, b)
print(f"Случайное целое число в границах от {a} до {b} = {random_integer}")

random_real_number = random.uniform(c, d)
print(f"Случайное вещественное число в границах от {c} до {d} = {random_real_number}")

random_character = chr(random.randint(ord(e), ord(f)))
print(f"Случайный символ в границах от {e} до {f} = {random_character}")
