# prints all the prime numbers befor a given numbers

def sieveOfEratothenes(number):
	isPrime = [True for x in range(2,number+1)]
	isPrime.insert(0,False)
	isPrime.insert(1,False)
	for x in range(number+1):
		if isPrime[x]:
			for j in range(x*2,number+1,x):
				isPrime[j] = False
	result = []
	for i in range(number+1):
		if isPrime[i]:
			result.append(i)
	return result

print(sieveOfEratothenes(1010))