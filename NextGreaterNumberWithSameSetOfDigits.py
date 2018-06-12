# Find next greater number with same set of digits
# Given a number n, find the smallest number that has same set of digits as n and is greater than n. If x is the greatest possible number with its set of digits, then print “not possible”.

# Examples:
# For simplicity of implementation, we have considered input number as a string.

# Input:  n = "218765"
# Output: "251678"

# Input:  n = "1234"
# Output: "1243"

# Input: n = "4321"
# Output: "Not Possible"

# Input: n = "534976"
# Output: "536479"

# Approach
# Start from the right side and find a digit which is smaller than its next digit
# like in 534976 , 4 is smaller than 9 let d = 4
# then swap find the smallest digit  in right side of 'd' which is greater than 'd'
# swap these two digits and then sort all the digits to the right side of the 'd'
import math
def findNextGreaterNumber(number):
	number = [int(x) for x in str(number)]
	n = len(number)
	d = n-1
	for i in range(n-2,-1,-1):
		if number[i] < number[i+1]:
			d = i
			break
	if i is not d:
		print("not Possible")
		return
	k = d+1
	for i in range(d+1,n):
		if number[i] > number[d] and number[i] < number[k]:
			k = i
	number[k],number[d] = number[d],number[k]
	number[d+1:k+1] = number[k:d:-1]
	number = [str(x) for x in number]
	number = ''.join(number)
	print(number)

findNextGreaterNumber(218765k)



