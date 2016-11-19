# import re
#
# key = r"saas and sas and saaas"
# p1 = r"sa{1,2}s"
# pattern1 = re.compile(p1)
# print pattern1.findall(key)
# ['saas', 'sas']

import learn.re
key = r'saaaaas and saas and sssaaass'
p1 = r'sssa{1,3}s'

pat  = learn.re.compile(p1)
print pat.findall(key)
# ['sssaaas']
