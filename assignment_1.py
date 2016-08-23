##############################
## Smart Health Application ##
######## Assignment 1 ########
##############################

## Submitted By:
	# Biswadeep Khan - MT16124 - M.Tech (CB)
	# Divyanshu Srivastava - MT16125 - M.Tech (CB)

import warnings

class Person (object):

	active = False

	def __init__(self, username, email, fname, lname, address, about , url):
		self.username = username
		self.email = email
		self.firstname = fname
		self.lastname = lname
		self.address = address
		self.aboutme = about
		self.url = url		# check url datatype for 3 url..maybe a tuple or
							# dictionary
		self.usertype = ''
		self.active = True

	def sign_out(self):
		self.active = False

	def change_user_type(self, utype):
		self.usertype = utype

class User (Person):

	AllowedUserType = ('new', 'middle', 'old') # could be used later

	def __init__(self, karma, **args):
		self.karmaScore = karma
		super(User, self).__init__(**args)
		self.userType = 'new'

	def change_user_type(self, utype):
		if utype in self.AllowedUserType:
			super(User, self).change_user_type(utype)
		else:
			warnings.warn(str(utype + ' is not an allowed user type!'), UserWarning)

class Moderator (Person):

	AllowedQualifications = ('MD', 'MBBS', 'BHMS', 'PHD') 	# There could be 
							# more.. nood to be checked

	def __init__(self, ephone, qual, *args):
		self.emergencyContact = ephone
		if qual in self.AllowedQualifications:
			self.professionalQualification.append = qual
		else:
			warnings.warn(str(qual + ' is not a recognised qualification!'), UserWarning)

		super(Moderator, self).__init__(*args)
		self.userType = 'mod'

	@staticmethod
	def updateAllowedQual(qual):
		if qual not in AllowedQualifications:
			AllowedQualifications.append(qual)
		else
			warnings.warn(qual + ' already present !')

class Administrator (Person):

	def __init__(self, ephone, *args):
		self.emergencyContact = ephone
		Super(Administrator, self).__init__(*args)
		self.userType = 'admin'


## Initializing objects and Testing
# User

uname = "deepak_tyagi"
em = 'deepak@tyagi.com'
fn = 'deepak'
ln = 'tyagi'
add = 'B-23, Okhla, New Delhi'
abt = 'Hi there! I am a student at IIITD.'
link = 'instagram.com/deepak_tyagi'
karm = 0

user1 = User(karma = karm, username = uname, email = em, fname = fn, lname = ln, address = add, about = abt , url= link)
user1.change_user_type('sexy')
