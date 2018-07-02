# Move all zeroes to end of array
# Given an array of random numbers, Push all the zero’s of a given array to the end of the array. For example, 
# if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}. 
# The order of all other elements should be same. Expected time complexity is O(n) and extra space is O(1).

# Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
# Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

# Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
# Output : arr[] = {1, 2, 3, 6, 0, 0, 0};

# Approach is to use a count variable 
# for every non zero value store the a[i] into a[count] and increment the count value
def move0toend(l):
	count = 0
	for i in range(len(l)):
		if l[i] != 0:
			l[count] = l[i]
			count += 1
	for i in range(count,len(l)):
		l[i] = 0
	print(l)
move0toend([1,2,0,0,0,3,6])