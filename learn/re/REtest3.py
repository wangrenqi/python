import learn.re

key = r"asdada<HtMl>hello</hTmL>hdsfsdfshh"

p = r"<[Hh][Tt][Mm][Ll]>.+?</[Hh][Th][Mm][Ll]>"

patten1 = learn.re.compile(p)


print patten1.findall(key)


# key = r'lalala<hTal>hello</Htal>heiheihei'
# p1 = r'<[Hh][Tt][Aa][Ll]>.+?</[Hh][Tt][Aa][Ll]>'
# pattern1 = re.compile(p1)
# print pattern1.findall(key)

# ke  = r'adasdada<aHA>aaa<aHa>'
#
# p = r'<[Aa][Hh][Aa]>.+?<[Aa][Hh][Aa]>'
#
# pat = re.compile(p)
#
# print pat.findall(ke)

