def checkAllBitsAreSet(number):
	if number %2 == 0:
		return False
	else:
		while(number > 0):
			if number%2 != 1:
				return False
			number //= 2
		return True

number = 0
print(checkAllBitsAreSet(number))