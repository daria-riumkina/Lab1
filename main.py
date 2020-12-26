import re

text = open('steam_description_data.csv', 'r')
string = text.read()
symbols = len(string)  # количество символов
wo_space = len(re.sub(r' ', '', string))  # количество символов без пробела
wo_punct = len(re.sub(r'[-:;,.!?]\s', '', string))  # количество символов без знаков препинания
words = len(re.split(r' ', string))  # количество слов
new_text = re.sub(r'[.!?]\s', r'|', string)
sentences = len(new_text.split('|'))  # количество предложений

print('В этом тексте', symbols, 'символов')
print('В этом тексте', wo_space, 'символов без пробелов')
print('В этом тексте', wo_punct, 'символов без знаков препинания')
print('В этом тексте', words, 'слов')
print('В этом тексте', sentences, 'предложений')
print(re.sub(r'[-:;,.!?]\s', '', string))

text.close()
