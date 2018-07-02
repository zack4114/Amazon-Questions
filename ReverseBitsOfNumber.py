# Given an unsigned integer, reverse all bits of it and return the number with reversed bits.

# Input : n = 1
# Output : 2147483648  
# On a machine with size of unsigned
# bit as 32. Reverse of 0....001 is
# 100....0.

# Input : n = 2147483648
# Output : 1 

# Method1 – Simple
# Loop through all the bits of an integer. If a bit at ith position is set in the i/p no. then set the bit at 
# (NO_OF_BITS – 1) – i in o/p. Where NO_OF_BITS is number of bits present in the given number.
def findReverse(num):
	reverse = 0
	noOfBits = 32
	for i in range(noOfBits):
		temp = (num & (1<<i))
		if temp:
			reverse = reverse | (1<<((noOfBits - 1) - i))
	return reverse
print(findReverse(2147483648))