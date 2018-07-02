# Using Queue for BFS Traversal 
# Time Complexity is O(n)

class Tree(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None

	def child(self,lx,rx):
		if lx is not None:
			self.left = Tree(lx)
		if rx is not None:
			self.right = Tree(rx)

def BFS(root):
	q = []
	temp = root
	while(temp is not None):
		print(temp.data)
		if (temp.left is not None):
			q.insert(0,temp.left)
		if (temp.right is not None):
			q.insert(0,temp.right)
		if len(q) == 0:
			return
		temp = q.pop()

root = Tree(1)
root.child(2,None)
root.left.child(4,None)
BFS(root)
