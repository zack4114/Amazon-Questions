# Given an integer x, find square root of it. If x is not a perfect square, then return floor(√x).
# Input: x = 4
# Output: 2

# Input: x = 11
# Output: 3

# Naive Approac O(n)

# def findSqrt(number):
# 	if number == 1 or number == 0:
# 		return number
# 	for i in range(number//2 + 1):
# 		if i*i == number:
# 			return i
# 		elif i*i > number and (i-1)*(i-1) < number:
# 			return i-1
# number = 144
# print(findSqrt(number))


# Binary search approach O(logn):
def findSqrt(number):
	if number ==0 or number == 1:
		return number
	else:
		ans = 1
		start = 2
		end = number//2
		while(start<=end):
			mid = (start+end)//2
			if mid * mid == number:
				return mid
			elif number < mid*mid:
				end = mid - 1
			elif number > mid*mid:
				ans = mid
				start = mid + 1
		return ans
number = 18312
print(findSqrt(number))