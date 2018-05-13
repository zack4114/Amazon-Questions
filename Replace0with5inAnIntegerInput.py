

# One solution if use of array is allowed

# number = int(input("Enter an integer"))
# number = str(number)
# number = list(number)
# for x in range(len(number)):
# 	if number[x] == '0':
# 		number[x] = '5'
# print(''.join(number))


# if use of array is not allowed
# Non Recursive solution
# number = 10110101212104124100000124010
# numberLength = len(str(number))
# temp = number
# outputNumber = 0
# divisor = 10
# for i in range(numberLength):
# 	digit = number % 10
# 	if digit == 0:
# 		digit = 5
# 	number = number // 10
# 	outputNumber += divisor//10 * digit
# 	divisor = divisor * 10
# print(outputNumber)


# Recursive solution
def Convert0to5(number):
	if number == 0:
		return number
	else:
		digit = number % 10
		if digit == 0:
			digit = 5
		return Convert0to5(number//10) * 10 + digit


number = 10
if number == 0:
	number = 5
print(Convert0to5(number))


