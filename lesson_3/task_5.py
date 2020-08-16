"""5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве."""

import random

lst = [random.randint(-100, -1) for _ in range(10)]
print(lst)
n = 0
pos = None

for i, item in enumerate(lst):
    if item < n:
        n = item
        pos = i

print(f"Максимальный отрицательный элемент {n}, его позиция в массиве {pos}")