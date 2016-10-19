import sys
import math

class Node():

	'''
	Node constructor requires a max node size
	'''
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.data = []
		self.next = None

	'''
	Allows one to delete items from the node
	'''
	def __del__(self):
		self.next = None
		del self.data

	'''
	A string representation of values in the node
	'''
	def __str__(self):
		return str(self.data)

	'''
	Returns the number of items in a node
	'''
	def __len__(self):
		return len(self.data)

	'''
	Returns the value of and item at the given index
	'''
	def __getitem__(self, index):
		return self.data[index]

	'''
	Sets the value of and item at the given index
	'''
	def __setitem__(self,key,value):
		self.data[key] = value

	'''
	Determines if the object is in the given node
	'''
	def __contains__(self,obj):
		if obj in self.data:
			return True
		else:
			return False
	
	'''
	This function creates an iterator by which one can loop through the values inside the list
	'''
	def __iter__(self):
		for x in self.data:
			yield x

	'''
	This function creates an iterator by which one can loop through the values inside the list in reverse
	'''
	def __reversed__(self):
		for x in reversed(self.data):
			yield x

	'''
	Allows items to be added to the node
	'''
	def add(self, item):
		if self.isFull():
			raise Exception('Node is full')
		self.data.append(item)

	'''
	Allows a list of items to be added to the node
	'''
	def addList(self, newList):
		if len(newList) > self.maxSize:
			raise Exception('New list is greater than max list size')
		self.data += newList

	'''
	Determines if the node has reached maxSize
	'''
	def isFull(self):
		if len(self.data) == self.maxSize:
			return True
		else:
			return False

	'''
	Determines if the node is currently empty
	'''
	def isEmpty(self):
		if len(self.data) == 0:
			return True
		else:
			return False

	'''
	Returns the current size of the node
	'''
	def size(self):
		return len(self.data)

	'''
	Removes the last item in the node
	'''
	def remove(self):
		return self.data.pop()

	'''
	Removes the first item in the node
	'''
	def removeFirstItem(self):
		return self.data.pop(0)

	'''
	Removes an item at the given index in the node
	'''
	def removeIndex(self, index):
		if index >= 0 and index < self.maxSize:
			return self.data.pop(index)
		else:
			raise IndexError()

	'''
	Removes the first x items from the node
	'''
	def removeFirstXItems(self, x):
		newList = []
		for i in range(x):
			if not self.isEmpty():
				newList.append(self.removeFirstItem())
		return newList

	'''
	Divides the node in half (rounding up) and returns the second half of the node
	'''
	def splitNode(self):
		if self.isFull():
			split = []
			newSize = math.ceil(self.size() / 2)
			while self.size() > newSize:
				split.append(self.removeIndex(newSize))
			return split