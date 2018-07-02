# Add two numbers represented by linked lists | Set 1
# Given two numbers represented by two lists, write a function that returns sum list. The sum list is list 
# representation of addition of two input numbers.

# Example 1

# Input:
#   First List: 5->6->3  // represents number 365
#   Second List: 8->4->2 //  represents number 248
# Output
#   Resultant list: 3->1->6  // represents number 613
# Example 2

# Input:
#   First List: 7->5->9->4->6  // represents number 64957
#   Second List: 8->4 //  represents number 48
# Output
#   Resultant list: 5->0->0->5->6  // represents number 65005

class node(object):
	def __init__(self,x):
		self.data = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None

	def pushAtBeginning(self,x):
		temp = node(x)
		temp.next = self.head
		self.head = temp

	def sumTwoList(self,first,second):
		temp = None
		prev = None
		carry = 0
		i = 0
		while(first is not None or second is not None):
			firstData = 0 if first is None else first.data
			secondData = 0 if second is None else second.data
			Sum = carry+firstData+secondData


			carry = 1 if Sum >= 10 else 0
			Sum = Sum if Sum < 10 else Sum%10

			temp = node(Sum)
			if self.head is None:
				self.head = temp
			else:
				prev.next = temp
			prev = temp

			if first is not None:
				first = first.next
			if second is not None:
				second = second.next
		if carry > 0:
			temp.next = node(carry)

	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data,"->",end="")
			temp = temp.next

first = LinkedList()
second = LinkedList()
res = LinkedList()
first.pushAtBeginning(6)
first.pushAtBeginning(4)
first.pushAtBeginning(9)
first.pushAtBeginning(5)
first.pushAtBeginning(7)
second.pushAtBeginning(4)
second.pushAtBeginning(8)
first.printList()
print()
second.printList()
print()
res.sumTwoList(first.head,second.head)
res.printList()

