# Count all possible groups of size 2 or 3 that have sum as multiple of 3

# Input: arr[] = {3, 6, 7, 2, 9}
# Output: 8
# // Groups are {3,6}, {3,9}, {9,6}, {7,2}, {3,6,9},
# //            {3,7,2}, {7,2,6}, {7,2,9}


# Input: arr[] = {2, 1, 3, 4}
# Output: 4
# // Groups are {2,1}, {2,4}, {2,1,3}, {2,4,3}

# Approach is that the sum of group of numbers is multiple of 3 it the sum of their remainder (when divided by 3) 
# is multiple of 3

# so creae a hashList which have the count of numbers having remainder as 0 1 2


def countPossibleGroups(listOfNumbers):
	count = 0
	hashList = [0]*3
	for x in listOfNumbers:
		hashList[x%3] += 1
	# print(hashList)


# Case for group of 2 numbers
	# either take all two numbers from 0 remainder c[0]C2
	count += (hashList[0] * (hashList[0]-1))//2
	# Or take 1 from 1 remainder and 1 from 2 remainder
	count += hashList[1] * hashList[2]

# Case for group of 3 Numbers
	# take all from 0 remainder c[0]C3
	count += (hashList[0]*(hashList[0]-1)*(hashList[0]-2))//6
	#take all from 1 remainder (sum of remainder = 3 and 3%3 = 0)
	count += (hashList[1]*(hashList[1]-1)*(hashList[1]-2))//6
	# take all from 2 remanider(sum of remainder = 6 and 6%3 == 0)
	count += (hashList[2]*(hashList[2]-1)*(hashList[2]-2))//6
	# Take 1 from 0 remainder 1 from 1 remainder and 1 from 2 remainder
	count += (hashList[0] * hashList[1] * hashList[2])

	return count


listOfNumbers = [1,2,4,3]
print(countPossibleGroups(listOfNumbers))
