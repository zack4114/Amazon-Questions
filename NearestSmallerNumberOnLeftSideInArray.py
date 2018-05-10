# Find the nearest smaller numbers on left side in an array
# Given an array of integers, find the nearest smaller number for every element such that the smaller element is on left side.

# Input:  arr[] = {1, 6, 4, 10, 2, 5}
# Output:         {_, 1, 1,  4, 1, 2}
# First element ('1') has no element on left side. For 6, 
# there is only one smaller element on left side '1'. 
# For 10, there are three smaller elements on left side (1,
# 6 and 4), nearest among the three elements is 4.

# Input: arr[] = {1, 3, 0, 2, 5}
# Output:        {_, 1, _, 0, 2}

# Expected time complexity is O(n).



# Below Solution is in O(n^2)

# inputArr = [1,6,4,10,2,5]
# outputArr = ['_']

# for i in range(1,len(inputArr)):
# 	anySmallerFlag = False
# 	for j in range(i-1,-1,-1):
# 		if inputArr[j] < inputArr[i]:
# 			outputArr.append(inputArr[j])
# 			anySmallerFlag = True
# 			break
# 	if not anySmallerFlag:
# 		outputArr.append('_')

# print(outputArr)


# Below Solution in O(n) using Stack

"""Let input sequence be 'arr[]' and size of array be 'n'

1) Create a new empty stack S

2) For every element 'arr[i]' in the input sequence 'arr[]',
   where 'i' goes from 0 to n-1.
    a) while S is nonempty and the top element of 
       S is greater than or equal to 'arr[i]':
           pop S
    
    b) if S is empty:
           'arr[i]' has no preceding smaller value
    c) else:
           the nearest smaller value to 'arr[i]' is 
           the top element of S

    d) push 'arr[i]' onto S"""

stack = []
inputArr = [1,6,4,10,2,5]
outputArr = []

for i in inputArr:
	while len(stack) !=0 and stack[-1] >= i:
		stack.pop()
	if len(stack) == 0:
		outputArr.append('_')
	else:
		outputArr.append(stack[-1])
	stack.append(i)

print(outputArr)