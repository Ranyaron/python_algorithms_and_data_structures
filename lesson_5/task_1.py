"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import OrderedDict

my_dict = {}
number_enterprises = int(input("Введите кол-во предприятий: "))

for i in range(number_enterprises):
    name_enterprises = input("Введите наименование предприятия: ")
    profit_enterprises = int(input("Введите прибыль за четыре квартала: "))
    my_dict[name_enterprises] = profit_enterprises

# print(my_dict)

new_dict = OrderedDict(sorted(my_dict.items(), key=lambda x: x[1]))
# print(new_dict)

my_sum = 0
for key, value in new_dict.items():
    my_sum += value

average_profit = round(my_sum / len(new_dict), 2)
print(f"Средняя прибыль (за год для всех предприятий) = {average_profit}")

my_list_min = []
my_list_max = []
for key, value in new_dict.items():
    if value < average_profit:
        my_list_min.append(key)
    if value > average_profit:
        my_list_max.append(key)

print(f"Прибыль {', '.join(my_list_max)} выше среднего.")
print(f"Прибыль {', '.join(my_list_min)} ниже среднего.")
