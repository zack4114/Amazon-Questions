# Problem : Given four points, you need to identify whether the coordinates are the coordinates of the square or not in the same plane
# Approach : take one point and find the distance of it from the other three points, for the coordinates to be of square
# 			First condition : the distance from two points should be same and from third ppint it should be sqrt(2) times of other distance.
#			Second Condition: if first condition satisfies then, the distance of the third point from the remaining two points should be same 


#Function to find distance between two points
def distSquare(p1,p2):
	return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2

#Fuction to find whether the coordinates are of a square
def isSquare(p1,p2,p3,p4):
	p12 = distSquare(p1,p2)
	p13 = distSquare(p1,p3)
	p14 = distSquare(p1,p4)

	if p12 == p13 and p14 == 2*p12:
		p42 = distSquare(p4,p2)
		p43 = distSquare(p4,p3)
		return p42 == p43 and p12 == p42

	if p12 == p14 and p13 == 2*p12:
		p32 = distSquare(p3,p2)
		p34 = distSquare(p3,p4)
		return p32 == p34 and p12 == p32

	if p13 == p14 and p12 == 2*p13:
		p23 = distSquare(p2,p3)
		p24 = distSquare(p2,p4)
		return p23 == p24 and p13 == p23

	return False

# Four points declaration
p1 = (10,10)
p2 = (10,20)
p3 = (20,10)
p4 = (20,20)

print(isSquare(p1,p2,p3,p4))


