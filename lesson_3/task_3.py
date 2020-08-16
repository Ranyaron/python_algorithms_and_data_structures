"""3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы."""

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