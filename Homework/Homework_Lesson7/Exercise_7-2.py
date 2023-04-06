"""Задача 36: 
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

*Пример:*

**Ввод:** `print_operation_table(lambda x, y: x * y) `
**Вывод:**
1 2  3  4  5  6
2 4  6  8  10 12
3 6  9  12 15 18
4 8  12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36"""


"""ДЛЯ СЕБЯ :)"""


"""
# Вывод с помощью numpy:

import numpy as np

def operation(num_rows = 6, num_columns = 6):
    n = list()
    for i in range(1, num_columns+1):
        for j in range(1, num_rows+1):
            n.append(i * j)

    # print(n)
    splits = np.array_split(n, num_columns)
    for array in splits:
        print(*list(array))
    
    return n

operation()
"""
######################################################
# Вывод в одну строку шесть списков от 1 до 6 в списке:
"""def operation(num_rows = 6, num_columns = 6):
    n = list()
    for i in range(1, num_columns+1):
        for j in range(1, num_rows+1):
            n.append(i * j)

    sum = list()
    count = 0
    for i in range(len(n)):
        if i == count:
            tempArray = list()
            sum.append(tempArray)
            count += 6
        
        tempArray.append(n[i])
    
    return sum

print(operation())
"""
######################################################


"""НА ПРОВЕРКУ :)"""

def printOperationTable(operation, numRows = 6, numColumns = 6):
    if operation(1,1) == 2:
        print(1, end = '\t')

    for row in range(1, numRows + 1):
        for column in range(1, numColumns + 1):
            if operation(1,1) == 2:
                column = column - 1
            print(operation(row,column), end = '\t')
        print()

print(printOperationTable(lambda x, y : x * y))