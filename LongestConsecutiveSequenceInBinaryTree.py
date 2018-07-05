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

def LCSUtil(root,expected,curLen):
	global res
	if root is None:
		return
	if root.data == expected:
		curLen += 1
	else:
		curLen=1
	res = max(res,curLen)
	LCSUtil(root.left,root.data+1,curLen)
	LCSUtil(root.right,root.data+1,curLen)

def LCS(root):
	global res
	if root is None:
		return 0
	else:
		LCSUtil(root,root.data,0)
	return res

root = node(6)
root.child(None,9)
root.right.child(7,10)
root.right.right.child(None,11)
res = 0
print(LCS(root))

root1 = node(1)
root1.child(2,4)
root1.left.child(3,None)
root1.right.child(5,6)
root1.right.right.child(7,None)