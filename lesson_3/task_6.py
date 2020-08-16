"""6. В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""

import random

lst = [random.randint(1, 100) for _ in range(10)]
print(lst)

new_lst = []
x = 0
n = 0
for i in lst:
    if i > x:
        x = i
    for j in lst:
        if x < j:
            x = j
    lst.remove(x)
    lst.insert(n, 0)
    new_lst.append(x)
    x = 0
    n += 1

print(new_lst)

new_lst = new_lst[1:-1]
print(new_lst)

my_sum = 0
for e in new_lst:
    my_sum += e

print(f"Сумму элементов, находящихся между минимальным и максимальным элементами, {my_sum}")