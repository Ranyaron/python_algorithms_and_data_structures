"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""

# python3 -m timeit -n 1000 -s "import less_2_task_3" "less_2_task_3.mirror(100)"
# or
# python -m timeit -n 1000 -s "import less_2_task_3" "less_2_task_3.mirror(100)"

import random


# вариант 1
# def mirror(n):
#     number = random.randint(1, n)
#     turn = ""
#     while number > 0:
#         turn += str(number % 10)
#         number = number // 10


# "less_2_task_3.mirror(100)"
# 1000 loops, best of 5: 1.71 usec per loop

# "less_2_task_3.mirror(1000)"
# 1000 loops, best of 5: 2.04 usec per loop

# "less_2_task_3.mirror(10000)"
# 1000 loops, best of 5: 2.47 usec per loop


# вариант 2
# def mirror(n):
#     number = random.randint(1, n)
#     lst = []
#     for i in str(number):
#         lst.append(i)
#     lst.reverse()
#     return lst


# "less_2_task_3.mirror(100)"
# 1000 loops, best of 5: 1.53 usec per loop

# "less_2_task_3.mirror(1000)"
# 1000 loops, best of 5: 1.7 usec per loop

# "less_2_task_3.mirror(10000)"
# 1000 loops, best of 5: 1.82 usec per loop


# вариант 3
def mirror(n):
    number = str(random.randint(1, n))
    number = number[::-1]
    return number


# "less_2_task_3.mirror(100)"
# 1000 loops, best of 5: 1.34 usec per loop

# "less_2_task_3.mirror(1000)"
# 1000 loops, best of 5: 1.39 usec per loop

# "less_2_task_3.mirror(10000)"
# 1000 loops, best of 5: 1.5 usec per loop


# общий вывод:
# вариант 3 лучше остальных:
# - хорошая скорость выполнения
# - короткий код
