# Урок 3. Функции, рекурсия, алгоритмы

# Функции и модули
# Задача
# Необходимо создать функцию sumNumbers(n), которая будет
# считать сумму всех элементов от 1 до n.
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)
# n = int(input()) # 5
# sumNumbers(n) # 15

# Задача
# Программный код, который мы написали прекрасно справляется с
# поставленной задачей. Давайте изменим наш код и добавим в него
# return. НО перед этим давайте вспомним, что делает return:

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# n = int(input()) # 5
# print(sumNumbers(n)) # 15

# # Модульность
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     return # выход из функции

# # Возмоность передачи неограниченного 
# # количества аргументовж
# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))# asdw
# print(concatenatio('a', '1')) # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# Рекурсия
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2) 

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i - 2))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Быстрая сортировка
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))