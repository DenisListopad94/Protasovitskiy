# 2) Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
import re


text = 'brvrbrbrze tgz z1d)z a43fg z*3nz frez34<zferf'
pattern = re.findall(r'z...z', text)
print(pattern)
