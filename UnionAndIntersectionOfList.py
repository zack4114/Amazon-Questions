# Union and Intersection of two Linked Lists
# Given two Linked Lists, create union and intersection lists that contain union and intersection of the elements 
# present in the given lists. Order of elments in output lists doesn’t matter.

# Example:

# Input:
#    List1: 10->15->4->20
#    lsit2:  8->4->2->10
# Output:
#    Intersection List: 4->10
#    Union List: 2->8->20->4->15->10

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
			self.currNode = self.head
		else:
			self.currNode.next = temp
			self.currNode = temp

	def isInList(self,x):
		temp = self.head
		while(temp is not None):
			if temp.data == x:
				return True
			temp =temp.next
		return False
# Naive method is to travel list one and then for each element in list 1 check that element in list 2
	# def union(self,l1,l2):
	# 	if l1.head is None:
	# 		self.head = l2.head
	# 	elif l2.head is None:
	# 		self.head = l1.head
	# 	else:
	# 		temp1 = l1.head
	# 		while(temp1 is not None):
	# 			self.push(temp1.data)
	# 			temp1 = temp1.next
	# 		temp = self.head
	# 		while(temp.next is not None):
	# 			temp = temp.next
	# 		temp1 = l1.head
	# 		temp2 = l2.head
	# 		while(temp2 is not None):
	# 			if not l1.isInList(temp2.data):
	# 				temp.next = node(temp2.data)
	# 				temp = temp.next
	# 			temp2 = temp2.next

	# def intersection(self,l1,l2):
	# 	if l1.head is None:
	# 		return
	# 	elif l2.head is None:
	# 		return
	# 	else:
	# 		temp1 = l1.head
	# 		while(temp1 is not None):
	# 			temp2 = l2.head
	# 			while(temp2 is not None):
	# 				if temp1.data == temp2.data:
	# 					self.push(temp1.data)
	# 				temp2 = temp2.next
	# 			temp1 = temp1.next



# Method 2 using hashing 
	def union(self,l1,l2):
		h = set()
		temp1 = l1.head
		while(temp1 is not None):
			self.push(temp1.data)
			h.add(temp1.data)
			temp1 = temp1.next
		temp2 = l2.head
		while(temp2 is not None):
			if temp2.data not in h:
				self.push(temp2.data)
			temp2 = temp2.next

	def intersection(self,l1,l2):
		h = set()
		temp1 = l1.head
		while(temp1 is not None):
			h.add(temp1.data)
			temp1 = temp1.next
		temp2 = l2.head
		while(temp2 is not None):
			if temp2.data in h:
				self.push(temp2.data)
			temp2 = temp2.next


	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,"->",end="")
			temp = temp.next
		print()

	def testing(self,l1):
		self.head = l1.head

l1 = LinkedList()
l2 = LinkedList()
l1.push(10)
l1.push(15)
l1.push(4)
l1.push(20)
l2.push(8)
l2.push(4)
l2.push(2)
l2.push(10)
l3 = LinkedList()
l4 = LinkedList()
l3.union(l1,l2)
# l3.testing(l1)
l4.intersection(l1,l2)
l1.printList()

l2.printList()

l3.printList()

l4.printList()










