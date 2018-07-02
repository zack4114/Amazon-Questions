# Question: An Array of integers is given, both +ve and -ve. You need to find the two elements such that their 
# sum is closest to zero.

# For the below array, program should print -80 and 85.

# Simple approach is to use two loops and find the sum for all pairs and return the min sum O(n^2)



# Efficient approach O(nlogn)
import math
def findPair(l):
	min_sum = math.inf
	min_r = 0
	min_l = len(l) - 1
	r = len(l) - 1
	lt = 0
	l.sort()
	while(lt < r):
		s = l[lt]+l[r]
		if abs(s) < abs(min_sum):
			min_sum = s
			min_l=lt
			min_r=r
		elif s < 0:
			lt+=1
		else:
			r-=1
	print(l[min_l],l[min_r])

findPair([1, 60, -10, 70, -80, 85])
