"""5. Пользователь вводит номер буквы в алфавите.
Определить, какая это буква."""

number_letter = input("Введите номер буквы: ")

letter = chr(int(number_letter) - 1 + ord("a"))

print(f"Буква под № {number_letter} в алфавите = {letter}")
