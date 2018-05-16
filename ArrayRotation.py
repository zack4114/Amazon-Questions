def rotate(arr,d,n):
	return arr[d:] + arr[:d]
arr = [1,2,3,4,5,6,7]
print(rotate(arr,2,len(arr)))
