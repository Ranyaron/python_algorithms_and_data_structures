"""4. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв."""

letter_1 = input("Введите первую букву: ")
letter_2 = input("Введите вторую букву: ")

number_letter_1 = ord(letter_1) - ord("a") + 1
number_letter_2 = ord(letter_2) - ord("a") + 1

number_letters = ord(letter_2) - ord(letter_1) - 1

print(f"Место в алфавите у буквы {letter_1} = {number_letter_1}")
print(f"Место в алфавите у буквы {letter_2} = {number_letter_2}")
print(f"Между буквами {letter_1} и {letter_2} находится {number_letters} букв(ы).")
