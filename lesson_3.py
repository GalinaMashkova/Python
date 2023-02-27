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
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
n = int(input()) # 5
print(sumNumbers(n)) # 15