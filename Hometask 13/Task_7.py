# 7) Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
import re

some_str = '2022-02-28'
pattern = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', some_str)
print(pattern)
