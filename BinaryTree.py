from Node import *
import sys

class Tree():
	"""docstring for Tree"""
	"""There is no duplicate element"""
	def __init__(self, widthx, heighty, rootx=0, rooty=0, value=None):
		# widthx is the width of the first branch (from root to its child)
		# heighty is the height of each layer of tree 
		self.rootx = rootx
		self.rooty = rooty
		self.widthx = widthx
		self.heighty = heighty

		if value == None:
			self.root = None
		else:
			# the root should always be at the (rootx, rooty)
			self.__setRoot(node = Node(value))



	def __setRoot(self, node):
		self.root = node
		node.x = self.rootx
		node.y = self.rooty
		node.parent=None
		node.layer = 0

	def __leftmost(self):
		# return the smallest node in the tree
		node = self.root
		while True:
			if node.left == None:
				break
			node = node.left
		return node


	def __iter__(self, asNode=False):
		return self.Tree_iter(self.__leftmost(), asNode=asNode)

	def __updateTreeCoordinate(self, node, left=False, right=False, singleLayer=False):
		# update the coordinate of all its children by default
		# cand only update right children or left children
		layer = node.layer + 1
		if left == True and node.left != None:
			# update the coordinate
			x = node.x - self.widthx/(2**node.layer)
			y = node.y - self.heighty
			node.left.x = x
			node.left.y = y
			node.left.layer = layer
			if singleLayer == False:
				self.__updateTreeCoordinate(node.left, left=True, right=True)

		if right == True and node.right !=None:
			# update the coordinate
			x = node.x + self.widthx/(2**node.layer)
			y = node.y - self.heighty
			node.right.x = x
			node.right.y = y
			node.right.layer = layer
			if singleLayer == False:
				self.__updateTreeCoordinate(node.right, left=True, right=True)


	def find(self, key):
		# return the node which has the key, else return the node where the item should be
		return self.__find(self.root, key)


	def __find(self, node, key):
		# recursively find the elememt
		if node.value == key:
			return node
		elif node.value > key:
			# handle the case where the expected node does not exist
			if node.left == None:
				return node
			return self.__find(node.left, key)
		elif node.value < key:
			if node.right == None:
				return node
			return self.__find(node.right,key)


	def rangeSearch(self, start, end):
		# return the range of values in the tree
		# inclusive
		node = self.find(start)
		result = []		
		if node.value < start:
			node = node.next()
		while node.value <= end:
			result.append(node.value)
			node = node.next()
		return result


	def insert(self, value):
		# insert first element
		if self.root == None: 
			self.__setRoot(Node(value))
		else:
			self.__insert(self.root, value)
		

	def __insert(self, node, value):
		if node.value > value:
			if node.left == None:
				node.left = Node(value, parent=node)
				self.__updateTreeCoordinate(node, left=True, singleLayer=True)
			else:
				self.__insert(node.left, value) 

		elif node.value < value:
			if node.right == None:		
				node.right = Node(value, parent=node)
				self.__updateTreeCoordinate(node, right=True, singleLayer=True)
			else:
				self.__insert(node.right, value)


	def delete(self, value):
		"""
		edge cases
		edge case: delete the root
		"""
		node = self.find(value)
		if node.right == None:
			# left gets promoted
			left = node.left
			if node.isRoot():
				node.killChild(left)
				self.__setRoot(left)
				self.__updateTreeCoordinate(self.root, left=True, right=True)
				return
			parent = node.parent
			parent.killChild(node)
			left = parent.add(left)
			self.__updateTreeCoordinate(parent ,left=left, right=not left)
		else:
			# guarenteed to have next
			"""
		 	edge cases

			handle the case where there is no next (node could be root)
			# the node is guarenteed to have right child, which means the node is guarenteed to have next
			next is root (next has no parent)
			# next will never be root, since the node must have a right child 
			"""
			# replace it by next element, next's right gets be appended to next's place
			_next = node.next()

			# next is guarenteed not to have child to its left
			nextParent = _next.parent
			nextRight = _next.right

			# swap node and next
			node.value = _next.value

			# safely remove next

			nextParent.killChild(_next)
			_next.killChild(nextRight)
			if nextRight != None:
				nextParent.add(nextRight)
				nextRight.x = _next.x
				nextRight.y = _next.y
				self.__updateTreeCoordinate(nextRight, left=True, right=True)

				
	def Draw(self, delay=0):
		# delay is in milisecond
		# draw the tree
		node_iter = self.__iter__(asNode=True)
		for i in node_iter:
			i.Draw()
			plt.draw() 
			if delay != 0:
				plt.pause(delay/1000)
		plt.show()


	class Tree_iter():
		def __init__(self, node, asNode):
			self.current = node
			self.previous = None
			self.asNode = asNode


		def __iter__(self):
			return self


		def __next__(self):
			# fix the error when there is only a root in the tree
			if self.current == None:
				raise StopIteration
			self.previous = self.current
			self.current = self.current.next()
			return self.previous.value if self.asNode == False else self.previous


if __name__ == '__main__':
	def main(args):
		t = Tree(value=6, widthx=20, heighty=20)
		t.insert(2)
		t.insert(4)
		t.insert(-12)
		t.insert(3.5)
		t.insert(-14)
		t.insert(-15)
		t.insert(-13)
		t.insert(3)
		t.insert(5)
		t.insert(3.75)
		t.insert(10)
		t.insert(15)
		t.insert(7)
		t.insert(8)
		t.insert(12)
		t.insert(50)
		for i in args:
			t.delete(i)


		t.Draw(1)

	args = [int(i) for i in sys.argv[1:]]

	main(args)


	# n = t.find(4)
	# print(n)
	# print(n.next())

	# print(list(t))


	# for i in t.__iter__(asNode=True):
	# 	print(i)