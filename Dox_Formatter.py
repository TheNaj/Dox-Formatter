import time
import sys

print("""

________                  __________                              __________             
___  __ \_________  __    ___  ____/___________________ _________ __  /__  /_____________
__  / / /  __ \_  |/_/    __  /_   _  __ \_  ___/_  __ `__ \  __ `/  __/  __/  _ \_  ___/
_  /_/ // /_/ /_>  <      _  __/   / /_/ /  /   _  / / / / / /_/ // /_ / /_ /  __/  /    
/_____/ \____//_/|_|      /_/      \____//_/    /_/ /_/ /_/\__,_/ \__/ \__/ \___//_/     


+================================================================================================+
""")

time.sleep(2.5)

print("""
______                        
___  /______  __              
__  __ \_  / / /              
_  /_/ /  /_/ /               
/_.___/_\__, /                
       /____/                 
_____   __      _____________ 
___  | / /_____ ______(_)__(_)
__   |/ /_  __ `/____  /__  / 
_  /|  / / /_/ /____  / _  /  
/_/ |_/  \__,_/ ___  /  /_/   
                /___/         
\n
""")

#First welcoming message explaining how the tool works
print("""Welcome to Naji's command line Dox Formatter! Please enter down below which bit of informtation you'd like to record.
If you want to at any moment quit formatting and save your dox format, please press "f" at any input. If at any moment you want
to exit to program, press "x".

1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other
\n
""")

#Functions of every single option to append to the dox. Asks an input for the value, appends names list to WriteName then
#prints out how many names you have total and the number. Goes back to the main loop and asks again for what you want. This process repeats
#for all functions.
def Name():
	WriteName = input("What names would you like to add?: ")
	if WriteName == 'x' or WriteName == 'X':
		print("Exiting...")
		sys.exit()
	elif WriteName == 'f' or WriteName == 'F':
		PrintDox()
	else:
		names.append(WriteName)
		print('\n')
		print(names)
		print(f"You have {len(names)} name(s) so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

def Addr():
	WriteAddr = input("What addresses would you like to add?: ")
	if WriteAddr == 'x' or WriteAddr == 'X':
		print("Exiting...")
		sys.exit()
	elif WriteAddr == 'f' or WriteAddr == 'F':
		PrintDox()
	else:
		addr.append(WriteAddr)
		print('\n')
		print(addr)
		print(f"You have {len(addr)} name(s) so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

def Phone():
	WritePhone = input("What phone numbers would you like to add?: ")
	if WritePhone == 'x' or WritePhone == 'X':
		print("Exiting...")
		sys.exit()
	elif WritePhone == 'f' or WritePhone == 'F':
		PrintDox()
	else:
		phone.append(WritePhone)
		print('\n')
		print(phone)
		print(f"You have {len(phone)} phone number(s) so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

def Social():
	WriteSocial = input("What social media would you like to add?: ")
	if WriteSocial == 'x' or WriteSocial == 'X':
		print("Exiting...")
		sys.exit()
	elif WriteSocial == 'f' or WriteSocial == 'F':
		PrintDox()
	else:
		social.append(WriteSocial)
		print('\n')
		print(social)
		print(f"You have {len(social)} social media(s) so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

def Family():
	WriteFamily = input("What family/friends would you like to add?: ")
	if WriteFamily == 'x' or WriteFamily == 'X':
		print("Exiting...")
		sys.exit()
	elif WriteFamily == 'f' or WriteFamily == 'F':
		PrintDox()
	else:
		family.append(WriteFamily)
		print('\n')
		print(family)
		print(f"You have {len(family)} family/friend(s) so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

def Other():
	WriteOther = input("What other things would you like to add?: ")
	if WriteOther == 'x' or WriteOther == 'X':
		print("Exiting...")
		sys.exit()
	elif WriteOther == 'f' or WriteOther == 'F':
		PrintDox()
	else:
		other.append(WriteOther)
		print('\n')
		print(other)
		print(f"You have {len(other)} other things so far.")
		print('\n')
		print("""
1. Name(s)
2. Address(s)
3. Phone Number(s)
4. Social Media(s)
5. Family or Friend(s)
6. Other""")
		print("\n")
		Loop()

#Lists of the dox
names = []
addr = []
phone = []
social = []
family = []
other = []

#Will print out the dox from Dox_Format to a file. Loops through Dox_Format and adds a comma and space between each piece of info.
def PrintDox():
	with open("DoxList.txt", 'w') as file:
		for row in Dox_Format:
			s = ", ".join(map(str, row))
			file.write(s + "\n")

#Lists for Adding to Dox_Format (really bad coding i know)
divider = ["+-----------------------------------------------------------------------+"]
name = ["Names - "]
addresses = ["Addresses - "]
phones = ["Phone Numbers - "]
socials = ["Social Medias - "]
families = ["Family/Friends - "]
others = ["Others - "]
space = ["\n"]

#Main Dox, gets all its variables from above and prints them. Decided to use tuples since they print out white space and looks better.
Dox_Format = (
divider,
name,
space,
names,
divider,
addresses,
space,
addr,
divider,
phones,
space,
phone,
divider,
socials,
space,
social,
divider,
families,
space,
family,
divider,
others,
space,
other,
divider,
space
)

#Main loop, asks for input, goes to the function or shows an error based off what you put for the variable option.
def Loop():
	while True:
		option = input("What would you like to add?: ")
		if option == 'x' or option == 'X':
			print("Exiting...")
			sys.exit()
		elif option == 'f' or option == 'F':
			PrintDox()
			break
		elif option == '1':
			Name()
			break
		elif option == '2':
			Addr()
			break
		elif option == '3':
			Phone()
			break
		elif option == '4':
			Social()
			break
		elif option == '5':
			Family()
			break
		elif option == '6':
			Other()
			break
		elif option > str(6):
			print("Too high of a number entered, try again.")
			continue
		else:
			print("Something went wrong, please try again.")

Loop()
