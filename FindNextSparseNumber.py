# Find Next Sparse Number
# A number is Sparse if there are no two adjacent 1s in its binary representation. For example 5 (binary representation: 101)
# is sparse, but 6 (binary representation: 110) is not sparse.
# Given a number x, find the smallest Sparse number which greater than or equal to x.

# Examples:

# Input: x = 6
# Output: Next Sparse Number is 8

# Input: x = 4
# Output: Next Sparse Number is 4

# Input: x = 38
# Output: Next Sparse Number is 40

# Input: x = 44
# Output: Next Sparse Number is 64

# Naive approach is to make a utility function isSparse() to check whether a number is a sparse number or not
# time complexity of this function is O(logx)
# then search for numbers greater than the given number which is sparse
# therefore the timecomplexity of this is O(xlogx)
# def isSparse(x):
# 	while(x > 0):
# 		if x & 1 == 1 and 2 == x & 2:
# 			return False
# 		x=x >> 1
# 	return True

# def findNextSparse(x):
# 	while(not isSparse(x)):
# 		x += 1
# 	print(x)
# findNextSparse(4)



# Efficient Approach
# An Efficient Solution can solve this problem without checking all numbers on by one. Below are steps.

# 1) Find binary of the given number and store it in a 
#    boolean array.
# 2) Initialize last_finalized bit position as 0.
# 2) Start traversing the binary from least significant bit.
#     a) If we get two adjacent 1's such that next (or third) 
#        bit is not 1, then 
#           (i)  Make all bits after this 1 to last finalized
#                bit (including last finalized) as 0. 
#           (ii) Update last finalized bit as next bit. 
# For example, let binary representation be 01010001011101, we change it to 01010001100000 
# (all bits after highlighted 11 are set to 0). Again two 1’s are adjacent, so change binary representation 
# to 01010010000000. This is our final answer.
# Time complexity is O(logx)
# Space Complexity is O(logx)
def findNextSparse(x):
	bits = []
	res = 0
	while(x > 0):
		bits.insert(0,x&1)
		x = x>>1
	bits.insert(0,0)
	print(bits)
	for i in range(len(bits)-2,-1,-1):
		if bits[i] == 1 and bits[i+1] == 1 and bits[i-1] != 1:
			for j in range(len(bits)-1,i-1,-1):
				bits[j] = 0
			bits[i-1] = 1
	print(bits)
	for i in bits:
		res = res << 1

		res = res | i
	print(res)
findNextSparse(44)
	
