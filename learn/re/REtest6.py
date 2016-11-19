# import re
#
# key = r"chuxiuhong@hit.edu.cn"
# p1 = r"@.+\."
# pattern1 = re.compile(p1)
# print pattern1.findall(key)
# ['@hit.edu.']

# import re
# key = r'pyq225@gmail.com..a.a.a.a.b.c.d'
# p1 = r'@.+\.'
#
# patten1 = re.compile(p1)
# print patten1.findall(key)
# ['@gmail.com..a.a.a.a.b.c.']

import learn.re
key = r'pyq225@gmail.com..a.a.a.a.b.c.d'
p1 = r'@.+?\.'

patten1 = learn.re.compile(p1)
print patten1.findall(key)
# ['@gmail.']
