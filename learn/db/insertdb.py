import MySQLdb

db = MySQLdb.connect('localhost', 'root', 'forever367', 'testdb')

cursor = db.cursor()

sql = '''INSERT INTO EMPLOYEE (FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac','Mohan',20,'M',2000)
         '''
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()


# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
#        ('Mac', 'Mohan', 20, 'M', 2000)
