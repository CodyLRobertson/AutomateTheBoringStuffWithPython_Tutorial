


numInput = int(input("Enter a number to be calculated with the Collatz Sequence:"))
def collatz(number):
	if number % 2 == 0:
		print(number//2)
		return number == number // 2

	else: 
		number % 2 == 1
		print((number*3)+1)
		return number == (number*3)+1
if numInput > 1:
	collatz(numInput)
else: 
	print("We've reduced to one (1) via the Collatz Sequence.")