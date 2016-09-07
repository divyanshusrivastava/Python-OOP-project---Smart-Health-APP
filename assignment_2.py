##############################
## Smart Health Application ##
######## Assignment 2 ########
##############################

## Submitted By:
	# Biswadeep Khan 		- MT16124 - M.Tech (CB)
	# Divyanshu Srivastava 	- MT16125 - M.Tech (CB)

import warnings
import copy
import MySQLdb

def disp_user_menu(uname):

	pass

#####################################
## 
## 		TEST CODE


db = MySQLdb.connect("localhost", "root","password","smarthealthdb")  
cursor = db.cursor()

print "\n\t\tOOP Python Assignment 1"
print "\t\tCode submittion by : \n"
print "\t\t\tDivyanshu Srivastava      \t\tBiswadeep Khan"
print "\t\t\t  MT16125                 \t\t  MT16124"
print "\t\t\tM. Tech (Comp. Bio.)      \t\tM. Tech (Comp. Bio.)"  
print "\t\t\tdivyanshu16125@iiitd.ac.in\t\tbiswadeep16124@iiitd.ac.in"

# waiting for user to contine
print "\n\n\t\t HIT ENTER TO BEGIN . ."
raw_input()

print '\t\t\t\t SMART HEALTH APP'
print '\n\t\t\t1. LOG IN'
print '\t\t\t2. SIGN UP'
choice = int(raw_input('\n\t\tEnter your choice: '))

if choice == 1:
	''' log in '''
	uname = raw_input('\n\tEnter username: ')
	pswd = raw_input('\tEnter password: ')
	query = "select * from user where username = '%s' and password = '%s'" % \
		(uname, pswd)

	cursor.execute(query)
	q_out = cursor.fetchall()
	print q_out
	
	if len(q_out) == 0:
		print '\n\t\tInvalid credentials !'

	else :
		print '\n\tLogin successful !\n'
		print q_out

		if q_out[15] == '1':
			''' usertype = user'''
			disp_user_menu(uname)

		elif q_out[15] == '2':
			''' usertype = administrator'''
			disp_admin_menu(uname)

		elif q_out[15] == '3':
			''' usertype = moderator'''
			disp_mod_menu(uname)

		else:
			pass 				# TODO: suitable error message
	
elif choice == 2:
	''' Sign Up '''

	print '\tEnter details\n'
	uname = raw_input('\tPreferred username: ')
	pswd = raw_input('\tPassword: ')			# TODO: replaced by **
	email1 = raw_input('\tPrimary E-mail id: ')
	email2 = raw_input('\tSecondary E-mail id: ')
	fname = raw_input('\tFirst name: ')
	lname = raw_input('\tLast name: ')
	aboutme = raw_input('\tAbout Yourself: ')
	p_url1 = raw_input('\tPhoto URL 1: ')
	p_url2 = raw_input('\tPhoto URL 2: ')
	p_url3 = raw_input('\tPhoto URL 3: ')
	street_no = raw_input('\tStreet Number: ')
	street_name = raw_input('\tStreet Name: ')
	munc = raw_input('\tMajor Muncipality: ')
	dist = raw_input('\tGoverning District: ')
	post = raw_input('\tPostal Area: ')
	utype = int(raw_input('\tUser Type (1. User, 2. Moderator, 3. Administrator): '))

	## Check if inputs are valid
	query = '''insert into user values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', \
	'%s', '%s', '%s', '%s', '%d', '%d')''' %\
	 (uname, pswd, email1, email2, fname, lname, \
			aboutme, p_url1, p_url2, p_url3, street_no, street_name, munc, dist, post, \
			utype, 1)

	cursor.execute(query)
	db.commit()
	
	if utype == 1:
	 	''' insert karma score '''

	 	pass

	if utype == 2:
		''' insert emergency phone also '''
		ephone = raw_input('\t Emergency Phone: ')

		cursor.execute('insert into administrator values ("%s", "%s")' % \
			(uname, ephone))

		db.commit()

	if utype == 3:
		''' insert emeg phone and qualification '''
		ephone = raw_input('\tEmergency Phone: ')
		cursor.execute('select * from qualification')
		qual_tuple = cursor.fetchall()
		print qual_tuple
		qual = list(raw_input('\t Academic Qualification (Insert as a list): '))
		
		for i in len(qual):
			cursor.execute('insert into moderatorqualifications values (%d, "%s", "%s")' \
				(i, uname, datetime.datetime.now().date()))
			db.commit()




	

	print query
	## Post : Fire Query

	pass
else:
	print 'Invalid option !'


# cursor.execute(query)
# db.commit()
# cursor.execute('select * from user')

# print cursor.fetchall()

db.close()