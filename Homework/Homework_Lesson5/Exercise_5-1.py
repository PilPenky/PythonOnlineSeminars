"""Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

import random

print('Введите число: ')
while True:
    a = input()

    if (a.isdigit() == False) or (int(a) < 1):
        print()
        print("Ошибка. Введите число больше нуля: ")
    else:
        break

c = 0

print('Введите степень, в которую нужно увеличить число: ')
while True:
    b = input()
        
    try:
        if int(b) < 0:
            c = b
            b = int(b) * -1
            break
    except Exception:
        print()

    if b.isdigit() == False:
        print("Ошибка. Введите степень, в которую нужно увеличить число - положительное или отрицательное числ: ")

    else:
        break
        

def rec_degree(a, b):
    if b == 0:
        return 1
    else:
        if int(b) < 1:
            return 1
        return int(a) * rec_degree(int(a), int(b)-1)
        quit()

print()
if int(c) == 0:
    print(f'{a}^{b} = {rec_degree(a, b)}')
else:
    sum = 1 / rec_degree(a, b)

    print(f'{a}^{b} = {"{0:.5f}".format(sum)}')