"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random


def middle_element(numbers, low, high):
    # выбираем средний элемент в качестве опорного
    pivot = numbers[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while numbers[i] < pivot:
            i += 1

        j -= 1
        while numbers[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # если элемент с индексом i (слева от опорного) больше,
        # чем элемент с индексом j (справа от опорного), меняем их местами
        numbers[i], numbers[j] = numbers[j], numbers[i]


def merge_sort(arr):
    """Вспомогательная функция, которая вызывается рекурсивно"""
    def quick_sort(items, low, high):
        if low < high:
            split_index = middle_element(items, low, high)
            quick_sort(items, low, split_index)
            quick_sort(items, split_index + 1, high)

    quick_sort(arr, 0, len(arr) - 1)


x = 0
y = 50
array = [i for i in range(x, y)]
random.shuffle(array)
print(array)

merge_sort(array)
print(array)
