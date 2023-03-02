# Знакомство с языком Python (семинары)
# Урок 4. Словари, множества и профилирование

# # Задача №25. Решение в группах
# # Напишите программу, которая принимает на вход
# # строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к
# # символам с помощью постфикса формата _n.
# # Input: a a a b c a a d c d d
# # Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# # Для решения данной задачи используйте функцию
# # .split()
# list1 = input().split()
# list2 = {}
# list3 = []
# for i in list1:
#     if i in list2:
#         list3.append(i + '_' + str(list2[i]))
#         list2[i] = list2[i] + 1
#     else:
#         list3.append(i)
#         list2[i] = 1
# print(list3)

# list = list(input().split())
# list_2 = {}
# list_3 = []
# for i in list:
#     if i in list_2:
#         list_3.append(i + "_" + str(list_2[i])) # i - это ключ, ф list_2[i] - значение по этому ключу
#         list_2[i] = list_2[i] + 1
#     else:
#         list_3.append(i)
#         list_2[i] = 1
# print(list_3)

# # Задача
# # Пользователь вводит текст(строка). Словом считается 
# # последовательность непробельных символов идущих 
# # подряд, слова разделены одним или большим числом 
# # пробелов. Определите, сколько различных слов 
# # содержится в этом тексте.
# # Input: She sells sea shells on the sea shore The shells
# # that she sells are sea shells I'm sure.So if she sells sea
# # shells on the sea shore I'm sure that the shells are sea
# # shore shells
# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# print(len(set(list(text.lower().split(' ' )))))

# # Задача
# # В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# # круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# # каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# # выросло различное число ягод – на i-ом кусте выросло ai
# #  ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым
# # кустом, собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может
# # собрать за один заход собирающий модуль, находясь перед некоторым кустом
# # заданной во входном файле грядки.
# list1 = input ('Введите через пробел количество ягод на каждом кусте: ').split()
# newlist = []
# if len(list1) >= 3:
#     for i in range (1, len(list1) - 1):
#         newlist.append(int(list1[i - 1]) + int(list1[i]) + int(list1[i + 1]))
#     newlist.append(int(list1[- 2]) + int(list1[-1]) + int(list1[0]))
#     print(newlist)
#     print('Максимальное число ягод за один заход =', max(newlist))
# else:
#     count = 0
#     for i in list1:
#         count = count + int(i)
#     print(count)

# # Задача
# # Даны два неупорядоченных набора целых чисел (может быть, с
# # повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# # встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# # элементов второго множества. Затем пользователь вводит сами элементы множеств.
# # 11 6
# # 2 4 6 8 10 12 10 8 6 4 2
# # 3 6 9 12 15 18
# # -> 6 12
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#     less = [i for i in arr[1:] if i <= pivot]
#     greater = [i for i in arr[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# list1 = input('Введите элементы первого множества: ').split()
# list2 = input('Введите элементы второго множества: ').split()
# listNew1 = []
# listNew2 = []
# listEnd = []
# for i in set(list1):
#     listNew1.append(i)
# for i in set(list2):
#     listNew2.append(i)
# listNew1 = quick_sort(listNew1)
# listNew2 = quick_sort(listNew2)
# for i in range(len(listNew1)):
#     for j in range(len(listNew2)):
#         if listNew1[i] == listNew2[j]:
#             listEnd.append(listNew1[i])
# print(listNew1)
# print(listNew2)
# print(quick_sort(listEnd))   
