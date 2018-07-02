# Given a binary tree, print all root-to-leaf paths
# For the below example tree, all root-to-leaf paths are: 

# 				10
# 		8				2
# 	3		5		2



# 10 –> 8 –> 3
# 10 –> 8 –> 5
# 10 –> 2 –> 2


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

def isLeafNode(root):
	if root is None:
		return False
	if root.left is None and root.right is None:
		return True
	return False

def findAllRootToPathWays(root,path,pi):
	if root is None:
		return
	path[pi] = root.data
	pi += 1
	if isLeafNode(root):
		print(path[:pi])
	else:
		findAllRootToPathWays(root.left,path,pi)
		findAllRootToPathWays(root.right,path,pi)

root = Tree(10)
root.child(8,2)
root.left.child(3,5)
path = [0]*1000
pi = 0
root.right.child(2,4)
findAllRootToPathWays(root,path,pi)
