import math
def canRepresentedAsXRaisedToY(number):
	base = 2
	if number == 0:
		return False
	if number == 1:
		return True
	else:
		while(base < math.sqrt(number)+1):
			if (math.log(number,base) % 1 == 0):
				return True
			base+=1
		return False

number = 9	
print(canRepresentedAsXRaisedToY(number))
			