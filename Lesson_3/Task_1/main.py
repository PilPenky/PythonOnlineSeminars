"""Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6"""

import random

num = int(input("Введите количество элементов в списке: "))
list1 = list()

for i in range(num):
    list1.append(random.randint(-4, 4))

print("Дан список", list1)
list1 = set(list1)
print("В нём содержится", len(list1), "уникальных элементов:")
print(*list1)