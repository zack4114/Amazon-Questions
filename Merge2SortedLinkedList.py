# Merge two sorted linked lists
# Write a SortedMerge() function that takes two lists, each of which is sorted in increasing order, and merges the 
# two together into one list which is in increasing order. SortedMerge() should return the new list. The new list 
# should be made by splicing
# together the nodes of the first two lists.

# For example if the first linked list a is 5->10->15 and the other linked list b is 2->3->20, then SortedMerge() 
# should return a pointer to the head node of the merged list 2->3->5->10->15->20.

# There are many cases to deal with: either ‘a’ or ‘b’ may be empty, during processing either ‘a’ or ‘b’ may run 
# out first, and finally there’s the problem of starting the result list empty, and building it up while going 
# through ‘a’ and ‘b’.

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
	def printLinkedList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,'->',end = "")
			temp = temp.next
		print()

	def mergeTwoSortedLinkedList(self,l1,l2):
		temp1 = l1.head
		temp2 = l2.head
		while(temp1 is not None and temp2 is not None):
			if temp1.data < temp2.data:
				self.push(temp1.data)
				temp1 = temp1.next
			else:
				self.push(temp2.data)
				temp2 = temp2.next
		while(temp1 is not None):
			self.push(temp1.data)
			temp1 = temp1.next
		while(temp2 is not None):
			self.push(temp2.data)
			temp2 = temp2.next

l1 = LinkedList()
l2 = LinkedList()
l3 = LinkedList()
l1.push(5)
l1.push(10)
l1.push(15)
l2.push(2)
l2.push(3)
l2.push(20)
l1.printLinkedList()
l2.printLinkedList()
l3.mergeTwoSortedLinkedList(l1,l2)
l3.printLinkedList()