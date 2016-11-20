# coding=utf-8
import re
import urllib
import MySQLdb

url = 'http://www.weather.com.cn/weather/101010100.shtml'


def getHtml(url):
    page = urllib.urlopen(url)
    result = page.read()
    page.close()
    return result


p = getHtml(url)


# print p

def getCity(html):
    key = r'<title>【(.+?)天气】.+?</title>'
    result = re.findall(key, html)
    return result[0]


print getCity(p)

db = MySQLdb.connect('localhost', 'root', 'forever367', 'testdb')
cursor = db.cursor()
sql = 'INSERT INTO weather(city) VALUES (%s)' %  [getCity(p)]
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
    print 'exception'
db.close()
print 'done'

# sql = '''INSERT INTO EMPLOYEE (FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Mac','Mohan',20,'M',2000)
#          '''
#
# 插入或更新数据有两种方法
#
# 1.
# 拼接sql语句：
#
# sql_content = "insert into table(key1,key2,key3) values (%s,%s,%s)" % (value1, value2, value3)
# cur.execute(sql_content)
# 2.
# 用问号替代
#
# sql_content = "insert into table(key1,key2,key3) values (?,?,?)"
# cur.execute(sql_content, (value1, value2, value3))