# Урок 4. Функции высшего порядка, работа с файлами

# # Анонимные, lambda-функции
# def f(x):
#     return x * 2
# print(f(2))

# def f(x):
#     return x ** 2
# g = f   

# def f(x):
#     return x ** 2
# g = f
# print(f(4)) # 16
# print(g(4)) # 16 

# def calc1(a):
#     return a + a
# def calc2(b):
#     return b * b
# def math(op, x):
#     print(op(x))
# math(calc1, 5) # 10
# math(calc2, 5) # 25

# def sum(x, y):
#     return x + y
# def mylt(x, y):
#     return x * y 
# def calc(op, a, b):
#     print(op(a, b))
# calc(mylt, 4, 5) # 20

# def calc2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))
# def calc1(a, b):
#     return a + b
# math(calc2, 5, 45) # 225
# math(calc2, 5, 45) # 50

# def calc2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))
# math(lambda a, b: a + b, 5, 45) # 50

# # Задача
# # В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар 
# # (число; квадрат числа).
# # Пример: 1 2 3 5 8 15 23 38
# # Получить: [(2, 4), (8, 64), (38, 1444)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
# print(res)

# # Как можно сделать этот код лучше, используя lambda?
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

# # Функция map
# list_1 = [x for x in range (1,20)]
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# # Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется 
# # пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# # 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем список из 
# # значений строки, пример:
# data = '1 2 3 5 8 15 23 38'
# print(data) 
# data = data.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int, data.split()))
# print(data)

# def where(f, col):
#     return [x for x in col if f(x)]
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# # Функция filter
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res) # [15, 65, 175]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

# # Функция zip
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# # Функция enumerate
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# # Файлы
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# colors = ['red', '8899', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# # Модуль os
# os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# ● os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с 
# путями, такие как:
# ○ os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

# # Модуль shutil
# import shutil

# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на 
# директорию, а не на символическую ссылку.