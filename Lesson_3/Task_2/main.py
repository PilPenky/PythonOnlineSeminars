"""Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]"""

import random

my_list = [random.randint(10, 100) for _ in range(random.randint(5, 10))]
k = 3
n = len(my_list) - k
print(my_list)
while n > 0:
    item = my_list.pop()
    my_list.insert(0, item)
    n -= 1

print(my_list)