# # Level order traversal in spiral form
# # Write a function to print spiral order traversal of a tree. For below tree, function should print 1, 2, 3, 4, 5, 6, 7.
							
# 								1
# 							  /	  \
#  						    /       \
# 						  /			  \
# 						2				3
#					  /   \          /    \
# 					7		6		5		4
#                  8 9    10 11   12 13   14 15




class node(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
	def child(self,lx,rx):
		if lx is not None:
			self.left = node(lx)
		if rx is not None:
			self.right = node(rx)

def spiralTravel(root):
	q = []
	level = 0
	q.append(root)
	while(len(q) > 0):
		size = len(q)
		level+=1
		tq = []
		while(size > 0):
			if level % 2 == 0:
				temp = q.pop()
				if temp.left is not None:
					tq.insert(0,temp.left)
				if temp.right is not None:
					tq.insert(0,temp.right)
			else:
				temp = q[0]
				del(q[0])
				if temp.right is not None:
					tq.append(temp.right)
				if temp.left is not None:
					tq.append(temp.left)
			print(temp.data,'->',end="")
			
			size -=1
		q = tq
	print()



root = node(1)
root.child(2,3)
root.left.child(7,6)
root.right.child(5,4)
root.left.left.child(8,9)
root.left.right.child(10,11)
root.right.left.child(12,13)
root.right.right.child(14,15)
spiralTravel(root)



