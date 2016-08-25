##############################
## Smart Health Application ##
######## Assignment 1 ########
##############################

## Submitted By:
	# Biswadeep Khan 		- MT16124 - M.Tech (CB)
	# Divyanshu Srivastava 	- MT16125 - M.Tech (CB)

import warnings
import copy

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

print "\n\t\tOOP Python Assignment 1"
print "\t\tCode submittion by : \n"
print "\t\t\tDivyanshu Srivastava      \t\tBiswadeep Khan"
print "\t\t\t  MT16125                 \t\t  MT16124"
print "\t\t\tM. Tech (Comp. Bio.)      \t\tM. Tech (Comp. Bio.)"  
print "\t\t\tdivyanshu16125@iiitd.ac.in\t\tbiswadeep16124@iiitd.ac.in"

# waiting for user to contine
print "\n\n\t\t HIT ENTER TO BEGIN . ."
raw_input()


## Person 1 - User

print "\n> Test Case 1: User"
print "  ~~~~~~~~~~~~~~~~~"

uname = "deepak_tyagi"
em = 'deepak@tyagi.com'
fn = 'deepak'
ln = 'tyagi'
add = 'B-23, Okhla, New Delhi'
abt = 'Hi there! I am a student at IIITD.'
link = 'instagram.com/deepak_tyagi'
karm = 0

user1 = User(karma = karm, username = uname, email = em, fname = fn, lname = ln, address = add, about = abt , url= link)

print "\nPrinting Details . . "
user1.display()

# changing user type
user1.change_user_type('middle')

print "\nPrinting Details after changing user_type from 'new' to 'middle' . . "
user1.display()

# waiting for user to contine
print "\n\n\t\t HIT ENTER TO CONTINUE . ."
raw_input()

## Person 2 - Moderator

print "\n> Test Case 2: Moderator"
print "  ~~~~~~~~~~~~~~~~~~~~~~"

uname = "sooraj_tyagi"
em = 'sooraj@tyagi.com'
fn = 'sooraj'
ln = 'tyagi'
add = 'B-27, Okhla, New Delhi'
abt = 'Hi there! I am a moderator at IIITD.'
link = 'instagram.com/deepak_tyagi'
ephon = '9090909090'
qua = 'MD'

mod1 = Moderator(ephone = ephon, qual = qua, username = uname, email = em, fname = fn, lname = ln, address = add, about = abt , url= link)

print "\nPrinting Details . . "
mod1.display()

# waiting for user to contine
print "\n\n\t\t HIT ENTER TO CONTINUE . ."
raw_input()

## Person 3 - Administrator

print "\n> Test Case 3: Administrator"
print "  ~~~~~~~~~~~~~~~~~~~~~~~~~~"

uname = "pankaj_tyagi"
em = 'pankaj@tyagi.com'
fn = 'pankaj'
ln = 'tyagi'
add = 'B-25, Okhla, New Delhi'
abt = 'Hi there! I am an admin at IIITD.'
link = 'instagram.com/pankaj_tyagi'
ephon = '7898789909'

admin1 = Administrator(ephone = ephon, username = uname, email = em, fname = fn, lname = ln, address = add, about = abt , url= link)

print "\nPrinting Details . . "
admin1.display()

# waiting for user to contine
print "\n\n\t\t HIT ENTER TO CONTINUE . ."
raw_input()


## Storing multiple users in a list to illustrate updation and deletion
## Admin and Mod can also be managed accordingly

print "\nInserting 3 More Users . . "
user_list = [user1]

user2 = copy.deepcopy(user1)
user2.username = 'sooraj_tyagi'
user_list.append(user2)

user3 = copy.deepcopy(user2)
user3.username = 'gajraj_tyagi'
user_list.append(user3)

print "\nInsertion Complete . . "
print "\nPrinting All Users . . "
for index, user in enumerate(user_list):
	print "\tS.no: " + str(index+1) + "\tUsername: " + user.username

print "\nDeletion : Input username you wish to delete : ",
temp = raw_input()

flag = False	
for index, user in enumerate(user_list):
	if user.username == temp:
		del user_list[index]
		flag = True
		print "\nDeletion Successful!"
		break

if not flag:
	warnings.warn("Input username not found")

print "\nPrinting All Users . . "
for index, user in enumerate(user_list):
	print "\tS.no: " + str(index+1) + "\tUsername: " + user.username


print "\n\t\tHIT ENTER TO EXIT .. "
raw_input()