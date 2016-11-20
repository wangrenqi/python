# coding=utf-8
import MySQLdb
import sys

print '系统默认编码' + sys.getdefaultencoding()

#FUCK 2.7

db = MySQLdb.connect('localhost', 'root', 'forever367', 'testdb')

cursor = db.cursor()

# str1 = '上海'
# str2 = str1.decode('gb2312').encode('utf-8')
# sql = '''INSERT INTO weather(city) VALUES('%s')''' % (str2)

# sql1 = sql
# sql2 = sql1.decode('gbk').encode('utf-8')

# 注意%s要用''括起来。。


# u = '中文' #指定字符串类型对象u
# str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
# u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象u1
# u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容

s = '上海'
s1 = s.decode('ascii').encode('utf-8')
sql = '''INSERT INTO weather(city) VALUES('%s')''' % (s1)


try:
    cursor.execute(sql)
    db.commit()
except:
    print 'exception'
    db.rollback()
db.close()

print 'done'

# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
