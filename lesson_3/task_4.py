"""4. Определить, какое число в массиве встречается чаще всего."""

import random

lst = [random.randint(1, 5) for _ in range(10)]
new_lst = []
print(lst)
count = 0
number = 0
for i in lst:
    n = i
    cnt = 0
    for j in lst:
        if n == j:
            cnt += 1
    if cnt > count:
        count = cnt
        number = n

print(number)