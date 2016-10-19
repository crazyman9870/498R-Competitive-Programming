import sys
import math
from ..unrolled_linked_list.LLNode import Node

class UnrolledLinkedList():

	'''
	This is the constructor
	Sets the default values and max node capacity if unspecified
	'''
	def __init__(self, max_node_capacity=16):
		self.max_node_capacity = max_node_capacity
		self.size = 0
		self.nodeCount = 0
		self.head = None

	'''
	This method is designed search the list and remove the specified index
	If the removal causes an imbalance the reblance function is called to rebalance
	and optimize the list storage
	'''
	def __delitem__(self, index):
		#Grab Node and Index Tuple
		tup = self.getNodeIndexByIndex(index)
		#Remove the item from the list
		tup[0].removeIndex(tup[1])
		self.size -= 1
		#Rebalance the list
		if self.head is not None and self.size == 0:
			del self.head
			self.nodeCount = 0
			self.head = None
		else:
			self.rebalance(tup[0])

	'''
	This function returns the value in the at the given index of the list
	To get the location it calls a function which returns a tuple with a pointer to the given
	node and the index of the value within that node
	'''
	def __getitem__(self,index):
		tup = self.getNodeIndexByIndex(index)
		return tup[0][tup[1]]

	'''
	This function sets the item at the given key to the given value
	To get the location it calls a function which returns a tuple with a pointer to the given
	node and the index of the value within that node
	'''
	def __setitem__(self,key,value):
		tup = self.getNodeIndexByIndex(key)
		tup[0][tup[1]] = value

	'''
	This function creates an iterator by which one can loop through the values inside the list
	'''
	def __iter__(self):
		temp = self.head
		while temp is not None:
			for x in temp:
				yield x
			temp = temp.next

	'''
	This returns a string representation of the list
	The list is represented by {}
	Each node inside the list is represented by []
	The nodes in the list are separated by a comma then a space
	'''
	def __str__ (self):
		if self.head is None:
			return '{}'

		string = []
		temp = self.head
		while temp is not None:
			string.append(str(temp))
			#string.append(str(temp))
			temp = temp.next
		return '{' + ', '.join(str(x) for x in string) + '}'

	'''
	Returns the current size of the list
	'''
	def __len__(self):
		return self.size

	'''
	This function creates an iterator by which one can loop through the values inside the list
	in reverse order
	'''
	def __reversed__(self):
		nodes = []
		temp = self.head
		while temp is not None:
			nodes.append(temp)
			temp = temp.next
		nodes = nodes[::-1]
		for node in nodes:
			for x in reversed(node):
				yield x

	'''
	This function checks the list to see if it contains the value given
	'''
	def __contains__(self,obj):
		#Base Case
		if self.head is None:
			return False

		temp = self.head
		while temp is not None:
			if obj in temp:
				return True
			temp = temp.next

		return False

	'''
	This function adds a value to the list
	If the list is empty it will create a new node to store the value in
	If the node becomes full it will split the last node in the list,
	move half of the values into a new node,
	and append the new value to the new node
	'''
	def append(self,data):
		#Base Case
		if self.head is None:
			self.head = Node(self.max_node_capacity)
			self.head.add(data)
			self.size = 1
			self.nodeCount = 1
			return

		temp = self.head
		while temp.next is not None:
			temp = temp.next

		if temp.isFull():
			newList = temp.splitNode()
			temp.next = Node(self.max_node_capacity)
			temp.next.addList(newList)
			temp.next.add(data)
			self.size += 1
			self.nodeCount += 1
		else:
			temp.add(data)
			self.size += 1

	'''
	This reblance method is designed to optimize the space the nodes occupy
	When a node becomes less that half full the algorithm goes as follows:
	Caluculate the minimum number of items the current node requires to use half of it's space
	Absorbs the first x number of itmes from the next node to meet the required minimum size
	Continues on to the next node until all the nodes following the start node have been rebalanced
	'''
	def rebalance(self, startNode):
		temp = startNode.next
		minSize = math.ceil(startNode.maxSize / 2)
		while temp is not None:
			if len(startNode) < minSize:
				itemsNeeded = minSize + 1 - len(startNode)
				newItems = temp.removeFirstXItems(itemsNeeded)
				startNode.addList(newItems)
				if temp.isEmpty():
					n = temp.next
					startNode.next = n
					del temp
					self.nodeCount -= 1
				startNode = startNode.next
				if startNode is None:
					temp = None
				else:
					temp = startNode.next
			else:
				break

	'''
	This function takes and index and returns a tuple
	The tuple contains a pointer to the node that contains the given index, 
	and the index in the node where the given index points to
	'''
	def getNodeIndexByIndex(self, index):
		#Base Cases
		if self.head is None:
			raise Exception('List is empty')
		#Check to see if the abs of the index is in range
		if index < 0:
			index = self.convertNegativeIndex(index)
		if index >= self.size or index < 0:
			raise IndexError()

		#Find the node
		temp = self.head
		iMin = 0
		iMax = len(temp) - 1
		while not self.inRange(iMin, iMax, index):
			temp = temp.next
			iMin = iMax + 1
			iMax += len(temp)

		i = index - iMin
		return (temp, i)

	'''
	Returns the number of nodes that are in the given list  so far
	'''
	def nodeCount(self):
		return self.nodeCount

	'''
	A simple function given a lowerbound, upperbound, and index determines whether the index is in range
	'''
	def inRange(self, low, high, i):
		if i >= low and i <= high:
			return True
		else:
			return False

	'''
	This function converts a negative index to a valid positive index in the list
	'''
	def convertNegativeIndex(self, index):
		return self.size + index