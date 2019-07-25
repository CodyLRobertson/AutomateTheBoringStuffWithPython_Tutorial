#First Section of Chapter
'''
def hello():
	print('Howdy!')
	print('Howdy!!!!!!')
	print('Hello there.')
hello()
hello()
hello()

def hello(name, age, gender):
	print('Hello, '+ name + age + gender)

hello('Cody', ' 24 ', ' Male')
hello('Emilee', ' 25 ', ' Female')
'''
#Second Section of Chapter

#1
import random
#2
def getAnswer(answerNumber):
#3
	if answerNumber == 1:
		return 'It is certain'
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

#4
'''r = random.randint(1,10)
#5
fortune = getAnswer(r)
#6
print(fortune)
'''

print(getAnswer(random.randint(1,9)))

spam = print("Hello! ", end='')
None == spam
print(spam)

print("Cats", 'Dogs', 'mice')
print("Cats", 'Dogs', 'mice')


