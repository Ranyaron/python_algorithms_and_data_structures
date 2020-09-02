"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F.
Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque

num_1 = input("Введите первое 16-ричное число: ")
num_2 = input("Введите второе 16-ричное число: ")
number_1 = deque(num_1)
number_2 = deque(num_2)

number_1.reverse()
number_2.reverse()
# print(number_1, number_2)

my_list = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

new_number_1 = []
for i in number_1:
    for key, value in my_list.items():
        if i == key:
            new_number_1.append(value)
            break
    else:
        new_number_1.append(i)

# print(new_number_1)

new_number_2 = []
for j in number_2:
    for key, value in my_list.items():
        if j == key:
            new_number_2.append(value)
            break
    else:
        new_number_2.append(j)

# print(new_number_2)

if len(new_number_1) > len(new_number_2):
    new_number_2.append(0)
if len(new_number_1) < len(new_number_2):
    new_number_1.append(0)


# сумма чисел
outcome = []
q = 0
for i in range(len(new_number_1)):
    my_sum = int(new_number_1[i]) + int(new_number_2[i]) + q
    if my_sum > 16:
        remainder = my_sum - 16
        outcome.append(remainder)
        q = 1
    else:
        outcome.append(my_sum)
        q = 0

# print(outcome)

new_outcome = []
for k in outcome:
    for key, value in my_list.items():
        if k == value:
            new_outcome.append(key)
            break
    else:
        new_outcome.append(str(k))

new_outcome.reverse()

print(f"Сумма чисел {num_1} и {num_2} = {''.join(new_outcome)}")


# произведение
number = hex(int(num_1, 16) * int(num_2, 16))
print(f"Произведение {num_1} и {num_2} = {number}")

# outcome_1 = []
# outcome_2 = []
# q = 0
#
# for i in range(len(new_number_1)):
#     my_sum = int(new_number_1[i]) * int(new_number_2[0]) + q
#     if my_sum > 16:
#         remainder = my_sum - 16
#         outcome_1.append(remainder)
#         q = 1
#     else:
#         outcome_1.append(my_sum)
#         q = 0
# outcome_1.append(0)
#
#
# for i in range(len(new_number_1)):
#     my_sum = int(new_number_1[i]) * int(new_number_2[1]) + q
#     if my_sum > 16:
#         remainder = my_sum - 16
#         outcome_2.append(remainder)
#         q = 1
#     else:
#         outcome_2.append(my_sum)
#         q = 0
# outcome_2.reverse()
# outcome_2.append(0)
# outcome_2.reverse()
#
# outcome = []
# q = 0
# for i in range(len(outcome_1)):
#     my_sum = int(outcome_1[i]) + int(outcome_2[i]) + q
#     if my_sum > 16:
#         remainder = my_sum - 16
#         outcome.append(remainder)
#         q = 1
#     else:
#         outcome.append(my_sum)
#         q = 0
#
# print(outcome)
#
# new_outcome = []
# for k in outcome:
#     for key, value in my_list.items():
#         if k == value:
#             new_outcome.append(key)
#             break
#     else:
#         new_outcome.append(str(k))
#
# new_outcome.reverse()
#
# print(''.join(new_outcome))
