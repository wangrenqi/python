# import re
#
# key = r"mat cat hat pat"
# p1 = r"[^p]at"
#
# pattern1 = re.compile(p1)
# print pattern1.findall(key)
# ['mat', 'cat', 'hat']

import learn.re

key = r'mat cat hat'
p1 = r'[^p]at'

patten = learn.re.compile(p1)
print patten.findall(key)
