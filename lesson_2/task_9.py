"""9. Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр."""

max_number = ""
my_max = 0

entered_numbers = int(input("Сколько цифр Вы хотите ввести: "))

while entered_numbers > 0:
    number = input("Введите число: ")
    my_sum = 0
    for i in number:
        my_sum += int(i)
    if my_sum > my_max:
        max_number = number
        my_max = my_sum
        entered_numbers -= 1
    else:
        entered_numbers -= 1

print(f"Наибольшее число {max_number}, его сумма цифр = {my_max}")