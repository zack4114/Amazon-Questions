# Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. 
# Expected Time Complexity is O(n2).


# Input : arr[] = {-2, 0, 1, 3}
#         sum = 2.
# Output : 2
# Explanation :  Below are triplets with sum less than 2
#                (-2, 0, 1) and (-2, 0, 3) 

# Input : arr[] = {5, 1, 3, 4, 7}
#         sum = 12.
# Output : 4
# Explanation :  Below are triplets with sum less than 4
#                (1, 3, 4), (1, 3, 5), (1, 3, 7) and 
#                (1, 4, 5)

# O(n^3) Solution

# def countTriplet(listOfNumbers,Sum):
# 	res = 0
# 	for i in range(len(listOfNumbers) - 2):
# 		for j in range(i+1,len(listOfNumbers)):
# 			for k in range(j+1,len(listOfNumbers)):
# 				if listOfNumbers[i]+listOfNumbers[j]+listOfNumbers[k] < Sum:
# 					res += 1
# 	return res
# listOfNumbers = [-2,0,1,3]
# Sum = 2
# print(countTriplet(listOfNumbers,Sum))



# O(n^2) Solution
# 1) Sort the input array in increasing order.
# 2) Initialize result as 0.
# 3) Run a loop from i = 0 to n-2.  An iteration of this loop finds all
#    triplets with arr[i] as first element.
#      a) Initialize other two elements as corner elements of subarray
#         arr[i+1..n-1], i.e., j = i+1 and k = n-1
#      b) Move j and k toward each other until they meet, i.e., while (j < k)
#             (i) if (arr[i] + arr[j] + arr[k] >= sum), then do k--

#             // Else for current i and j, there can (k-j) possible third elements
#             // that satisfy the constraint.
#             (ii) Else Do ans += (k - j) followed by j++


def countTriplets(listOfNumbers,Sum):
	result = 0
	listOfNumbers.sort()
	for i in range(len(listOfNumbers)-2):
		j = i+1
		k = len(listOfNumbers)-1
		while(j<k):
			if(listOfNumbers[i] + listOfNumbers[j] + listOfNumbers[k] >= Sum):
				k = k - 1
			else:
				result += (k-j)
				j += 1
	return result

listOfNumbers = [1,4,3,5,7]
print(countTriplets(listOfNumbers,12))
