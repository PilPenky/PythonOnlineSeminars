"""Задача 6: 
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no"""

print("Введите шестизначное число: ")
   
while True:
    NumberTicket = input()

    if (NumberTicket.isdigit() == False) or (int(NumberTicket) < 100000 or int(NumberTicket) > 999999):
        print()
        print("Ошибка. Введите шестизначное число: ")
    else:
        break
# isdigit() возвращает True, если все символы являются цифрами и есть хотя бы один символ (строка является не пустой и не состоит из пробелов), в противном случае False.

FirstPartNT = int(NumberTicket) // 1000
sumFP = 0
r = range(3)
for i in r:
    a = FirstPartNT % 10
    sumFP = sumFP + a
    FirstPartNT = FirstPartNT // 10


SecondPartNT = int(NumberTicket) % 1000
sumSP = 0
r = range(3)
for i in r:
    a = SecondPartNT % 10
    sumSP = sumSP + a
    SecondPartNT = SecondPartNT // 10

if sumFP == sumSP:
    text = ('0000000000000000000000000\n' 
            '0000011111100011111100000\n' 
            '0000100000001000000010000\n' 
            '0001000000000000000001000\n' 
            '00100000000БИЛЕТ000000100\n' 
            '00110000СЧАСТЛИВЫЙ0001100\n' 
            '0000110000000000000110000\n' 
            '0000001100000000011000000\n' 
            '0000000010000000100000000\n' 
            '0000000001100011000000000\n' 
            '0000000000001000000000000\n'  
            '0000000000000000000000000')
    print(text.replace('0',' '))
else:
    print()
    print('Билет не счастливый :(')