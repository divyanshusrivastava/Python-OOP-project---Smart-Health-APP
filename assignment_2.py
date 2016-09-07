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


class Person (object):

	active = False

	def __init__(self, username, email, fname, lname, address, about , url):
		self.username = username[0:20]
		self.email = email
		self.__firstname = fname
		self.__lastname = lname
		self.address = address
		self.aboutme = about
		self.url = url		# check url datatype for 3 url..maybe a tuple or
							# dictionary
		self.usertype = ''
		self.active = True

	def sign_out(self):
		self.active = False

	def print_details(self):
		print 
		print "\tUserame: \t" + self.username
		print "\tEmail ID: \t" + self.email
		print "\tAddress: \t" + self.address
		print "\tAbout Me: \t" + self.aboutme
		print "\tLink to profile photo: \t" + self.url

		

class User (Person):

	AllowedUserType = ('new', 'middle', 'old') # could be used later

	def __init__(self, karma, **args):
		self.karmaScore = karma
		super(User, self).__init__(**args)
		self.userType = 'new'

	def change_user_type(self, utype):
		if utype in self.AllowedUserType:
			self.userType = utype
		else:
			warnings.warn(str(utype + ' is not an allowed user type!'), UserWarning)

	def display(self):
		super(User, self).print_details()
		print "\tUser Type: \t" + self.userType
		print "\tKARMA score: \t" + str(self.karmaScore)

class Moderator (Person):

	AllowedQualifications = ('MD', 'MBBS', 'BHMS', 'PHD') 	# There could be 
							# more.. nood to be checked

	def __init__(self, ephone, qual, **args):
		self.emergencyContact = ephone
		if qual in self.AllowedQualifications:
			self.professionalQualification = qual
		else:
			warnings.warn(str(qual + ' is not a recognised qualification!'), UserWarning)

		super(Moderator, self).__init__(**args)
		self.userType = 'mod'

	@staticmethod
	def updateAllowedQual(qual):
		if qual not in AllowedQualifications:
			AllowedQualifications.append(qual)
		else:
			warnings.warn(qual + ' already present !')

	def display(self):
		super(Moderator, self).print_details()
		print "\tEmergency Contact: \t" + self.emergencyContact
		print "\tUser Type: \t" + self.userType
		print "\tProfessional Qualification: \t" + self.professionalQualification

class Administrator (Person):

	def __init__(self, ephone, **args):
		self.emergencyContact = ephone
		super(Administrator, self).__init__(**args)
		self.userType = 'admin'

	def display(self):
		super(Administrator, self).print_details()
		print "\tEmergency Contact: \t" + self.emergencyContact
		print "\tUser Type: \t" + self.userType




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


	pass
elif choice == 2:
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
		
	

	

	print query
	## Post : Fire Query

	pass
else:
	print 'Invalid option !'


cursor.execute(query)
db.commit()
cursor.execute('select * from user')

print cursor.fetchall()

db.close()