"""8. Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого)."""

# python3 -m timeit -n 1000 -s "import less_1_task_8" "less_1_task_8.average_number(100)"
# or
# python -m timeit -n 1000 -s "import less_1_task_8" "less_1_task_8.average_number(100)"

import random


# вариант 1
# def average_number(n):
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


# "less_1_task_8.average_number(100)"
# 1000 loops, best of 5: 2.09 usec per loop

# "less_1_task_8.average_number(1000)"
# 1000 loops, best of 5: 2.26 usec per loop

# "less_1_task_8.average_number(10000)"
# 1000 loops, best of 5: 3.27 usec per loop


# вариант 2
def average_number(n):
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


# "less_1_task_8.average_number(100)"
# 1000 loops, best of 5: 2.18 usec per loop

# "less_1_task_8.average_number(1000)"
# 1000 loops, best of 5: 2.22 usec per loop

# "less_1_task_8.average_number(10000)"
# 1000 loops, best of 5: 3.32 usec per loop


# вариант 3
# def average_number(n):
#     numbers = [random.randint(1, n) for _ in range(3)]
#     if numbers[1] < numbers[0] < numbers[2] or numbers[2] < numbers[0] < numbers[1]:
#         return numbers[0]
#     elif numbers[0] < numbers[1] < numbers[2] or numbers[2] < numbers[1] < numbers[0]:
#         return numbers[1]
#     else:
#         return numbers[2]


# "less_1_task_8.average_number(100)"
# 1000 loops, best of 5: 3.89 usec per loop

# "less_1_task_8.average_number(1000)"
# 1000 loops, best of 5: 4.02 usec per loop

# "less_1_task_8.average_number(10000)"
# 1000 loops, best of 5: 4.29 usec per loop


# общий вывод:
# вариант 2 лучше остальных:
# - хорошая скорость выполнения
# - короткий и понятный код
