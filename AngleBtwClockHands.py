h = 3.00
m = 30.00

# find angle of min hand wrt 12 
if m == 60:
	minHandAngle = 0
else:
	minHandAngle = m*6

# find raw angle of hour hand wrt 12 
if h == 12:
	hourHandAngle = 0
else:
	hourHandAngle = h * 30

# find exact angle of hour hand wrt 12
hourHandAngle = hourHandAngle + minHandAngle*(1/12)

angleBetweenHands = abs(minHandAngle-hourHandAngle)
print(angleBetweenHands,"degree")