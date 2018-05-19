# Given an even number (greater than 2 ), print two prime numbers whose sum will be 
# equal to given number. There may be several combinations possible. Print only first such pair.



# Input: n = 74
# Output: 3 71

# Input : n = 1024
# Output: 3 1021

# Input: n = 66
# Output: 5 61

# Input: n = 9990
# Output: 17 9973

# Naive approach very time costly
# Find list of prime numbers less that the given number
# then find pair of numbers from that list whose sum is equal to the given sum

# def isPrime(number):
# 	for x in range(2,number-1):
# 		if number % x == 0:
# 			return False
# 	return True

# def findPrimePair(number):
# 	listOfPrimeNumber = []
# 	for x in range(2,number):
# 		if isPrime(x):
# 			listOfPrimeNumber.append(x)
# 	i = 0
# 	j = len(listOfPrimeNumber) - 1
# 	listOfPrimeNumber.sort()
# 	while(i < j):
# 		if listOfPrimeNumber[i] + listOfPrimeNumber[j] == number:
# 			return [listOfPrimeNumber[i],listOfPrimeNumber[j]]
# 		elif listOfPrimeNumber[i] + listOfPrimeNumber[j] < number:
# 			i += 1
# 		elif listOfPrimeNumber[i] + listOfPrimeNumber[j] > number:
# 			j -= 1

# number = 9990
# print(findPrimePair(number))










#  Efficient approach using sieveOfEratothenes to find the list of prime number
# and then search in that list to finf the pair whose sum is equal to the given sum

def sieveOfEratothenes(number):
	# create a isPrime boolean list which stores whether the current index is prime number or not
	isPrime = [True if x >= 2 else False for x in range(number+1)]
	for i in range(2,number+1):
		if isPrime[i]:
			for j in range(i*2,number+1,i):
				isPrime[j] = False

	return isPrime

def findPair(number):
	isPrime = sieveOfEratothenes(number)
	k = [i for i in range(number+1) if isPrime[i]]
	# for i in range(number+1):
	# 	if (isPrime[i] and isPrime[number- i]):
	# 		return [i,number-i]
	i = 0
	j = number
	while(i < j):
		if isPrime[i] and isPrime[j] and i+j == number:
			return [i,j]
		elif isPrime[i] and isPrime[j] and i+j < number:
			i+=1
		elif isPrime[i] and isPrime[j] and i+j > number:
			j-=1
		elif isPrime[i]:
			j-=1
		elif isPrime[j]:
			i+=1
		else:
			i+=1
			j-=1
	return -1

number = 9990
print(findPair(number))
