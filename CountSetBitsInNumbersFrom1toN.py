# Given a positive integer n, count the total number of set bits in binary representation of all numbers from 1 to n.

# First Approch is to iterate through all numbers and count set bits in each number
# Time complexity O(nLogn)

# def countSetBitsIn1ToN(number):
# 	count = 0
# 	for i in range(1,number+1):
# 		count += countSetBits(i)
# 	return count

# def countSetBits(number):
# 	count = 0
# 	while (number > 0):
# 		if number & 1 == 1:
# 			count +=1
# 		number = number >> 1
# 	return count

# number = 17
# print(countSetBitsIn1ToN(number))



# If we observe bits from rightmost side at distance i than bits get inverted after 2^i position in vertical sequence.
# for example n = 5;
# 0 = 0000
# 1 = 0001
# 2 = 0010
# 3 = 0011
# 4 = 0100
# 5 = 0101

# Observe the right most bit (i = 0) the bits get flipped after (2^0 = 1)
# Observe the 3nd rightmost bit (i = 2) the bits get flipped after (2^2 = 4)

# So, We can count bits in vertical fashion such that at i’th right most position bits will be get flipped after 2^i iteration;
#  Time Complexity in this case is O(k*n) k is numbet of bits required and k is always <= 64

# def toggleFlag(flag):
# 	if flag == 0:
# 		return 1
# 	elif flag == 1:
# 		return 0
# 	else:
# 		return -1


# def countSetBits(number):
# 	i = 0
# 	count = 0
# 	while(2**i <= number):
# 		flag = 0
# 		change = 2**i
# 		for j in range(number+1):
# 			count += flag
# 			if(change == 1):
# 				flag = toggleFlag(flag)
# 				change = 2**i
# 			else:
# 				change -= 1
# 		i += 1
# 	return count

# number = 10
# print(countSetBits(number))





# O(Logn) Approach
# If the input number is of the form 2^b -1 e.g., 1, 3, 7, 15.. etc, the number of set bits is b * 2^(b-1). 
# This is because for all the numbers 0 to (2^b)-1, if you complement and flip the list you end up with the 
# same list (half the bits are on, half off).
#  in this case return b * 2^(b-1).  i.e (no.of bits * (total numbers)/2)

def getLeftMostBit(number):
	count = 0
	while(number > 1):
		number = number >> 1
		count += 1
	return count


def CountSetBitsIn1ToN(number):
	if number == 0:
		return 0
	m = getLeftMostBit(number)
	if number == 2**(m+1)-1:
		return (m+1) * 2**(m)
	else:
		number = number - 2**m
		return (number + 1) + CountSetBitsIn1ToN(number) + m * 2**(m-1)

number = 17
print(CountSetBitsIn1ToN(number))





