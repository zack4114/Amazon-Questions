# Given an array arr[] and a position in array, k. Write a function name reverse (a[], k) such that it reverses subarray 
# arr[0..k-1]. Extra space used should be O(1) and time complexity should be O(k).

# Input:
# arr[] = {1, 2, 3, 4, 5, 6}
#     k = 4

# Output:
# arr[] = {4, 3, 2, 1, 5, 6} 

def reverseArray(listOfNumbers,index):
	for i in range((index-1)//2):
		listOfNumbers[i],listOfNumbers[index-1-i] = listOfNumbers[index-1-i],listOfNumbers[i]
	print(listOfNumbers)

listOfNumbers = [1, 2, 3, 4, 5, 6]
index = 4
reverseArray(listOfNumbers,index)