# Урок 7. Функции высшего порядка

# # Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# # Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# # Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# # Фраза может сосcтоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# # Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# # В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# # *Пример:*
# # **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# # **Вывод:** Парам пам-пам
# # Рассмотрели на семинаре
# list1= input('Введите фразы через пробел: ')
# list1 = list1.split(' ')
# list2 = ["у", "е", "а", "о", "я", "и", "ю", "ы"]
# list3 = []

# for i in range(len(list1)):
#     count = 0
#     for j in range(len(list2)):
#         if list1[i].count(list2[j]) > 0:
#             count += list1[i].count(list2[j])
#     list3.append(count) 

# print(list3)
# if len(set(list3)) == 1:
#     print ('Парам пам-пам')
# else:
#     print('Пам парам')

# def param(poema):
#     poema = poema.split()
#     list = []
#     for i in poema:
#         sumGl = 0
#         for j in i:
#             if j in 'аеёионыэюя' :
#                 sumGl = sumGl + 1
#         list.append(sumGl)
#     return len(list) == list.count(list[0])
# text = input ('Введите фразы через пробел: ')
# if param(text):
#     print ('Парам пам-пам')
# else:
#     print('Пам парам')

# def param2(arr):
#     list = []
#     for i in arr:
#         sumGl = 0
#         for j in i:
#             if j in 'аеёионыэюя' :
#                 sumGl = sumGl + 1
#         list.append(sumGl)
#     return list

# def param(poema, fun):
#     poema = poema.split()
#     list = fun(poema)
#     return len(list) == list.count(list[0])

# text = input ('Введите фразы через пробел: ')
# if param(text, param2):
#     print ('Парам пам-пам')
# else:
#     print('Пам парам')