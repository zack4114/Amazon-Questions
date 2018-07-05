# Pairwise swap elements of a given linked list
# Given a singly linked list, write a function to swap elements pairwise. For example, 
# if the linked list is 1->2->3->4->5 then the function should change it to 2->1->4->3->5, and if 
# the linked list is 1->2->3->4->5->6 then the function should change it to 2->1->4->3->6->5.


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
	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,'->',end="")
			temp = temp.next
		print()
	def PairwiseSwap(self):
		temp = self.head
		while(temp is not None and temp.next is not None):
			temp.data,temp.next.data = temp.next.data,temp.data
			temp = temp.next.next
l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.push(6)
l.printList()
l.PairwiseSwap()
l.printList()