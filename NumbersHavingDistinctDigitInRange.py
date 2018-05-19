# Given a range, print all numbers having unique digits.
# Input : 10 20 (both inclusive)
# Output : 10 12 13 14 15 16 17 18 19 20  (Except 11)

# Input : 1 10
# Output : 1 2 3 4 5 6 7 8 9 10


def findNumbers(listOfNumbers):
	result = []
	for i in listOfNumbers:
		isUnique = True
		visited =[False]*10
		temp = i
		while(i > 0):
			if(visited[i%10]):
				isUnique = False
				break
			visited[i%10] = True
			i //=10
		if isUnique:
			result.append(temp)
	return result

lowerBound = 20
upperBound = 50
listOfNumbers = [x for x in range(lowerBound,upperBound+1)]
print(findNumbers(listOfNumbers))
