"""Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива

Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
"""

def inputable(n): 
    return [input(f'элемент {i+1}: ') for i in range(n)]

N = int(input('Введите количество элементов первого массива N: '))
arrayN = inputable(N)
print(arrayN)

M = int(input('Введите количество элементов второго множества M: '))
arrayM = inputable(M)
print(arrayM)

outpootArray = []
for i in arrayN:
    if i not in arrayM: 
        outpootArray.append(i)
print(outpootArray)

#print(list(filter(lambda x: x not in arrayM, arrayN)))