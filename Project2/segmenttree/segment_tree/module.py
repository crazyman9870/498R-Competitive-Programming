import sys

class SegmentTreeNode():

	def __init__(self, nodeSum=0, leftIndex=0, rightIndex=0):
		self.nodeSum = nodeSum
		self.leftIndex = leftIndex
		self.rightIndex = rightIndex

	def __str__(self):
		string = '(' + str(self.nodeSum) + ', [' + str(self.leftIndex) \
			+ ', ' + str(self.rightIndex) + '])'
		return string

	def getSum(self):
		return self.nodeSum

	def setSum(self, newSum):
		self.nodeSum = newSum

	def getLeftIndex(self):
		return leftIndex

	def setLeftIndex(self, index):
		self.leftIndex = index

	def getRightIndex(self):
		return rightIndex

	def setRightIndex(self, index):
		self.leftIndex = index


class SegmentTree(object):
	
	'''
	SegmentTree Constructor
	size = size of the list
	nodeCount = the number of nodes in the tree
	tree = the entire tree
	leaves = the items in the list
	initiallizes the tree and leaves with zeros
	'''
	def __init__(self, size):

		self.size = size
		self.nodeCount = (size * 2) - 1 
		self.tree = []
		self.leaves = []

		for z in range(self.size):
			self.leaves.append(0)

		for z in range(self.nodeCount):
			self.tree.append(SegmentTreeNode())

		self.initTree()

	def initTree(self):

		for i in range(len(self.tree)):
			print(i, self.tree[i])

		#for i in range(self.size, self.nodeCount, 1):

		
		#leftpos = (2 * treepos) + 1
		#rightpos = (2 * treepos) + 2
		
		#for z in range(self.nodes):
		#	tree.append((0, [0,0]))

	'''
	Returns the size of the list
	'''
	def __len__(self):
		return self.size

	'''
	Returns the number of nodes in the tree
	'''
	def treeSize(self):
		return self.nodeCount

	def setValue(self, value, index):

		self.leaves[index] = value

		print('setValue')

	def getSum(self, indexLeft, indexRight):
		print('getSum')

class SegmentTreeMax(object):
	def __init__(self, size):
		self.size = size

class SegmentTreeScheduler(object):
	def __init__(self, size):
		self.size = size

