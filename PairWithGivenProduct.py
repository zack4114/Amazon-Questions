# Pair with given product
# Given an array of distinct elements and a number x, find if there is a pair with product equal to x
# Input : arr[] = {10, 20, 9, 40};
#         int x = 400;
# Output : Yes

# Input : arr[] = {10, 20, 9, 40};
#         int x = 190;
# Output : No

# Input : arr[] = {-10, 20, 9, -40};
#         int x = 400;
# Output : Yes

# Input : arr[] = {-10, 20, 9, 40};
#         int x = -400;
# Output : Yes

# Input : arr[] = {0, 20, 9, 40};
#         int x = 0;
# Output : Yes


# Solution in O(n^2)
# def isPairPresent(inputArr,product):
# 	for i in inputArr:
# 		for j in inputArr:
# 			if i*j == product:
# 				return True
# 	return False

# inputArr = [10,20,9,40]
# product = 400

# print(isPairPresent(inputArr,product))




# # Solution in O(nlogn)
# # in this we sort the input array and then we pick a number, divide the product by it and search for the result in the right side of the array.
# #  We sort the given array. After sorting, we traverse the array and for every element arr[i],
# #  we do binary search for x/arr[i] in the subarry on right of arr[i], i.e., in subarray arr[i+1..n-1]
# def binarySearch(inputArr,number):
# 	length = len(inputArr)
# 	start = 0
# 	end = length - 1
# 	while(start <= end):
# 		mid = round((start+end)//2)
# 		if inputArr[mid] == number:
# 			return True
# 		elif number < inputArr[mid]:
# 			end = mid - 1
# 		else:
# 			start = mid + 1
# 	return False

# def isPairPresent(inputArr,product):
# 	for i in range(len(inputArr)):
# 		if inputArr[i] == 0:
# 			if product == 0:
# 				return True
# 		else:
# 			temp = product/inputArr[i]
# 			if binarySearch(inputArr[i+1:],temp):
# 				return True
# 	return False

# inputArr = [10,20,9,40]
# inputArr.sort() #O(nlogn)  time complexity Sorting done using Timsort(mixed of insertion sort and merge sort)
# print(isPairPresent(inputArr,360))




# Solution in O(n)
# Using hash (Set) to search in O(1) therefore reducing the complexity to O(n)
def isPairPresent(inputArr,product):
	tempSet = set()
	for i in inputArr:
		if i == 0:
			return True
		else:
			if product%i == 0:
				if product/i in tempSet:
					return True
			tempSet.add(i)
	return False
inputArr = [10,20,9,40]
product = 400
print(isPairPresent(inputArr,product))

