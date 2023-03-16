"""Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
Пример:
5 -> 1 0 1 1 0
2
"""
import random

while True:
    n = int(input("Введите количество монет: "))

    if n <= 0 == False:
        print('Чего?! Монет нет?!')
    else:
        break

coins = list()

for i in range(int(n)):
    coins.append(random.randint(0, 1))

print(coins)


if n == 1:
    tempCoins = ""
    if coins[i] == 1:
        tempCoins = 'решкой'
    else:
        tempCoins = 'орлом' 
    
    print(f'Монета одна, лежит {tempCoins} вверх и переворачивать её не нужно.\nИли Вы хотите её перевернуть? (yes/no)')
    a = input()
    if a == 'yes':

        n = 0

        if tempCoins == 'решкой':
            tempCoins = 'орлом' 
        else:
            tempCoins = 'решкой'
        
        while True:

            for i in range(4):
                print(f'[{n}] - Монета лежит {tempCoins} вверх. Довольны теперь? (yes/no)')
                
                q = str(input())
                
                if n == 0:
                    n = 1
                else:
                    n = 0

                if tempCoins == 'решкой':
                    tempCoins = 'орлом' 
                else:
                    tempCoins = 'решкой'

                if q == 'yes':   
                    print("До свидания, довольный человек :)")
                    quit()
            print('ДА ТЫ ДОСТАЛ!')
            quit()
    else:
        print("До свидания")

head = 0
tail = 0

for i in range(int(n)):
    if coins[i] == 0:
        tail += 1
    else:
        head += 1

print(f'Решка: {head}')
print(f'Орел: {tail}')

count = 0
for i in range(int(n-1)):
    if coins[i] == coins[i + 1]:
        count += 1
        if count == n-1:
            print('Монеты уже повернуты вверх одной и той же стороной.')
            quit()
    
if head == tail:
    print(f'Количество перевернутых монет разными сторонами одинаковое.\nМинимальное количество монет, которые нужно перевернуть: {head}')
elif head > tail:
    print(f'Минимальное количество монет, которые нужно перевернуть: {tail}, орел.')
elif head < tail:
    print(f'Минимальное количество монет, которые нужно перевернуть: {head}, решка.')