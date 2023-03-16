"""Задача №9.
По данному целому неотрицательному n вычислите значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while

Input: 5
Output: 120 """

number = int(input('Введите значение: '))

i = 1
result = 1

if number == 0:
    print(result)
elif number < 0:
    print('Введите целое неотрицательное число!')
else:
    while i <= number:
        result = result * i
        i = i + 1
    print(result)


