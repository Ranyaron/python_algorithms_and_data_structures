"""7. В одномерном массиве целых чисел определить
два наименьших элемента.
Они могут быть как равны между собой (оба минимальны),
так и различаться."""

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
print(f"2 наименьших числа: {new_lst[-1]} и {new_lst[-2]}")