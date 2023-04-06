"""Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
Стихотворение Винни-Пух вбивает в программу с клавиатуры.
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

*Пример:*
            2   1  1   1   1    2    1  1  1  1
**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-дам
**Вывод:** Парам пам-пам  """

from turtle import*

print('Здравствуй, Винни-Пух!\nРасскажи мне, пожалуйста, стихотворение, а я скажу тебе есть ли в твоем стихотворении ритм или нет :)')
userPhrase = input()

def letterSearch(userPhrase):
    countArray = []
    count = 0

    for i in range(len(userPhrase)):

        vowels = ['А', 'Я', 'У', 'Ю', 'О', 'Е', 'Ё', 'Э', 'И', 'Ы', 'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы',
        'A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
        for j in vowels:
            if j == userPhrase[i]:
                count += 1
                break

        if userPhrase[i] == ' ':
            countArray.append(count)
            count = 0

        if i == len(userPhrase)-1:
            countArray.append(count)
            count = 0  

    return countArray 

def heart():
    speed(10)
    # Сердце
    fillcolor('red')
    begin_fill()

    up()
    goto(450, 0) # Отступ 80
    down()
    right(90)

    up()
    goto(653, 160) # Отступ 80
    down()

    right(43)
    forward(628)

    right(94)
    forward(628)

    right(53)
    circle(-221, 153)

    right(-147)
    circle(-221, 154)


    goto(653, 159)

    right(53)
    forward(628)

    end_fill()

    up()
    goto(0, 0)
    down()


    # Класс
    up()
    goto(215, 0) # Отступ 80
    down()

    right(137)
    forward(100)



    right(90)
    circle(-30, 50)

    right(40)
    forward(30)

    left(90)
    forward(30)

    circle(-8, 190)
    left(10)
    forward(30)

    left(180)
    forward(40)

    circle(-8, 190)
    left(10)
    forward(40)

    left(180)
    forward(40)

    circle(-8, 190)
    left(10)
    forward(40)

    left(180)
    forward(30)

    circle(-8, 190)
    left(10)
    forward(50)

    input()

def letterComparison(countArray):
    countTwo = 0

    if len(countArray) == 1:
        print('Винни, ну алё! Из одной фразы стихотворение не сделать :)')
        quit()

    for i in range(len(countArray)-1):
        if countArray[i] == countArray[i+1]:
            countTwo += 1
        else:
            countTwo += 0
    
    if countTwo == len(countArray)-1:
        print('Парам пам-пам, с ритмом все в порядке :)')
        heart()
    elif countTwo != len(countArray)-1:
        print('Пам парам, Винни, с ритмом не всё в порядке :( ')

letterComparison(letterSearch(userPhrase))