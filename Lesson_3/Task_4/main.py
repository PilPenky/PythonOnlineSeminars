"""Задача №23.
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

import random

my_list = [random.randint(1, 10) for _ in range(random.randint(5, 10))]
print(my_list)
count = 0

for index in range(len(my_list)):
    if index > 0 and my_list[index] > my_list[index - 1]:
        count += 1

print(count)