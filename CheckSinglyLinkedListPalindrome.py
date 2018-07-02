# Function to check if a singly linked list is palindrome
# Given a singly linked list of characters, write a function that returns true if the given list is palindrome, else false

# METHOD 1 (Use a Stack)
# A simple solution is to use a stack of list nodes. This mainly involves three steps.
# 1) Traverse the given list from head to tail and push every visited node to stack.
# 2) Traverse the list again. For every visited node, pop a node from stack and compare data of popped node with currently 
# visited node.
# 3) If all nodes matched, then return true, else false.

# Time complexity of above method is O(n), but it requires O(n) extra space. Following methods solve this with constant 
# extra space.


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
			print(temp.data,"->",end="")
			temp = temp.next
		print()

	def isPalindrome(self):
		stack = []
		temp = self.head
		while(temp is not None):
			stack.append(temp.data)
			temp = temp.next
		temp = self.head
		print(stack)
		while(len(stack) is not 0):
			if temp.data is not stack.pop():
				print("Not Palindrome")
				return
			temp = temp.next
		print("palindrome")
l = LinkedList()
l.push('R')
l.push('A')
l.push('D')
l.push('A')
l.push('R')
l.printList()
l.isPalindrome()


