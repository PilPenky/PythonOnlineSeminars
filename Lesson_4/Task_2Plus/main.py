"""Дополнительная задача.
Посчитать количество слов в книге 'Война и мир'"""

import fileinput

with open('war_and_peace.ru.txt', encoding = 'utf-8') as f:
    text = f.read().lower().strip().replace('.', '').replace(',', '').replace(':', '').replace(';', '').replace('?', '').replace('!', '').split()

print(len(text))