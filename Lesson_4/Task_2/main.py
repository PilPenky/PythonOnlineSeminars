"""Задача №27.
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13"""

source_string = 'She sells sea shells on the sea shore The shells that she sells are sea shells I\'am sure. So if she sells sea shells on the sea shore I\'am sure that the shells are sea shore shells'

source_string = source_string.replace('.', '')
source_string = source_string.lower()


word_list = source_string.split()
print(word_list)
words_unique = set(word_list)
print(words_unique)
length = len(words_unique)
print(length)