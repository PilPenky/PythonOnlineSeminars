"""Задача 8:
Требуется определить, можно ли от шоколадки размером n x m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

Пример:
3 2 4 -> yes
3 2 1 -> no """

while True:
    x = input('Укажите ширину шоколадки: ')
    y = input('Укажите высоту шоколадки: ')

    if (x.isdigit() == False or y.isdigit() == False) or (int(x) == 1 and int(y) == 1):
        if x.isdigit() == False or y.isdigit() == False:
            print('Ошибка. Введите данные цифрами:')
            print()
        else:
            print('У вас очень странные представления о шоколадках :)\nВведите данные еще раз:')
            print()
    else:
        break  

# Рисую шоколадку:
print('Ваша шоколадка: ')
r = range(int(y))
for i in r:
    rr = range(int(x))
    for i in rr:
        print('0', end = " ")
    print()

print()

z = int(input('Укажите, сколько долек хотите отломить от шоколадки: '))
print()

if (z < int(x)) and (z < int(y)):
    print('Отломить нельзя')
elif z > (int(x) * int(y)):
    print('Отломить не получается, в шоколадке нет столько долек.')
elif z == (int(x) * int(y)):
    print('Ломать не нужно, забирайте шоколадку целиком.\nКушайте одни и в темноте :)')
elif (z >= int(x)) or (z >= int(y)): # Проверка по ширине
    rx = range(int(x), int(x) * int(y) + 1, int(x))
    for i in rx:
        if i == z:
            print('Можете отломить :)')
            break
    else:
        if (z >= int(x)) or (z >= int(y)): # Проверка по высоте
            ry = range(int(y), int(x) * int(y) + 1, int(y))
            for j in ry:
                if j == z:
                    print('Можете отломить :)')
                    break
            else:
                if (z >= int(x)) or (z >= int(y)):
                    print('Отломить нельзя :(')
else:
    print('Отломить нельзя ПОСЛЕДНЕЕ')