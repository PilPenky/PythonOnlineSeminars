"""Задача 28: 
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4"""

import random

print('Введите первое число: ')
while True:
    a = input()

    if (a.isdigit() == False) or (int(a) < 1):
        print()
        print("Ошибка. Введите число больше нуля: ")
    else:
        break

print('Введите второе число: ')
while True:
    b = input()

    if (b.isdigit() == False) or (int(b) < 1):
        print()
        print("Ошибка. Введите число больше нуля: ")
    else:
        break

def sum_nums(a, b):
    if int(b) == 0:
        return 1
    if b != 0:
        return int(a) + sum_nums(int(a)-(int(a)-1), int(b)-1)


print(f'{a} + {b} = {sum_nums(a, b)}')