# Sort a linked list of 0s, 1s and 2s
# Given a linked list of 0s, 1s and 2s, sort it.

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
		else:
			self.currNode.next = temp
		self.currNode = temp
	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,'->',end='')
			temp = temp.next
		print()


def sortList(l):
	count = [0]*3
	temp = l.head
	while(temp is not None):
		count[temp.data] += 1
		temp = temp.next
	temp = l.head
	i = 0
	while(temp is not None):
		while(count[i] != 0):
			temp.data = i
			temp = temp.next
			count[i]-=1
		i+=1
	return l

l = LinkedList()
l.push(0)
l.push(1)
l.push(1)
l.push(0)
l.push(1)
l.push(0)
l.push(2)
l.push(2)
l.push(0)
l.push(2)
l.push(0)
sortList(l).printList()