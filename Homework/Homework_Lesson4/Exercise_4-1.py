"""Задача 22
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества."""

import random

print('Введите числовое значение для первого набора чисел (длину массива): ')
while True:
    a = input()

    if (a.isdigit() == False) or (int(a) < 1):
        print()
        print("Ошибка. Введите числовое значение (длину массива): ")
    else:
        break

print('Введите числовое значение для второго набора чисел (длину массива): ')
while True:
    b = input()

    if (b.isdigit() == False) or (int(b) < 1):
        print()
        print("Ошибка. Введите числовое значение (длину массива): ")
    else:
        break

a = [random.randint(1, int(a)) for i in range(int(a))]
print(f'Второй набор чисел: {a}')

b = [random.randint(1, int(b)) for i in range(int(b))]
print(f'Первый набор чисел: {b}')

a_sets = set(a)
b_sets = set(b)

# a_sets = {10, 5, 15, 1286, 3, 4, 20, 0}
# b_sets = {1286, 3, 10, 0, 4, 20, 15}

fin = a_sets.intersection(b_sets)

list_fin = [*fin]

for i in range(len(list_fin) - 1):
    for j in range(len(list_fin) - 1):
        temp = 0
        if list_fin[j] > list_fin[j+1]:
            temp = list_fin[j+1]
            list_fin[j+1] = list_fin[j]
            list_fin[j] = temp

print(*list_fin)