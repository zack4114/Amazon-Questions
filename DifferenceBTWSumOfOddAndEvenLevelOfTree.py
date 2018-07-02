# Difference between sums of odd level and even level nodes of a Binary Tree
# Given a a Binary Tree, find the difference between the sum of nodes at odd level and the sum of nodes at even level. 
# Consider root as level 1, left and right children of root as level 2 and so on.

# For example, in the following tree, sum of nodes at odd level is (5 + 1 + 4 + 8) which is 18. And sum of nodes at even 
# level is (2 + 6 + 3 + 7 + 9) which is 27. The output for following tree should be 18 – 27 which is -9.

#       5
#     /   \
#    2     6
#  /  \     \  
# 1    4     8
#     /     / \ 
#    3     7   9  

# A straightforward method is to use level order traversal. In the traversal, check level of current node, if it is odd, 
# increment odd sum by data of current node, otherwise increment even sum. Finally return difference between odd sum and
#  even sum.

class node(object):
	def __init__(self,x):
		self.data = x
		self.left = None
		self.right = None
	def child(self,lx,rx):
		if lx is not None:
			self.left = node(lx)
		if rx is not None:
			self.right= node(rx)

def findDifference(root):
	diff = 0
	q = []
	level = 0
	q.insert(0,root)
	while(len(q) is not 0):
		size = len(q)
		level += 1
		while(size > 0):
			temp1 = q.pop()
			if temp1.left is not None:
				q.insert(0,temp1.left)
			if temp1.right is not None:
				q.insert(0,temp1.right)
			if level %2 is 1:
				diff += temp1.data
			if level % 2 is 0:
				diff -= temp1.data
			size -= 1
	print(diff)



root = node(5)
root.child(2,6)
root.left.child(1,4)
root.right.child(None,8)
root.left.right.child(3,None)
root.right.right.child(7,9)
findDifference(root)

