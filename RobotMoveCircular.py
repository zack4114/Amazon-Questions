# Check if a given sequence of moves for a robot is circular or not
# Given a sequence of moves for a robot, check if the sequence is circular or not.
# A sequence of moves is circular if first and last positions of robot are same. A move can be on of the following.

  # G - Go one unit
  # L - Turn left
  # R - Turn right 
# Input: path[] = "GLGLGLG"
# Output: Given sequence of moves is circular 
# 
# Input: path[] = "GLLG"
# Output: Given sequence of moves is circular 

def checkCircular(string):
	N = 0
	E = 1
	S = 2
	W = 3
	direction = 0
	init_pos = [0,0]
	final_pos = [0,0]
	for i in string:
		if i == 'R':
			direction = (direction + 1)%4
		if i == 'L':
			direction = (4 + direction - 1)%4

		if i == "G":
			if direction == N:
				final_pos[1]+=1
			if direction == E:
				final_pos[0] += 1
			if direction == S:
				final_pos[1] -= 1
			if direction == W:
				final_pos[0] -= 1
	if final_pos == init_pos:
		print("Circular")
	else:
		print("Not Circular")

checkCircular("GLLGRLRLRLG")

