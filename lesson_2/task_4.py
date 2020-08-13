"""4. Найти сумму n элементов следующего ряда чисел:
1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры."""


def rec(n):
    number = 1
    my_sum = 1
    while n > 1:
        number /= -2
        my_sum += number
        n -= 1
    return my_sum


elements = int(input("Введите кол-во элементов n: "))
print(f"Сумма n элементов = {rec(elements)}")