# Урок 5. Рекурсия и алгоритмы

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4 

def recurssum(a, b):
    if b == 0:
        return a
    return 1 + recurssum(a, b - 1)
print(recurssum(2, 2))

# # Цикл
# def sum(x, y):
#     if (y == 0):
#         return x
#     else:
#         return sum(x + 1, y - 1)
# a = int(input('Введите число x: '))
# b = int(input('Введите число y: '))
# if (a >= b):
#     print (sum(a, b))
# else:
#     print(sum(b, a))