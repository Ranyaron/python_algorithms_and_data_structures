"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов."""

numbers = [_ for _ in range(2, 99 + 1)]
my_range = [_ for _ in range(2, 9 + 1)]

print(f"В диапазоне натуральных чисел от {numbers[0]} до {numbers[-1]}:")

for i in my_range:
    n = 0
    for j in numbers:
        if j % i == 0:
            n += 1
    print(f"{n} чисел, кратные {i}")