"""Задача №43.
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3

Вывод:
2
"""

import random

print('Введите числовое значение (длина массива): ')
while True:
    a = input()

    if (a.isdigit() == False) or (int(a) < 1):
        print()
        print("Ошибка. Введите числовое значение (длина массива): ")
    else:
        break

numbers = [random.randint(1, 21) for i in range(int(a))]
print(numbers)

count = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

print(count)
