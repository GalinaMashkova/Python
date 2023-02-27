# # Урок 1. Знакомство с языком программирования Python
# a = 2
# b = 1
# print(a+b)
# print(type(a))

# c = "Hello," # создание 1-ой строки
# d = 'world' # создание 2-ой строки
# print(c+d)
# print(type(c)) ## функция, которая указывает на тип данных
# print(type(d))

# Если Вы хотите закомментировать 1 строку достаточно применить 
# специальный символ “#”, если Вам нужно закомментировать сразу 
# несколько строк выделите их и нажмите ctrl + / или же используйте 
# тройные кавычки ‘’’

# # Интерполяция — способ получить сложную строку из нескольких простых 
# # с использованием специальных шаблонов
# a = 3
# b = 11
# s = 2022
# print(a, b, s)
# print(a, '-'b, '-'s) # НЕ РАБОТАЕТ
# print('{} - {} - {}'.format(a,b,s))
# print(f'first - {a} second - {b} third - {s}')

# # Оператор ввода данных
# print('Введите 1-ое число: ')
# a = input()
# print('Введите 2-ое число: ')
# b = input()
# print(a, ' + ', b, ' = ', a + b)

# # Встроенные типы данных
# n = 1.345
# print(int(n))
# m = '345'
# print(m * 2)
# print(int(m) * 2)

# n = 1.345
# print(str(n) * 2)

# n = '1.345'
# print(float(n) * 2) 
# m = 2
# print(float(m))

# # Ввести число
# print('Введите 1-ое число: ')
# a = int (input())
# print('Введите 2-ое число: ')
# b = int (input())
# print(a, ' + ', b, ' = ', a + b)

# # Округление числа
# a = 1.43425
# b = 2.2983
# c = round(a * b, 5) 
# print(c)

# # Сравнение в Python
# a = 1 > 4
# print(a) # False
# a = 1 == 2 
# print(a) # False
# a = 1 != 2 
# print(a) # True

# a = 'qwe' 
# b = 'qwe' 
# print(a == b) # True

# a = 1 < 3 < 5 < 10
# print (a) # True

# Условия в Python
# if condition:
#  # operator 1
#  # operator 2
#  # ...
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # ...
#  # operator n + m

# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator

# Сложные условия
# if condition1 and condition2: # выполнится, когда оба условия окажутся верными
# # operator
# if condition3 or condition4: # выполнится, когда хотя бы одно из условий окажется верным
# # operator

# Цикл While
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# # Управляющие конструкции: while-else
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# # Пример программного кода без использования break:
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# # Пожалуй
# # хватит )
# # 9

# # Задача
# # Пользователь вводит число, необходимо найти минимальный делитель данного числа
# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
# i += 1

# # Цикл for, функция range()
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# # Немного о строках
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# # Срезы
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ

# text = 'съешь ещё этих мягких французских булок'
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...