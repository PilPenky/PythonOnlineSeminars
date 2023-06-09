"""Задача №7.
Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
Если год является високосным, то выведите YES, иначе выведите NO. 
Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.
Input: 2016
Output: YES
"""

"""Любой год, который делится на 4 без остатка, является високосным годом: например, 1988, 1992 и 1996 годы являются високосными годами.
Тем не менее, есть еще небольшая ошибка, которая должна быть учтена. Чтобы устранить эту ошибку, григорианский календарь предусматривает, что год, 
который делится без остатка на 100 (например, 1900) является високосным годом только в том случае, если он также без остатка делится на 400.

По этой причине следующие годы не являются високосными:
1700, 1800, 1900, 2100, 2200, 2300, 2500, 2600
Это потому, что они делятся без остатка на 100, но не на 400.

Следующие годы – високосные: 1600, 2000, 2400
Это потому, что они делятся без остатка на 100 и 400."""


year = int(input('Введите год: '))

if (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
    print("YES")
else:
    print("NO")