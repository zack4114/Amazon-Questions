# We can use string characters as index and build a count array. Following is the algorithm.

# 1) Scan the string from left to right and construct the count array.
# 2) Again, scan the string from left to right and check for count of each
#  character, if you find an element who's count is 1, return it.
# Example:



 

# Input string: str = geeksforgeeks
# 1: Construct character count array from the input string.
#    ....
#   count['e'] = 4
#   count['f'] = 1
#   count['g'] = 2
#   count['k'] = 2
#   ……
# 2: Get the first character who's count is 1 ('f').



# The above approach takes O(n) time, but in practice it can be improved. The first part of the algorithm runs through the 
# string to construct the count array (in O(n) time). This is reasonable. But the second part about running through the 
# string again just to find the first non-repeater is not good in practice. In real situations, your string is expected 
# to be much larger than your alphabet. Take DNA sequences for example: they could be millions of letters long with an 
# alphabet of just 4 letters. What happens if the non-repeater is at the end of the string? Then we would have to scan 
# for a long time (again).
# We can augment the count array by storing not just counts but also the index of the first time you encountered the 
# character e.g. (3, 26) for ‘a’ meaning that ‘a’ got counted 3 times and the first time it was seen is at position 26.
# So when it comes to finding the first non-repeater, we just have to scan the count array, instead of the string.
def findFirstNonRepeatingCharacterIndex(s):
	count = [[0,0] for i in range(256)]
	for i in range(len(s)):
		count[ord(s[i])][0] += 1
		if count[ord(s[i])][1] == 0:
			count[ord(s[i])][1] = i
	for i in count:
		if i[0] == 1:
			print(s[i[1]])
			break
findFirstNonRepeatingCharacterIndex("geeksfks")