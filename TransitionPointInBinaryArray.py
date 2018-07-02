# Find the transition point in a binary array
# Given a sorted array containing only numbers 0 and 1, the task is to find the transition point efficiently. Transition point is a point where “0” ends and “1” begins.

# Examples :

# Input : 0 0 0 1 1
# Output : 3
# Index of first 1 is 3

# Input : 0 0 0 0 1 1 1 1
# Output : 4
# Index of first 1 is 4

# Naive approach is to use the linear search 
# Efficient appraoch is to use the binary search

def findTransitionPoint(l):
	start = 0
	end = len(l) -1
	while(start <= end):
		mid = (start + end)//2
		if l[mid] == 1 and (mid == 0 or l[mid-1] == 0):
			print(mid)
			return
		elif l[mid] == 0:
			start = mid + 1
		else:
			end = mid - 1
	print("No Transition Point")
findTransitionPoint([0,0,0,0,0])