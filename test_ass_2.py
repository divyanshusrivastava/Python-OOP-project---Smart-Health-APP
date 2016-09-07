## PYTHOn Assignment 2 test code

import MySQLdb
import datetime

db = MySQLdb.connect("localhost", "root","password","smarthealthdb")  
cursor = db.cursor()


cursor.execute('select * from qualification')
qual_tuple = cursor.fetchall()
print datetime.datetime.now()
print len(qual_tuple)

for i in range(1, len(qual_tuple)+1):
	print i

db.close()