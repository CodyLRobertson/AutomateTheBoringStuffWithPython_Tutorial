def spam():
	#1
	eggs =99 
	#2
	bacon()
	#3
	print(eggs)

def bacon():
	ham = 101
	#4
	eggs = 0

#5
spam()

'''
When the program starts, 
the spam() function is called ❺, 
and a local scope is created. 
The local variable eggs ❶ is set to 99. 
Then the bacon() function is called ❷, 
and a second local scope is created. 
Multiple local scopes can exist at the same time. 
In this new local scope, 
the local variable ham is set to 101, 
and a local variable eggs—which is different from the one in spam()’s local scope—is also created ❹ and set to 0.

When bacon() returns, 
the local scope for that call is destroyed. 
The program execution continues in the spam() function to print the value of eggs ❸, 
and since the local scope for the call to spam() still exists here, 
the eggs variable is set to 99. This is what the program prints.

The upshot is that local variables in one function are completely separate from the local variables in another function.
'''

def spam():
	eggs = 'spam local'
	print(eggs) #prints 'spam local'
def bacon():
	eggs = 'bacon local'
	print(eggs) # prints 'bacon local'
	spam()
	print(eggs) #continues to print 'bacon local' as out of local scope of spam()
eggs = 'global'
bacon()
print(eggs) #prints 'global'

#Ended on Local and Global Variables with the Same Name"