# Знакомство с языком Python (семинары)
# Урок 1. Ввод-Вывод, операторы ветвления

# # Задача
# # Напишите программу, которая принимает на вход два числа и проверяет,
# # является ли одно число квадратом другого
# # Пример
# # 2, 4 ->'да'
# numberA = int(input("Введите число: "))
# numberB = int(input("Введите число: "))
# if numberA * numberA == numberB or numberB * numberB == numberA:
#     # 2 * 2 == 4 or 4 * 4 == 2
#     print('да')
# else:
#     print('нет')

# numberA = int(input("Введите число: "))
# numberB = int(input("Введите число: "))
# if numberA ** 2 == numberB or numberB ** 2 == numberA:
#     # ** Возведение в степень
#     print('да')
# else: print('нет')

# # Задача
# # Напишите программу, которая на вход принимает 5 чисел и находит максимальное число
# # Пример
# # 1, 4, 8, 7, 5->8
# # 78, 55, 36, 90, 2->90
# max = 0
# for i in range(5):
#     n = int(input("Введите число: "))
#     if n > max:
#         max = n
# print(F"Максимальное число: {max}")

# a = -21
# b = -6
# c = -35
# f = -85
# g = -654
# max = a 
# if max < b:
#     max = b
# if max < c:
#     max = c  
# if max < f:
#     max = f
# if max < g:
#     max = g
# print(max)

# # Задача
# # Напишите программу, которая будет на вход принимать число
# # Пример 5->-5,-4,-3,-2,-1,0,1,2,3,4,5
# n = int(input("Введите число: "))
# for n in range (-n, n + 1):
#     print (f"{n}", end = ' ')
#     # end - вывести в одной строке

# n = abs(int(input("Введите число: ")))
# # abs () удаляет отрицательный знак числа
# for n in range (-n, n + 1):
#     print (f"{n}", end = ' ')

# n = int(input("Введите число: "))
# result = n / abs(n)
# for n in range (-n, n + int(result), int(result)):
#     print (f"{n}", end = ' ')

# # Заполнение списка
# iis = list(map(int, input("Введите числа через пробел: ").split()))
# print(iis)
# print(iis[0]) # обращение по индексу к элементу
    
# # Задача
# # Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N 
# number = int(input("Введите число: "))
# if number < 0:
#     number = number * -1
#     # number *= -1
# for i in range(-number, number + 1):
#     print(i)

# # Пример
# # 1,2->   1
# #         2 
# n = str(float(input("Введите число: ")))
# for i in range(len(n)):
#      if n[i] == '.':
#         print(n[i + 1])

# # Задача
# # Напишите программу, которафя будет принимать на вход дробь
# # и показывать первую цифру дробной части числа
# # 6,78 -> 7
# # 5 -> нет
# # 0,34 - > 3
# number = float(input("Введите дробное число: "))
# print(int(number * 10 % 10))

# # Задача
# # Напишите программу, которая принимает на вход чмсло
# # и проверяет, кратно ли оно 5 и 10 или 15, но не 30
# number = float(input("Введите дробное число: "))
# if (number % 10 == 0 and number % 15 == 0) and number % 30 != 0:
#     print('да')
# else: print('нет')