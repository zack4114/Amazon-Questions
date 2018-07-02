# XOR of all subarray XORs | Set 1
# Given an array of integers, we need to get total XOR of all subarray XORs where subarray XOR can be obtained by XORing 
# all elements of it.

# Examples :

# Input : arr[] = [3, 5, 2, 4, 6]
# Output : 7
# Total XOR of all subarray XORs is,
# (3) ^ (5) ^ (2) ^ (4) ^ (6)
# (3^5) ^ (5^2) ^ (2^4) ^ (4^6)
# (3^5^2) ^ (5^2^4) ^ (2^4^6)
# (3^5^2^4) ^ (5^2^4^6) ^
# (3^5^2^4^6) = 7     

# Input : arr[] = {1, 2, 3}
# Output : 2

# Input : arr[] = {1, 2, 3, 4}
# Output : 0

# Naive approach is to find all subarrays and xor all of them. Timecomplexity O(n^3)

# effiecient approach
# An efficient solution is based on the idea to enumerate all subarrays, we can count frequency of each element occurred 
# totally in all subarrays, if the frequency of an element is odd then it will be included in final result otherwise not.

# As in above example, 
# 3 occurred 5 times,
# 5 occurred 8 times,
# 2 occurred 9 times,
# 4 occurred 8 times,
# 6 occurred 5 times
# So our final result will be xor of all elements which occurred odd number of times
# i.e. 3^2^6 = 7

# From above occurrence pattern we can observe that number at i-th index will have 
# (i + 1) * (N - i) frequency. 
# So we can iterate over all elements once and calculate their frequencies and if it is odd then we can include that in our
#  final result by XORing it with the result.
# Total time complexity of solution will be O(N)
def findXORs(l):
	xor = 0
	n = len(l)
	for i in range(n):
		f = (i+1)*(n-i)
		if f % 2 is not 0:
			xor ^= l[i]
	return xor
print(findXORs([3,5,2,4,6]))