import learn.re

key = r'<h1>hello python<h1>'
p1 = r'<h1>.+<h1>'
patten = learn.re.compile(p1)
print patten.findall(key)
