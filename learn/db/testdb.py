import MySQLdb
db = MySQLdb.connect('localhost','root','forever367','testdb')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')
data = cursor.fetchone()

print 'database version : %s' % data
db.close()
