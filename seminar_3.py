# Знакомство с языком Python (семинары)
# Урок 3. Списки и словари

# # Задача
# # Дан список чисел. Определите, сколько в нем 
# # встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6
# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print (len(set(list_1)))

# # Задача
# # Дана последовательность из N целых чисел и число 
# # K. Необходимо сдвинуть всю последовательность 
# # (сдвиг - циклический) на K элементов вправо, K – 
# # положительное число.
# # Input: [1, 2, 3, 4, 5] k = 3
# # Output: [4, 5, 1, 2, 3]
# list = [1, 2, 3, 4, 5]
# list = list[3: ] + list [0: len(list) - 2]
# print(list)

# list = [1, 2, 3, 4, 5]
# k = 0
# for j in range(2):
#     for i in range(len(list) - 1):
#         k = list[i]
#         list[i] = list[i + 1]
#         list[i + 1] = k
#         print(list)

# # Задача
# # Напишите программу для печати всех уникальных 
# # значений в словаре. 
# # Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# # {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# listNew = []
# for a in list:
#     for item in a: # for (k, v) in dictionary.items():
#         listNew.append(a[item])
# print(set(listNew))

# # Задача.
# # Дан массив, состоящий из целых чисел. Напишите 
# # программу, которая подсчитает количество 
# # элементов массива, больших предыдущего (элемента 
# # с предыдущим номером) 
# # Input: [0, -1, 5, 2, 3]
# # Output: 2 (-1 < 5, 2 < 3)
# list = [0, -1, 5, 2, 3]
# x = 0
# for i in range(1, len(list)):
#     if list[i] > list[i - 1]:
#         x = x + 1
# print(x)

# list = []
# for i in range(7):
#         list.append(i)
# print(list)

# list_1 = [i * i for i in range (7)]
# print(list_1)