# Урок 2. Циклы (for, while)

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые
# – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

n = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(n):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        orel = orel + 1
    else:
        reshka = reshka + 1
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))


# # Эталонное решение
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
#     x = int(input())
#     if x == 0:
#         count_zero += 1
#     else:
#         count_one += 1
# if count_one > count_zero:
#     print(count_zero)
# else:
#     print(count_one)