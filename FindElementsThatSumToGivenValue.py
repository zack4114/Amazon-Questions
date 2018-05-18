# Find four elements that sum to a given value | Set 1 (n^3 solution)

# Given an array of integers, find all combination of four elements in the array whose sum is equal to a given value X.
# For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and X = 23, 
# then your function should print “3 5 7 8” (3 + 5 + 7 + 8 = 23).


# O(n^3) Solution
# def findElements(listOfNumbers,total):
# 	result = []
# 	for i in range(len(listOfNumbers)-3):
# 		for j in range(i+1,len(listOfNumbers) - 2):
# 			k = j+1
# 			l = len(listOfNumbers)-1
# 			while(k < l and k < len(listOfNumbers)-1 and l < len(listOfNumbers)):
# 				SUM = listOfNumbers[i] + listOfNumbers[j] + listOfNumbers[k] + listOfNumbers[l]
# 				if SUM == total:
# 					result.append([i,j,k,l])
# 					k += 1
# 					l -= 1
# 				elif SUM < total:
# 					k += 1
# 				elif SUM > total:
# 					l -= 1
# 	return result
# listOfNumbers=[10, 2, 3, 4, 5, 9, 7, 8]
# listOfNumbers.sort()
# total = 23
# result = findElements(listOfNumbers,total)
# for x in result:
# 	for y in x:
# 		print(listOfNumbers[y],end = ' ')
# 	print()

# O(n^4) Solution
def findElements(listOfNumbers,total):
	result = []
	for i in range(len(listOfNumbers)-3):
		for j in range(i+1,len(listOfNumbers)-2):
			for k in range(j+1,len(listOfNumbers)-1):
				for l in range(k+1,len(listOfNumbers)):
					if listOfNumbers[i] + listOfNumbers[j] + listOfNumbers[k] + listOfNumbers[l] == total:
						print(listOfNumbers[i],listOfNumbers[j],listOfNumbers[k],listOfNumbers[l])

listOfNumbers=[10, 2, 3, 4, 5, 9, 7, 8]
findElements(listOfNumbers,23)

