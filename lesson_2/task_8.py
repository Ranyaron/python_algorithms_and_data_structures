"""8. Посчитать, сколько раз встречается определенная цифра
в введенной последовательности чисел. Количество вводимых чисел и цифра,
которую необходимо посчитать, задаются вводом с клавиатуры."""

count = 0
nc = ""

entered_numbers = int(input("Сколько цифр Вы хотите ввести: "))
number_count = input("Какую цифру посчитать: ")

while entered_numbers > 0:
    number = input("Введите число: ")
    nc += number
    entered_numbers -= 1

for i in nc:
    if number_count == i:
        count += 1

print(f"Кол-во цифры {number_count} в веденных числах = {count}")