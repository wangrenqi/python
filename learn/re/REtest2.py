import learn.re

key =  r'kjdfhsdkjfhpyq225@gmail.com2342254afsdf'

p = r'pyq225@gmail.com'

patten = learn.re.compile(p)

print patten.findall(key)