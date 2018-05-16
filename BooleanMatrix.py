# import copy

# arr =[[1,0,0,1],[0,0,1,0],[0,0,0,0]]
# outputArr = copy.deepcopy(arr)

# time complexity O(M*N*M)
# Space complexity (M*N)

# for i in range(len(arr)):
# 	for j in range(len(arr[i])):
# 		if arr[i][j] == 1:
# 			for k in range(len(arr)):
# 				outputArr[k][j] = 1
# 			for k in range(len(arr[i])):
# 				outputArr[i][k] = 1

# print(outputArr)







# time complexity O(M*N) matrix[m][n]
# space Complexity O(M+N)

# arr =[[1,0,1],[0,0,0],[0,0,1]]
# row = [0] * len(arr)
# col = [0] * len(arr[0])

# for i in range(len(arr)):
# 	for j in range(len(arr[i])):
# 		if arr[i][j] == 1:
# 			row[i] = 1
# 			col[j] = 1

# for i in range(len(arr)):
# 	for j in range(len(arr[i])):
# 		if row[i] == 1 or col[j] == 1:
# 			arr[i][j] = 1

# print(arr)



# Time COmplexity O(M*N)
# SPACE COMPLEXITY O(1)
arr =[[0,0,1],[0,0,0],[0,0,0]]
row_flag = False
col_flag = False
for i in range(len(arr)):
	for j in range(len(arr[i])):
		if (i == 0 and arr[i][j] == 1):
			row_flag = True
		if (j == 0 and arr[i][j] == 1):
			col_flag = True
		if (arr[i][j] == 1):
			arr[0][j] = 1
			arr[i][0] = 1

for i in range(1,len(arr)):
	for j in range(1,len(arr[i])):
		if arr[0][j] == 1 or arr[i][0] == 1:
			arr[i][j] = 1

if row_flag:
	for j in range(len(arr[0])):
		arr[0][j] = 1

if col_flag:
	for j in range(len(arr)):
		arr[j][0] = 1

print(arr)



