# Знакомство с языком Python (семинары)
# Урок 2. Циклы (for, while)

# # Задача
# # По целому неотрицательному n вычислите значение N! N! = 1 * 2 * 3 * ... * N (произведение всех чисел от 1 до N) 0! = 1
# # Решить задачу используя цикл while.
# # Пример
# # 5 -> 120
# n = int(input("Введите число: "))
# i = 1
# s = n 
# while i < n:
#     s = i * s 
#     i = i + 1
# print(s)

# n = int(input("Введите конечное число: "))
# fact = 1
# list1 = [i for i in range(1, n + 1)]
# print(list1)
# for i in list1:
#     fact = fact * i 
# print(fact)

# # Дано натуральное число А > 1. Определите, каким по счету числом Фибоначи оно является,
# # т.е. выведите такое число n, что Фибоначи(n) = A.
# # Если А не является числом Фибоначи, выведите число -1.
# # # Пример
# # # 5 -> 6
# # Числа Фибоначчи первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
# n = int(input('Введите число: '))
# a = 0
# b = 1
# count = 1
# while b < n:
#     sum = a + b
#     a = b
#     b = sum
#     count = count + 1
# if b == n:
#     print(count)
#     # print(f"{n} число фибоначи ")
# else:
#     print(-1)

# n = int(input("Введите число: "))
# list = []
# i = 0
# k = 0
# j = 2
# while i < 2:
#     list.append(i)
#     i = i + 1
# print(list)
# while j < n + 2:
#     k = list[j - 2] + list[j - 1]
#     list.append(k)
#     j = j + 1
# i = 0
# for i in range(len(list)):
#     if n == list[i]:
#         print ('Это число фибоначи')
# print('Это простое число')

# recursive_lambda = (lambda func: lambda *args: func(func, *args))
# s = [recursive_lambda(lambda a, b: b * a (a, b - 1) if b > 0 else 1) (i) for i in range(7)]
# print(s)

