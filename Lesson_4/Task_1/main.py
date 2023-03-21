"""Задача №25.
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2"""

str_list = 'a a a b c a a d c d d'.split()
print('a a a b c a a d c d d')

dictionary = {}

for item in str_list:
    if(not dictionary.keys().__contains__(item)):
        print(item, end=' ')
        dictionary[item] = 0
    else:
        dictionary[item] += 1
        print(F'{item}_{dictionary[item]}', end=' ')