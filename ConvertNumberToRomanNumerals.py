# Converting Decimal Number lying between 1 to 3999 to Roman Numerals
# Given a number, find its corresponding Roman numeral.
# Example:

# Input : 9
# Output : IX

# Input : 40
# Output : XL

# Input :  1904
# Output : MCMIV


# In this approach we consider the main significant digit in the number. Ex: in 1234, main significant digit is 1. Similarly in 345 it is 3.
# In order to extract main significant digit out, we need to maintain a divisor (lets call it div) like 1000 for 1234 (since 1234 / 1000 = 1) and 100 for 345 (345 / 100 = 3).

# Also, lets maintain a dictionary called romanNumeral = {1 : ‘I’, 5: ‘V’, 10: ‘X’, 50: ‘L’, 100: ‘C’, 500: ‘D’, 1000: ‘M’}

# Following is the algorithm:

# if main significant digit <= 3
# romanNumeral[div] * mainSignificantDigit
# if main significant digit == 4

# romanNumeral[div] + romanNumeral[div * 5]
# if 5 <= main significant digit <= 8

# romanNumeral[div * 5] + (romanNumeral[div] * ( mainSignificantDigit-5))
# if main significant digit == 9

# romanNumeral[div] + romanNumeral[div*10]
# Example:
# Suppose the input number is 3649.

# Iter 1
# Initially number = 3649
# main significant digit is 3. Div = 1000.
# So, romanNumeral[1000] * 3
# gives: MMM
# Iter 2

# now, number = 649
# main significant digit is 6. Div = 100.
# So romanNumeral[100*5] + (romanNumeral[div] * ( 6-5))
# gives: DC
# Iter 3

# now, number = 49
# main significant digit is 4. Div = 10.
# So romanNumeral[10] + romanNumeral[10 * 5]
# gives: XL
# Iter 4

# now, number = 9
# main significant digit is 9. Div = 1.
# So romanNumeral[1] * romanNumeral[1*10]
# gives: IX
# Final result by clubbing all the above: MMMDCXLIX

def findRomanNumeral(num):
	romanNumeral = {1 : 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
	div = 1
	while num >= div:
		div *= 10
	div //= 10
	if num < 10:
		div = 1
	res = ""
	while num > 0:
		temp = num // div
		if temp <= 3:
			res += romanNumeral[div] * temp
		elif temp == 4:
			res += romanNumeral[div] + (romanNumeral[div*5])
		elif 5 <= temp and temp <= 8:
			res += (romanNumeral[div*5]) + (romanNumeral[div] * (temp-5)) 
		elif temp == 9:
			res += (romanNumeral[div]) + (romanNumeral[div*10])
		num = num%div
		div //=10
	print(res)

findRomanNumeral(349)
