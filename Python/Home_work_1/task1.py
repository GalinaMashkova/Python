# Урок 1. Ввод-Вывод, операторы ветвления

# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначного число: ')
number = int (input())
summa = 0
while number > 0:
     x = number % 10
     summa = summa + x
     number = number // 10
print(summa)

# n = 123
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9



