"""*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 

А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
12  """

n = input('Введите слово: ')

# Реализация проверки на ввод языка:
countEng = 0
ascii = 0
for i in range(len(n)):
    for j in range(ord('A'), ord('Z') + 1):
        if chr(j) == n[i]:
            countEng += 1
            for i in [65, 69, 73, 76, 78, 79, 82, 83, 84, 85]:
                if ord(chr(j)) == i:
                    ascii += 1
                    break

            for i in [68, 71]:
                if ord(chr(j)) == i:
                    ascii += 2
                    break

            for i in [66, 67, 77, 80]:
                if ord(chr(j)) == i:
                    ascii += 3
                    break

            for i in [70, 72, 86, 87, 89]:
                if ord(chr(j)) == i:
                    ascii += 4
                    break

            for i in [75]:
                if ord(chr(j)) == i:
                    ascii += 5
                    break

            for i in [74, 88]:
                if ord(chr(j)) == i:
                    ascii += 8
                    break

            for i in [81, 90]:
                if ord(chr(j)) == i:
                    ascii += 10
                    break

            break
    else:
        for k in range(ord('a'), ord('z') + 1):
                if chr(k) == n[i]:
                    countEng += 1
                    for i in [97, 101, 105, 111, 117, 108, 110, 115, 116, 114]:
                        if ord(chr(k)) == i:
                            ascii += 1
                            break

                    for i in [100, 103]:
                        if ord(chr(k)) == i:
                            ascii += 2
                            break

                    for i in [98, 99, 109, 112]:
                        if ord(chr(k)) == i:
                            ascii += 3
                            break

                    for i in [102, 104, 118, 119, 121]:
                        if ord(chr(k)) == i:
                            ascii += 4
                            break

                    for i in [107]:
                        if ord(chr(k)) == i:
                            ascii += 5
                            break

                    for i in [106, 120]:
                        if ord(chr(k)) == i:
                            ascii += 8
                            break

                    for i in [113, 122]:
                        if ord(chr(k)) == i:
                            ascii += 10
                            break
                    break


else:
    countRus = 0

    for i in range(len(n)):
        for j in range(ord('А'), ord('Я') + 1):
            if chr(j) == n[i]:
                countRus += 1
                for i in [1040, 1042, 1045, 1048, 1053, 1054, 1056, 1057, 1058]:
                    if ord(chr(j)) == i:
                        ascii += 1
                        break

                for i in [1044, 1050, 1051, 1052, 1055, 1059]:
                    if ord(chr(j)) == i:
                        ascii += 2
                        break

                for i in [1041, 1043, 1025, 1068, 1071]:
                    if ord(chr(j)) == i:
                        ascii += 3
                        break

                for i in [1049, 1067]:
                    if ord(chr(j)) == i:
                        ascii += 4
                        break

                for i in [1046, 1047, 1061, 1062, 1063]:
                    if ord(chr(j)) == i:
                        ascii += 5
                        break

                for i in [1064, 1069, 1070]:
                    if ord(chr(j)) == i:
                        ascii += 8
                        break

                for i in [1060, 1065, 1066]:
                    if ord(chr(j)) == i:
                        ascii += 10
                        break
                break
        else:
            for k in range(ord('а'), ord('я') + 1):
                    if chr(k) == n[i]:
                        countRus += 1
                        for i in [1072, 1074, 1077, 1080, 1085, 1086, 1088, 1089, 1090]:
                            if ord(chr(k)) == i:
                                ascii += 1
                                break

                        for i in [1076, 1082, 1083, 1084, 1087, 1091]:
                            if ord(chr(k)) == i:
                                ascii += 2
                                break

                        for i in [1073, 1075, 1105, 1100, 1103]:
                            if ord(chr(k)) == i:
                                ascii += 3
                                break

                        for i in [1081, 1099]:
                            if ord(chr(k)) == i:
                                ascii += 4
                                break

                        for i in [1078, 1079, 1093, 1094, 1095]:
                            if ord(chr(k)) == i:
                                ascii += 5
                                break

                        for i in [1096, 1101, 1102]:
                            if ord(chr(k)) == i:
                                ascii += 8
                                break

                        for i in [1092, 1097, 1098]:
                            if ord(chr(k)) == i:
                                ascii += 10
                                break
                        break

if (countEng < len(n)) and (countRus < len(n)):
    print('Ошибка. Нужно ввести слово, которое содержит либо только английские, либо только русские буквы.')
if (countEng == len(n)) or (countRus == len(n)):
    print(f'Стоимость введенного слова составляет: {ascii}')