""" Задача 2:
Найдите сумму цифр трехзначного числа.
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

print("Введите трехзначное число: ")

while True:
    number = int(input())

    if (number < 100 or number > 999):
        print("Ошибка. Введите трехзначное число: ")
    else:
        break

sum = 0

r = range(3)
for i in r:
    a = number % 10   # number %= 10
    sum = sum + a
    number = number // 10
print(sum)