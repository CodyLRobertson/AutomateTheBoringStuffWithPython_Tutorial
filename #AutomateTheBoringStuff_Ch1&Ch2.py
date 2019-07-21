
import time
import random



#AutomateTheBoringStuff

#Test Print HelloWorld as per tradition
'''
print("HelloWorld")
print("")
print("----------------------------------------------")

#Chapter (1) Operators and Precedence--------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("CHAPTER (1)")
print("")
print("-----------------------------------")
print("Below you will see examples of Python Expressions")
print("** = Exponent (2**3 = 8)")
print("% = Modulus/remainder (22 % 8 = 6)")
print("// = Integer division/floor quotient (22 // 8 = 2)")
print("/ = Division (22 / 8 = 2.75)")
print("* = Multiplication (3 * 5 = 15)")
print("- = Subtraction(5 - 2 = 3)")
print("+ = Addition(2 + 2 = 4)")
print("")
print("---------------------------------------------")
print('Order of operations is called "Precedence" and goes as follows from left to right:')
print("**,*,/,//,%, +,-")
print("You may use parenthesis to override read order.")
print("")
print("---------------------------------------")

#Chapter (1) The Integer, Floating-Point, and String Data Types
print("There are three (3) types of Data Types; Integers, Floating-Points, and Strings.")
print("This is an integer:")
print(4)
print("This is a Floating-Point:")
print(0.63)
print("This is a string:")
print("ABCDEFG")

#Chapter (1) String Concatenation and Replication----------------------------------------------------------------------------------

print("")
print("Chapter 2")
print("")
#Chapter (2) Flow and Conditionals
True and True

name = str(input("What is your name?   "))
password = str(input("What is the password?   "))

if name == 'Cody':
	print('Hello Cody')
if password =='PythonPassword':
	print("Access Granted.")
else:
	print("Password Incorrect.")
"""
spam = 0
while spam < 5:
	print('Hello World.')
	spam = spam +1
	ham = 0
	while ham <5:
		print("Add Ham!")
		ham = ham +1
		cheese = 0
		while cheese <5:
			print("Adding Cheese!")
			cheese = cheese +1
""'''
#This section of code works, but don't run it, lest you crash everything you hold dear.....
'''year = 0
while year < 10:
	print ("It is year " + str(year))
	year = year + 1
	month = 0
	while month < 12:
		print("It is month "+ str(month))
		month = month + 1
		week = 0
		while week < 4:
			print("It is week " +str(week))
			week = week + 1
			day = 0
			while day < 7:
				print("It is day " + str(day))
				day = day + 1
				hour = 0
				while hour < 24:
					print("It is hour " + str(hour))
					hour = hour + 1
					minute = 0
					while minute < 60:
						print("It is minute " + str(minute))
						minute = minute + 1
						second = 0
						while second < 60:
							print("It is second "+str(second))
							second = second + 1
				
name2 = ''
while name2 != name:
	print('Please type your name.')
	name2 = input()
print("Thanks!")

while True:
	print("Please type your name yet again.")
	name3 = input()
	if name3 == name2 or name:
		break
print("Thank you again!")

'''
# Chapter (3)----------------------------------------------------------------------------------
print("CHAPTER THREE (3)")
def listCounter():
	myList = ["Apple", "Banana","Cherry","Beef","Beer"]
	x = len(myList)
	print("Number of Items in "+ "myList"+ ": " + str(x))
	print("Items in list: " + str(myList))
def hello(name4):
	print('Hello ' + name4)
#Fix below
'''def getAnswer(answerNumber):
	if answerNumber == 1:
		return 'It is certain.'
	elif answerNumber == 2:
		return 'It is decidely so.'
	elif answerNumber == 3:
		return 'Yes.'
	elif answerNumber == 4:
		return 'Reply hazy, try again.'
	elif answerNumber == 5:
		return 'Ask again later.'
	elif answerNumber == 6:
		return 'Concentrate and ask again.'
	elif answerNumber == 7:
		return 'My replay is no.'
	elif answerNumber == 8:
		return 'Outlook not so good.'
	elif answerNumber == 9:
		return 'Very doubtful.'
	elif answerNumber == 10:
		return 'Hard No.'

	r = random.randint(1,10)
	fortune = getAnswer(r)
	print(fortune)
	'''

#MainProgramFunction

def Main():
	listCounter()
	hello(input())


Main()
#Fix get answer function
#getAnswer(r)
