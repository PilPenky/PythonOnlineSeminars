"""Задача №15.
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

import random

n = input("Введите количество арбузов: ")
melon_weight = list()

for i in range(int(n)):
    melon_weight.append(random.randint(1, 10))

print(melon_weight)

min = melon_weight[0]
max = melon_weight[0]

for i in range(int(n)):
    if(melon_weight[i] < min):
        min = melon_weight[i]
    if(melon_weight[i] > max):
        max = melon_weight[i]
print('min = ', min)
print('max = ', max)