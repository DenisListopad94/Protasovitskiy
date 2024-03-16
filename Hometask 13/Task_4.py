# 4) Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
import re
vowels = 'аяуюоеёэиыАЯУЮОЕЁЭИЫ'
some_str = 'апельсин фрукт помидор овощ'
pattern = re.findall(r'\b[' + vowels + r'][а-яА-Я]*\b', some_str)
print(pattern)
