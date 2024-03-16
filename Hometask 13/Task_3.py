# 3) Номер должен быть длиной 10 знаков и начинаться с 8 или 9.
# Есть список телефонных номеров, и нужно проверить их, используя регулярные выражения в Python
import re

some_numbers = ["89991234562", "81234567890", "7777777777", "9123456789", "812345678901", "8123456789"]
pattern_string = ' '.join(some_numbers)
pattern = re.findall(r'\b[8|9]\d{9}\b', pattern_string)
print(pattern)
