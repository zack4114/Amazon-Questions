# Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. 
# Expected time complexity is O(Logn)

# one approach is to do linear search O(n)
# in binary search first find the first occurance using binary search = i
# find last occurance using binary search = j
# Return i-j+1

def findFrequency(listOfNumbers,number):
	firstOccurance = findFirstOccurance(listOfNumbers,number,0,len(listOfNumbers)-1)
	print(firstOccurance)
	if firstOccurance == -1:
		return 0

	lastOccurance = findLastOccurance(listOfNumbers,number,firstOccurance,len(listOfNumbers)-1)
	print(lastOccurance)
	return lastOccurance - firstOccurance + 1

def findFirstOccurance(listOfNumbers,number,start,end):
	if end >= start:
		mid = (start + end)//2
		if (number == listOfNumbers[mid] and (number > listOfNumbers[mid-1] or mid == 0)):
			return mid
		elif (number <= listOfNumbers[mid]):
			return findFirstOccurance(listOfNumbers,number,start,mid-1)
		else:
			return findFirstOccurance(listOfNumbers,number,mid+1,end)
	else:
		return -1

def findLastOccurance(listOfNumbers,number,start,end):
	if end >= start:
		mid = (start + end)//2
		if(number == listOfNumbers[mid] and (mid == end or number < listOfNumbers[mid+1])):
			return mid
		elif(number < listOfNumbers[mid]):
			return findLastOccurance(listOfNumbers,number,start,mid-1)
		else:
			return findLastOccurance(listOfNumbers,number,mid+1,end)
	else:
		return -1


listOfNumbers = [1,1,1,2,2,2,2,2,2,3,4,5]
print(findFrequency(listOfNumbers,2))
