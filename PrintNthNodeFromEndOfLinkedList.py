# Program for n’th node from the end of a Linked List
# Given a Linked List and a number n, write a function that returns the value at the n’th node from end of the Linked List.

# For example, if input is below list and n = 3, then output is “B”
# A->B->C->D->

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
	def printNthNodeFromEnd(self,count):
		temp1 = self.head
		temp2 = self.head
		while(count > 0):
			temp1 = temp1.next
			count -=1
		while(temp1 is not None):
			temp1 = temp1.next
			temp2 = temp2.next
		print(temp2.data)
l = LinkedList()

l.push('A')
l.push('B')
l.push('C')
l.push('D')

l.printNthNodeFromEnd(3)