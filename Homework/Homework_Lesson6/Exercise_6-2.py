"""Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""

import random

def inputArray(a):
    print(a)
    while True:
        a = input()
        
        if (a.isdigit() == False) or (int(a) < 1):
            print()
            print("Ошибка. Введите числовое значение (длину массива): ")
        else:
            a = [random.randint(0, 100) for i in range(int(a))]
            break
    return a

a = inputArray('Введите длину массива: ')
print(a)

def inputAB(a):
    print(a)
    while True:
        a = input()

        if (a.isdigit() == False) or (int(a) < 0):
            print()
            print("Ошибка. Введите число больше нуля: ")
        else:
            break
    return a

def rangeN(max, min, a):
    list_1 = []
    for i in range(len(a)):
        if (a[i] >= int(min)) and (a[i] <= int(max)):
            list_1.append(i)
    return list_1

min = inputAB('Введите минимальное значение диапазона: ')
max = inputAB('Введите максимальное значение диапазона: ')
print(rangeN(max, min, a))