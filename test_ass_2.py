## PYTHOn Assignment 2 test code

import MySQLdb

db = MySQLdb.connect("localhost", "root","password","smarthealthdb")  
cursor = db.cursor()



cursor.execute('select * from usertype')


print cursor.fetchall()

db.close()