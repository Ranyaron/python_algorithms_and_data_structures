"""2. Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
Пример работы программ:
# >>> sieve(2)
3
# >>> prime(4)
7
# >>> sieve(5)
11
# >>> prime(1)
2
"""

# python3 -m timeit -n 1000 -s "import task_2" "task_2.sieve_eratosthenes(10)"
# or
# python -m timeit -n 1000 -s "import task_2" "task_2.sieve_eratosthenes(10)"


# вариант 1
def sieve_eratosthenes(n):
    count = 3636
    sieve = [i for i in range(count)]
    sieve[1] = 0

    for i in range(2, count):
        if sieve[i] != 0:
            j = i * 2

            while j < count:
                sieve[j] = 0
                j += i

    result = [i for i in sieve if i != 0]
    result = result[n - 1]
    return result


# "task_2.sieve_eratosthenes(10)"
# 1000 loops, best of 5: 829 usec per loop

# "task_2.sieve_eratosthenes(50)"
# 1000 loops, best of 5: 824 usec per loop

# "task_2.sieve_eratosthenes(100)"
# 1000 loops, best of 5: 826 usec per loop

# "task_2.sieve_eratosthenes(500)"
# 1000 loops, best of 5: 827 usec per loop


# вариант 2
# def sieve_eratosthenes(n):
#     lst = []
#     for i in range(2, 3636):
#         for j in lst:
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
#         if len(lst) == n:
#             break
#
#     return lst[-1]


# "task_2.sieve_eratosthenes(10)"
# 1000 loops, best of 5: 5.54 usec per loop

# "task_2.sieve_eratosthenes(50)"
# 1000 loops, best of 5: 77.5 usec per loop

# "task_2.sieve_eratosthenes(100)"
# 1000 loops, best of 5: 265 usec per loop

# "task_2.sieve_eratosthenes(500)"
# 1000 loops, best of 5: 5.83 msec per loop
