# Знакомство с языком Python (семинары)
# Урок 5. Рекурсия и алгоритмы

# # Задача №33. Решение в группах
# # Хакер Василий получил доступ к классному журналу и
# # хочет заменить все свои минимальные оценки на
# # максимальные. Напишите программу, которая
# # заменяет оценки Василия, но наоборот: все
# # максимальные – на минимальные.
# # Input: 5 -> 1 3 3 3 4
# # Output: 1 3 3 3 1
# def swapMark(arr):
#     max = arr[0]
#     min = arr[0]
#     for i in range(1, len(arr)):
#         if max < arr[i]:
#             max = arr[i]
#         if min > arr[i]:
#             min = arr[i]
#     for i in range(len(arr)):
#         if arr[i] == max:
#             arr[i] = min
#     print(arr)

# arr = [1, 3, 3, 3, 4]
# swapMark(arr)   

# # Задача
# # Напишите функцию, которая принимает одно число и 
# # проверяет, является ли оно простым
# # Напоминание: Простое число - это число, которое 
# # имеет 2 делителя: 1 и n(само число)
# # Input: 5
# # Output: yes
# def check(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return (f'Число {number} не простое, так делится на {i} без остатка')
#     return (f'Число {number} простое')
# number = int(input('Введите число: '))

# res = check(number)
# print(res)

# # Задача
# # Дано натуральное число N и последовательность из N элементов.
# # Требуется вывести эту последовательность в обратном порядке.
# # Примечание. В программе запрещается объявлять массивы и использовать циклы
# # (даже для ввода и вывода).
# # Input: 2 3 4
# # Output: 4 3
# def pos(number):
#     if number == 0:
#         return ''
#     x = int(input('Введите число: '))
#     return pos(number - 1) + str(x)
# number = int(input('Введите число: '))
# print(pos(number))

# def pos(number):
#     print('Запускается функция от', number)
#     if number == 0:
#         return ''
#     x = int(input('Введите число: '))
#     res = pos(number - 1) + str(x)
#     print (res)
#     return res
# number = int(input('Введите число: '))
# print(pos(number))

# def fib(n):
#     if n > 0:
#         if n in [1, 2]:
#             return 1
#         return fib(n - 1) + fib(n - 2)
#     else:
#         if n in [-1]:
#             return 1
#         return fib(n + 2) - fib(n + 1)
# list = []
# for i in range(-10, -1):
#     list.append(fib(i))
# print(list)