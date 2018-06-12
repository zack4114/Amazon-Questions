# Find nth Magic Number
# A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5. 
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

# Write a function to find the nth Magic number.

# Example:

# Input: n = 2
# Output: 25

# Input: n = 5
# Output: 130 

# If we notice carefully the magic numbers can be represented as 001, 010, 011, 100, 101, 110 etc, 
# where 001 is 0*pow(5,3) + 0*pow(5,2) + 1*pow(5,1). So basically we need to add powers of 5 for each 
# bit set in given integer n.

# Below is the implementation based on this idea.

def findNumber(n):
	res = 0
	power = 1
	while n > 0:
		if n%2 == 1:
			res += 5**power
		power += 1
		n //= 2
	print(res)
findNumber(5)