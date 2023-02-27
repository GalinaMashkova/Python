# Урок 2. Циклы (for, while)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


# x = abs(int(input('Введите первое натуральное число X от 1 до 1000 ')))
# y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#     print('Вы ввели число не из заданного диапазона!')
# else:
#     S = x + y
#     P = x * y
#     stop = 0
#     for i in range(1001):
#         if stop != 1:
#             for j in range(1001):
#                 if stop != 1:
#                     if i * j == P and i + j == S:
#                         print(i, j)
#                         stop = 1
#             else:
#                 j = 1001
#         else:
#             i = 1001

print('Введите 1-е натуральное число: ')
X = int (input())
print('Введите 2-е натуральное число: ')
Y = int (input())
S = X + Y
P = X * Y
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)

# # Эталонное решение
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)