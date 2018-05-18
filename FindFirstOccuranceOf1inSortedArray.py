# Given a sorted array consisting 0’s and 1’s. The problem is to find the index of first ‘1’ in the sorted array. 
# It could be possible that the array consists of only 0’s or only 1’s. If 1’s are not present in the array then print “-1”.

# Input : arr[] = {0, 0, 0, 0, 0, 0, 1, 1, 1, 1}
# Output : 6
# The index of first 1 in the array is 6.

# Input : arr[] = {0, 0, 0, 0}
# Output : -1
# 1's are not present in the array.

# Naive O(n) approach
# def findFirstOccurance(listOfnumbers,number):
# 	for i in range(len(listOfnumbers)):
# 		if listOfnumbers[i] == number:
# 			return i
# 	return -1

# listOfnumbers = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# print(findFirstOccurance(listOfnumbers,1))



# Binanry Search O(logn) Approach
def findFirstOccurance(listOfnumbers,start,end,number):
	if (start <= end):
		mid = (start+end)//2
		if(listOfnumbers[mid] == number ) and (mid == 0 or listOfnumbers[mid - 1] < number):
			return mid
		elif (number <= listOfnumbers[mid]):
			return findFirstOccurance(listOfnumbers,start,mid-1,number)
		elif (number > listOfnumbers[mid]):
			return findFirstOccurance(listOfnumbers,mid+1,end,number)
	else:
		return -1

listOfnumbers = [0,0,0,0,0,0,0,0,0,1,1,1,1]
print(findFirstOccurance(listOfnumbers,0,len(listOfnumbers)-1,1))