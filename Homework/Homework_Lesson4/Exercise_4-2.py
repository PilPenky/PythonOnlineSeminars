"""Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки."""

import random

print('Введите количество кустов черники: ')
while True:
    a = input()

    if (a.isdigit() == False) or (int(a) < 1):
        print()
        print("Ошибка. Введите числовое значение количества кустов черники: ")
    else:
        break

bushes = [random.randint(2, 10) for i in range(int(a))]

print(bushes)

list_berries = []

# Реализация обычным методом: x(3) = (y-1) + y + (y+1)
# for i in range(len(bushes)):
#     if i == 0:
#         list_berries.append(bushes[len(bushes) - 1] +  bushes[i]+ bushes[i + 1])

#     elif i == len(bushes) - 1: # Последний
#         list_berries.append(bushes[i - 1] +  bushes[i] + bushes[0])

#     elif i > 0 and i < len(bushes) - 1:
#         list_berries.append(bushes[i - 1] +  bushes[i] + bushes[i + 1])

# print(list_berries)


# Улучшенная реализация: x(3) =  Sum = (y-1) + y + (y+1).  Sum - (y-1) + (y+1)
# Находим сумму первых трех элементов массива, а в последующих итерациях от суммы вычитаем первый элемент и прибавляем четвертый(с последующий увеличением индекса)
sum_berries = 0
index = 1
max = 0
indexBush = []

for i in range(len(bushes)):
    
    if i == 0:
        list_berries.append(bushes[len(bushes) - 1] +  bushes[i]+ bushes[i + 1])
        if list_berries[i] > max:
            max = list_berries[i]
            indexBush.append(i)

    elif i == len(bushes) - 1:
        list_berries.append(bushes[i - 1] +  bushes[i] + bushes[0])
        if list_berries[i] >= max:
            if list_berries[i] == max:
                indexBush.append(i)
            else:
                max = list_berries[i]
                indexBush.clear()
                indexBush.append(i)
    
    elif i > 0 and i < len(bushes) - 1:

        if i == 1:
            for k in range(3):
                sum_berries = sum_berries + bushes[k]
            list_berries.append(sum_berries)

        else:
            list_berries.append(sum_berries - bushes[index - 1] + bushes[index + 2])
            sum_berries = list_berries[i]
            index += 1

        if list_berries[i] >= max:
            if list_berries[i] == max:
                indexBush.append(i)
            else:
                max = list_berries[i]
                indexBush.clear()
                indexBush.append(i)


print(list_berries)
print(f'Максимальное число ягод собирающий модуль собрал находясь на кусте(ах) под индексом(ами) {indexBush}, в количестве {max}.')