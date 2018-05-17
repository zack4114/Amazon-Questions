# def binarySearch(listOfNumbers,number):
# 	start = 0
# 	end = len(listOfNumbers)-1
# 	while(end >= start):
# 		mid = (start+end)//2
# 		if(number == listOfNumbers[mid]):
# 			return "Found"
# 		elif(number < listOfNumbers[mid]):
# 			end = mid - 1
# 		elif(number > listOfNumbers[mid]):
# 			start = mid + 1
# 	return "Not Found"

def binarySearch(listOfNumbers,number,start,end):
	if end >= start:
		mid = (start+end)//2
		if(number == listOfNumbers[mid]):
			return "Found"
		elif number > listOfNumbers[mid]:
			return binarySearch(listOfNumbers,number,mid+1,end)
		else:
			return binarySearch(listOfNumbers,number,start,mid-1)
	else:
		return "Not Found"

listOfNumbers = [9,12,7,1,30,12,10]
listOfNumbers.sort()
print(binarySearch(listOfNumbers,11,0,len(listOfNumbers)-1))