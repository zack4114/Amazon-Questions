# Find the smallest positive number missing from an unsorted array | Set 1
# You are given an unsorted array with both positive and negative elements. You have to find the smallest positive number 
# missing from the array in O(n) time using constant extra space. You can modify the original array.

# Examples

#  Input:  {2, 3, 7, 6, 8, -1, -10, 15}
#  Output: 1

#  Input:  { 2, 3, -7, 6, 8, 1, -10, 15 }
#  Output: 4

#  Input: {4, 3, 1, -1, -2}
#  Output: 2 


# A naive method to solve this problem is to search all positive integers, starting from 1 in the given array. 
# We may have to search at most n+1 numbers in the given array. So this solution takes O(n^2) in worst case.
# def findMissingNumber(l):
# 	n = len(l)
# 	for i in range(1,n):    #O(n)
# 		if i not in l:    #O(n)
# 			return i
# print(findMissingNumber([6,1,3,5]))


# Efficien approach using sorting 
# We can use sorting to solve it in lesser time complexity. We can sort the array in O(nLogn) time. Once the array is 
# sorted, then all we need to do is a linear scan of the array. So this approach takes O(nLogn + n) time which is O(nLogn).
# def findMissingNumber(l):
# 	l.sort() #O(nlogn)
# 	count = 1
# 	for i in range(len(l)):
# 		if l[i] > 0:
# 			if l[i] != count:
# 				return count
# 			else:
# 				count += 1
# print(findMissingNumber([4, 3, 1, -1, -2]))



# Another approach in O(n) time complexity and O(n) space complexity is to use hashing
# make a hash table of size n with all values set to 0 as soon as the number comes set index to 1


# def findMissingNumber(l):
# 	h = [0]*(max(l)+1)
# 	for i in l:
# 		if i > 0:
# 			h[i] = 1 				
# 	for i in range(1,len(h)):
# 		if h[i] == 0:
# 			return i
# print(findMissingNumber([2, 3, 7, 6, 8, -1, -10, 15]))



# Another approach in O(n) time complexity and O(1) space complexity
# 1) Segregate positive numbers from others i.e., move all non-positive numbers to left side. In the following code,
 # segregate() function does this part.
# 2) Now we can ignore non-positive elements and consider only the part of array which contains all positive elements. 
# We traverse the array containing all positive numbers and to mark presence of an element x, we change the sign of 
# value at index x to negative. We traverse the array again and print the first index which has positive value. In the 
# following code, findMissingPositive() function does this part. Note that in findMissingPositive, we have subtracted 1 
# from the values as indexes start from 0 in C.


def segregate(l):
	j = 0
	for i in range(len(l)):
		if l[i] <= 0 :
			l[i],l[j] = l[j],l[i]
			j += 1
	return l
def findMissingNumber(l):
	l = segregate(l)
	shift = 0
	for i in l:
		if i > 0:
			break
		shift += 1
	for i in range(shift,len(l)):
		if abs(l[i]-1) < len(l) and l[abs(l[i])+shift-1] > 0:
			l[abs(l[i])+shift-1] = -l[abs(l[i])+shift-1]
		print(l)
	for i in range(len(l)):
		if l[i] > 0:
			return i-shift+1
	return i-shift+1
print(findMissingNumber([10,1, 2, -10, -20]))

