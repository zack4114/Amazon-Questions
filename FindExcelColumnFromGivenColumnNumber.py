# # Find Excel column name from a given column number
# Input          Output
#  26             Z
#  51             AY
#  52             AZ
#  80             CB
#  676            YZ
#  702            ZZ
#  705            AAC

def findColumnName(number):
	res = ""
	while(number > 0):
		if number%26 == 0:
			res += 'Z'
			number = (number//26)-1
		else:
			res+= chr(number%26 + ord('A')-1)
			number = (number//26)
	res = res[-1::-1]
	print(res)

findColumnName(705)