# 1) Вам дана строка.
# Выведите все подстроки, содержащие "cat".
import re

some_str = "catkjfherjkfhc athegfhet catcatefgehrgcatbty tybcatvrthvrhcat"
pattern = re.findall(r'cat', some_str)
print(pattern)
