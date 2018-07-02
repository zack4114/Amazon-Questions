# The knight is placed on the first block of an empty board and, moving according to the rules of chess, 
# must visit each square exactly once.
# takes around 10 min to run in python

def isValid(x,y,sol):
	if (x >=0 and x< 8 and y>= 0 and y<8 and sol[x][y] is -1):
		return True
	return False


def solveKT():
	sol = [[-1]*8 for i in range(8)]
	for i in sol:
		print(i)
	moveX = [2, 1, -1, -2, -2, -1,  1,  2 ]
	moveY = [1, 2,  2,  1, -1, -2, -2, -1]
	sol[0][0] = 0

	if solveKTUtil(0,0,1,sol,moveX,moveY) == False:
		print("NO Solution")
		return False
	else:
		for i in sol:
			print(i)
	return True



def solveKTUtil(x,y,moveNo,sol,moveX,moveY):
	if moveNo is 64:
		return True
	for i in range(8):
		nx = x+moveX[i]
		ny = y+moveY[i]
		if isValid(nx,ny,sol):
			sol[nx][ny] = moveNo
			for i in sol:
				print(i)
			print()
			if solveKTUtil(nx,ny,moveNo+1,sol,moveX,moveY) == True:
				return True
			else:
				sol[nx][ny] = -1

	return False

solveKT()

