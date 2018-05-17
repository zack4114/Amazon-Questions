# Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.

def countSetBits(number):
	count = 0
	while (number > 0):
		if number & 1 == 1:
			count += 1
		number //= 2
	return count

def bitsNeededToFlip(number1,number2):
	return countSetBits(number1^number2)

number1 = 10
number2 = 20

print(bitsNeededToFlip(number1,number2))