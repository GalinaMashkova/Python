# Урок 6. Повторение списков

# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше
# заданного максимума)
list = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
min_number = int(input("Введите максимальное число: "))
max_number = int(input("Введите минимальное число: "))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)

