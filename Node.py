import matplotlib.pyplot as plt

class Node():
	"""docstring for Node"""
	# to construct a root: Node(value, parent = None)
	# value is a compulsory field
	# to construct a regular Node: Node(value, parent=parent, x=x, y=y)
	def __init__(self, value, x=0,  y=0, layer=0, parent=None):
		self.value = value
		self.parent = parent
		self.left = None
		self.right = None
		# layer of the node
		self.layer = layer
		# coordinate of the node in graph
		self.x = x
		self.y = y

	def isRoot(self):
		return True if self.parent == None else False

	def location(self):
		# return the location of itself in a tuple
		return (self.x, self.y)

	def parentValue(self):
		return self.parent.value if self.parent != None else None

	def parentLocation(self):
		return (self.parent.x, self.parent.y)

	def X(self):
		return self.x

	def Y(self):
		return self.y

	def killChild(self, child):
		# kill the reference to a child
		# used for deletion of the tree, guarenteed to be one of its children
		if child == None:
			return

		print(child)
		print(self)
		if self.left != None and self.left.value == child.value:
			self.left = None
			child.parent = None
		elif self.right!= None and self.right.value == child.value:
			self.right = None
			child.parent =	None



	def add(self, child):
		"""return True for left, False for right"""
		# add a child to the node
		# used for deletion of the tree, no duplicate element
		if child == None:
			return
		if child.value > self.value:
			self.right = child
			child.parent = self
			return False
		else:
			self.left = child
			child.parent = self
			return True


	def __str__(self):
		return "node value: {}, Node position: {}, Node parent value: {}".format(self.value, str(self.location()), self.parentValue())


	def next(self):
		# return the next value
		if self.right != None:
			# one step right (guaranteed larger element) and select the left most child(smallest in the larger element)
			return self.__LeftDescendant(self.right)
		else:
			# keep going up untill find the larger element
			return self.__RightAncestor(self)


	def __LeftDescendant(self, node):
		if node.left != None:
			return self.__LeftDescendant(node.left)
		else:
			return node


	def __RightAncestor(self, node):
		# handle the greatest element in the tree, and single root situation
		# if the method goes back to root (no parent) and itself is larger than root
		if node.parent == None and self.value >= node.value:
			return None
		elif node.value > self.value:
			return node
		else:
			return self.__RightAncestor(node.parent)


	def Draw(self):
		# draw the node and branch 
		plt.text(self.x, self.y, self.value)
		self.__DrawBranch()


	def __DrawBranch(self):
		# draw the branch to its parent
		if self.parent != None:
			plt.plot(*list(zip([self.x,self.y],[self.parent.x, self.parent.y])))


if __name__ == '__main__':
	n = Node(1, x=0, y= 0)
	n.parent=Node(20, x=2, y=2)
	n.Draw()
	plt.show()
	