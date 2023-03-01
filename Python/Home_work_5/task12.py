# Урок 5. Рекурсия и алгоритмы

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

x = int(input('Введите число A: '))
y = int(input('Введите число B: '))

def exponentiation(a, n):
    if (n == 1):
        return a
    else:
        return a * exponentiation(x, n - 1)
print(exponentiation(x, y))