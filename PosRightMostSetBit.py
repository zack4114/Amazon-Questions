# Write a one line C function to return position of first 1 from right to left, in binary representation of an Integer.
# Approach: Take 2's complement of the number and logically and it with original umber. This will give a binary number with only the rightmost set bet and all other bits set to 0.
# 			Take log ofthis number and then add 1 to it to get the position of the rightmost set bit.
# 			Example 
			# 18 = 010010
			# 2's complement  = 101101 + 1 = 101110 
			# and with 18  = 000010
			# log2(000010) = 1
			# 1 + 1 = 2
			# pos = 2

import math
def posRightMostSetBit(number):
	return math.log2(number & -number) + 1

print(posRightMostSetBit(8))
