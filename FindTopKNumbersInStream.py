# Find top k (or most frequent) numbers in a stream
# Given an array of n numbers. Your task is to read numbers from the array and keep at-most K numbers at the top 
# (According to their decreasing frequency) every time a new number is read. We basically need to print top k numbers 
# sorted by frequency when input stream has included k distinct elements, else need to print all distinct elements sorted
# by frequency.

# Examples:

# Input :  arr[] = {5, 2, 1, 3, 2}
#              k = 4
# Output : 5 2 5 1 2 5 1 2 3 5 2 1 3 5 

# Input  : arr[] = {5, 2, 1, 3, 4}
#              k = 4
# Output : 5 2 5 1 2 5 1 2 3 5 1 2 3 4
# Expected time complexity is O(n * k)

# Explanation of 1st example:
# Given array is arr[] = {5, 2, 1, 3, 2} and k = 4
# Step 1:After reading 5, there is only one element 5 whose frequency is max till now. so print 5.
# Step 2:After reading 2, we will have two elements 2 and 5 with same frequency. As 2, is smaller than 5 but their 
# frequency is same so we will print 2 5.
# Step 3: After reading 1, we will have 3 elements 1,2 and 5 with same frequency, so print 1 2 5.
# Step 4: Similarly after reading 3, print 1 2 3 5
# Step 5: After reading last element 2, since 2 has already occurred so we have now frequency of 2 as 2. So we keep 2 
# at the top and then rest of element with same frequency in sorted order. So print, 2 1 3 5.


def findNumbers(l):
	