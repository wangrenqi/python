import MySQLdb

db = MySQLdb.connect('localhost','root','forever367','testdb')

cursor = db.cursor()

sql = '''DELETE FROM EMPLOYEE WHERE AGE > '%d' ''' % (20)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()