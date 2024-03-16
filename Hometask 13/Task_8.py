# 8) Найти все слова, в которых есть хотя бы одна буква ‘b’
import re
some_str = 'dasdb frejknv refrbbfr b ferfqbefr efrefr bbb dsf17ertb'
pattern = re.findall(r'\b\w*b\w*\b', some_str)
print(pattern)
