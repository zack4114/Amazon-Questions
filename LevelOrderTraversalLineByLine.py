#           1
#        /     \
#       2       3
#     /   \       \
#    4     5       6
#         /  \     /
#        7    8   9
# Output for above tree should be
# 1
# 2 3
# 4 5 6
# 7 8 9<

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

def LevelOrderTraversal(root):
	q = []
	q.insert(0,root)
	while(len(q) > 0):
		size = len(q)
		while(size > 0):
			temp = q.pop()
			print(temp.data,end=" ")
			if temp.left is not None:
				q.insert(0,temp.left)
			if temp.right is not None:
				q.insert(0,temp.right)
			size-=1
		print()
root = node(1)
root.child(2,3)
root.left.child(4,5)
root.right.child(None,6)
root.left.right.child(7,8)
root.right.right.child(9,None)
LevelOrderTraversal(root)

