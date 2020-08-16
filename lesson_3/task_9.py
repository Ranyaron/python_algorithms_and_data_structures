"""9. Найти максимальный элемент
среди минимальных элементов столбцов матрицы."""

import random

rand_start = 1
rand_end = 10
size = 5
matrix = [[random.randint(rand_start, rand_end) for _ in range(size)] for _ in range(size)]
print(matrix)

lst = []
m = 0
z = rand_end
x = 1
n = 0
while m != size:
    for line in matrix:
        if line[m] <= z:
            z = line[m]
            lst.append(line[m])
            if len(lst) > x:
                del lst[n]
    m += 1
    z = rand_end
    x += 1
    n += 1

print(f"Минимальные элементы столбцов матрицы: {lst}")

max_number = rand_start
for i in lst:
    if i > max_number:
        max_number = i

print(f"Максимальный элемент среди минимальных элементов столбцов матрицы: {max_number}")