# Use Hashing:
# Traverse the list one by one and keep putting the node addresses in a Hash Table. At any point, if NULL 
# is reached then return false and if next of current node points to any of the previously stored nodes in 
# Hash then return true.


# Floyd’s Cycle-Finding Algorithm:
# This is the fastest method. Traverse linked list using two pointers.  Move one pointer by one and other pointer by 
# two.  If these pointers meet at some node then there is a loop.  If pointers do not meet then linked list doesn’t 
# have loop.

class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.currNode = None
	def push(self,x):
		temp = node(x)
		if self.head is None:
			self.head = temp
			self.currNode = temp
		else:
			self.currNode.next = temp
			self.currNode = temp

	# Checking Loop using Hashing
	# def checkLoop(self):
	# 	temp = self.head
	# 	h = set()
	# 	while(temp is not None):
	# 		if temp in h:
	# 			return True 
	# 		h.add(temp)
	# 		temp = temp.next
	# 	return False 

	# Checking for loop using floyds method
	def checkLoop(self):
		slow_ptr = self.head
		fast_ptr = self.head
		while(slow_ptr is not None and fast_ptr is not None and fast_ptr.next is not None):
			slow_ptr = slow_ptr.next
			fast_ptr = fast_ptr.next.next
			if slow_ptr == fast_ptr and slow_ptr is not None:
				return True
		return False

l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.head.next.next.next.next.next = l.head.next
# print(l.checkLoop())
print(l.checkLoop())