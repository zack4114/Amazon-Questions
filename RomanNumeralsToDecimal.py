# Converting Roman Numerals to Decimal lying between 1 to 3999
# Given a Romal numeral, find its corresponding decimal value.

# Example :

# Input : IX
# Output : 9

# Input : XL
# Output : 40

# Input : MCMIV
# Output :  1904
# M is a thousand, CM is nine hundred 
# and IV is four

# A number in Roman Numerals is a string of these symbols written in descending order(e.g. M’s first, followed by D’s, 
# 	etc.). However, in a few specific cases, to avoid four characters being repeated in succession (such as IIII or XXXX), 
# subtractive notation is often used as follows:

# I placed before V or X indicates one less, so four is IV (one less than 5) and 9 is IX (one less than 10).
# X placed before L or C indicates ten less, so forty is XL (10 less than 50) and 90 is XC (ten less than a hundred).
# C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred 
# is CM (a hundred less than a thousand).
# Algorithm to convert Roman Numerals to Integer Number :

# Split the Roman Numeral string into Roman Symbols (character).
# Convert each symbol of Roman Numerals into the value it represents.
# Take symbol one by one from starting from index 0:
# If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
# else subtract this value by adding the value of next symbol to the running total.

def romanToNumeral(roman):
	dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	res = 0
	i =0 
	while(i < len(roman)):
		if i == len(roman) - 1:
			res += dic[roman[i]]
			i+=1
		elif dic[roman[i]] < dic[roman[i+1]]:
			res += dic[roman[i+1]]-dic[roman[i]]
			i = i+2
		else:
			res += dic[roman[i]]
			i+=1
	return res
print(romanToNumeral("MMMIX"))




