# 6) В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
import re

some_str = ['I human',
            'You human',
            'We human']
pattern = [re.sub(r'human', 'computer', i) for i in some_str]
print('\n'.join(pattern))
