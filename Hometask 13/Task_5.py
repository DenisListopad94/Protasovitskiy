# 5) Дана строка. Вывести все числа этой строки, как отрицательные, так и положительные.
import re

some_str = 'brg123.567779tynby10 vrv11123vtb 4 11 -7 vrgrg2.6bgb -17.5'
pattern = re.findall(r'-?\d+\.?\d*', some_str)
print(pattern)
