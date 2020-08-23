"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

# python3 -m timeit -n 1000 -s "import less_3_task_6" "less_3_task_6.array_sum(10)"
# or
# python -m timeit -n 1000 -s "import less_3_task_6" "less_3_task_6.array_sum(10)"

import random
import cProfile


# вариант 1
# def array_sum(my_range):
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
#
#     new_lst = new_lst[1:-1]
#     my_sum = 0
#     for e in new_lst:
#         my_sum += e
#
#     return my_sum


# "less_3_task_6.array_sum(10)"
# 1000 loops, best of 5: 20.1 usec per loop

# "less_3_task_6.array_sum(50)"
# 1000 loops, best of 5: 178 usec per loop

# "less_3_task_6.array_sum(100)"
# # 1000 loops, best of 5: 572 usec per loop

# cProfile.run("array_sum(10)")
# cProfile.run("array_sum(50)")
# cProfile.run("array_sum(100)")


# вариант 2
# def array_sum(my_range):
#     min_ = -100
#     max_ = 100
#     lst = [random.randint(min_, max_) for _ in range(my_range)]
#     lst.sort()
#     lst = sum(lst[1:-1])
#     return lst


# "less_3_task_6.array_sum(10)"
# 1000 loops, best of 5: 11 usec per loop

# "less_3_task_6.array_sum(50)"
# 1000 loops, best of 5: 51 usec per loop

# "less_3_task_6.array_sum(100)"
# 1000 loops, best of 5: 104 usec per loop

# cProfile.run("array_sum(10)")
# cProfile.run("array_sum(50)")
# cProfile.run("array_sum(100)")


# вариант 3
def array_sum(my_range):
    min_ = -100
    max_ = 100
    lst = [random.randint(min_, max_) for _ in range(my_range)]
    lst = sum(lst) - max(lst) - min(lst)
    return lst


# "less_3_task_6.array_sum(10)"
# 1000 loops, best of 5: 11.4 usec per loop

# "less_3_task_6.array_sum(50)"
# 1000 loops, best of 5: 51.2 usec per loop

# "less_3_task_6.array_sum(100)"
# 1000 loops, best of 5: 103 usec per loop

# cProfile.run("array_sum(10)")
# cProfile.run("array_sum(50)")
# cProfile.run("array_sum(100)")


# общий вывод:
# вариант 3 лучше остальных:
# - хорошая скорость выполнения
# - короткий и понятный код
