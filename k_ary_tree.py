# k-ary tree

import types
from queue import Queue
from itertools import repeat

class K_ary_Tree():
	def __init__(self, k, value=None):
	
		self.__root = value
		self.__left = []
		self.__right = []
		self.__middle = None
		
		self.__childrenPerNode = k
		self.__searchRange = int(k/2)
		
		self.__parent = None
		self.__depth = 0
		self.__height = 0
		self.__width = 0
		
	# Public operations
	
	def Insert(self, value):
		# To avoid confusion, I will point out that "insert" and "Insert" are two operations, each operating on a different data type.  
		# "insert" is one of the built-in List methods in Python, and "Insert" is the tree insertion method.  

		if type(self.__root) == type(None) and type(self.__parent) == type(None):
			# The current tree under inspection is empty, so we can create a root and assign it the value
			
			self.__root = value
			self.__height = 1
				
		else:
				
			if value == self.__root:
				
				if self.__childrenPerNode % 2 != 0 and type(self.__middle) == type(None):
					# If the number of children per node is odd, then there will be a middle node.  
					# If there is no middle child, create one.  
					
					self.__middle = K_ary_Tree(self.__childrenPerNode, value)
				
					self.__middle.__parent = self
					self.__middle.__depth = self.__depth + 1
					self.__middle.__height += 1
					
					if len(self.__left) + len(self.__right) == 0:
						self.__height += 1
						
				
				elif self.__childrenPerNode % 2 == 0:
					# If the number of children per node is even, then there will be no middle node.
					# I have arbitrarily chosen to insert the value into the left subtree if the number of children per node is even
					
					if len(self.__left) == 0:

						newLeftNode = K_ary_Tree(self.__childrenPerNode, value)
						newLeftNode.__parent = self
						newLeftNode.__depth = self.__depth + 1
						newLeftNode.__height += 1
						
						self.__left.append(newLeftNode)
						
						if len(self.__right) == 0:
							self.__height += 1
				
					else:
						self.__subtreeInsert(value, self.__left)
					
				else:
					# If there is a middle child, descend until an empty middle child is found.
					
					nodesWithChildren = 0
								
					for node in frozenset(self.__left).union(frozenset(self.__right)).union(frozenset([self.__middle])):
						if type(node) != type(None):
							if len(node.__left) > 0 or len(node.__right) > 0 or type(node.__middle) != type(None):
								nodesWithChildren += 1
										
					if nodesWithChildren == 0:
						self.__height += 1
						
					self.__middle.Insert(value)
					
					if self.__height <= self.__middle.__height:
						self.__height = self.__middle.__height + 1
			
			elif value < self.__root:
				if len(self.__left) == 0:
					# Nothing exists in the left subtree yet, so just insert it in the first spot
					
					newLeftNode = K_ary_Tree(self.__childrenPerNode, value)
					
					newLeftNode.__parent = self
					newLeftNode.__depth = self.__depth + 1
					newLeftNode.__height += 1
					
					self.__left.append(newLeftNode)
					
					if len(self.__right) == 0 and type(self.__middle) == type(None):
						self.__height += 1
				else: 
					self.__subtreeInsert(value, self.__left)		
					
			else:
				if len(self.__right) == 0:
					# Nothing exists in the right subtree yet, so just insert it in the first spot
					
					newRightNode = K_ary_Tree(self.__childrenPerNode, value)
					
					newRightNode.__parent = self
					newRightNode.__depth = self.__depth + 1
					newRightNode.__height += 1
					
					self.__right.append(newRightNode)
					
					if len(self.__left) == 0 and type(self.__middle) == type(None):
						self.__height += 1

				else:
					self.__subtreeInsert(value, self.__right)
		
		heightList = []		
		
		for node in frozenset(self.__left).union(frozenset(self.__right)).union(frozenset([self.__middle])):
			if type(node) != type(None):
				heightList.append(node.__height)
		
		if len(heightList) > 0:
			self.__height = max(heightList) + 1
			
		else:
			self.__height = 1
		
		# Update the width of the tree

		self.__width = pow(self.__childrenPerNode, self.__height - 1)
	
	def Delete(self, value):
		# Start at the root and descend down based on the ordering rules until the value is found
		
		listIndex = None
		subtree = None
		valueFound = False
		
		if type(self.__parent) == type(None) and type(self.__root) == type(None):
			# The tree is empty
			raise ValueNotFound(value, True)
			
		else:
			if value == self.__root:
				valueFound = True
				subtree = 'Middle'
				successor = self.__treeSuccessor()
				
				if type(successor) == type(None):
					self.__root = None
					self.__height = 0
					if type(self.__parent) != type(None):
						self.__parent.__middle = None
		
				else:
					self.__transplant(successor, listIndex, subtree)

			elif value < self.__root:
				# search the left subtree 
				if len(self.__left) == 0:
					raise ValueNotFound(value, False)
					
				else:
					nodeCount = 0
					
					while nodeCount < len(self.__left) and not valueFound:
						if value == self.__left[nodeCount].__root:
							valueFound = True
							listIndex = nodeCount
							subtree = 'Left'
							
							successor = self.__left[nodeCount].__treeSuccessor()
							
							if type(successor) == type(None):
								if type(self.__left[nodeCount].__parent) == type(None):
									self.__left[nodeCount].__root = None
								else:
									if len(self.__left[nodeCount].__parent.__left) - 1 == 0 and len(self.__left[nodeCount].__parent.__right) == 0 and type(self.__left[nodeCount].__parent.__middle) == type(None):
										self.__left[nodeCount].__parent.__height -= 1
										
									self.__left.pop(nodeCount)
										
							else:
								self.__left[nodeCount].__transplant(successor, listIndex, subtree)
								del successor
								
						else:
							try:
								self.__left[nodeCount].Delete(value)
							except ValueNotFound:
								nodeCount += 1
							else:
								valueFound = True
				
				if not valueFound:
					raise ValueNotFound(value, False)
			
			else:
				# search the right subtree
				if len(self.__right) == 0:
					raise ValueNotFound(value, False)
				
				else:
					nodeCount = 0
				
					while nodeCount < len(self.__right) and not valueFound:
						if value == self.__right[nodeCount].__root:
							valueFound = True
							listIndex = nodeCount
							subtree = 'Right'
							
							successor = self.__right[nodeCount].__treeSuccessor()
							
							if type(successor) == type(None):
								if type(self.__right[nodeCount].__parent) == type(None):
									self.__right[nodeCount].__root = None
								else:
									if len(self.__right[nodeCount].__parent.__left) == 0 and len(self.__right[nodeCount].__parent.__right) - 1 == 0 and type(self.__right[nodeCount].__parent.__middle) == type(None):
										self.__right[nodeCount].__parent.__height -= 1
											
									self.__right.pop(nodeCount)
									
							else:
								self.__right[nodeCount].__transplant(successor, listIndex, subtree)
								del successor	
						
						else:
							try:
								self.__right[nodeCount].Delete(value)
							except ValueNotFound:
								nodeCount += 1
							else:
								valueFound = True
				if not valueFound:
					raise ValueNotFound(value, False)
		
		# Update the height and width of the tree
		
		heightList = []		
		
		for node in frozenset(self.__left).union(frozenset(self.__right)).union(frozenset([self.__middle])):
			if type(node) != type(None):
				heightList.append(node.__height)
		
		if len(heightList) > 0:
			self.__height = max(heightList) + 1
			
		else:
			self.__height = 1
		
		self.__width = pow(self.__childrenPerNode, self.__height - 1)
		
		
	def Print(self):
		# Pretty print the tree
		
		q = Queue()
		q.put(self)
		
		row = []
			
		currentDepth = 0
		
		outputWidth = self.__width * 2 - 1
		firstNodeLocation = int(outputWidth/2)
		step = int(outputWidth/self.__childrenPerNode)
		
		map = {}
		
		treeMaxStrLen = len(str(self.__treeMax()[0].__root))
		
		if treeMaxStrLen > 4:
			pass
		else:
			treeMaxStrLen = 4
			
		treeMaxSpace = ''.rjust(treeMaxStrLen)
		stringLen = outputWidth * treeMaxStrLen
		
		if (self.__height - 1) == 0:
			nodeToInspect = q.get()
			
			row += list(repeat(treeMaxSpace, step))
			row.append(str(nodeToInspect.__root).center(treeMaxStrLen))
			
			map[currentDepth] = row
			
		else:
			while currentDepth <= (self.__height - 1):
				nodeToInspect = q.get()
			
				if nodeToInspect.__depth == currentDepth:
					
					if nodeToInspect.__depth == 0:
						row += list(repeat(treeMaxSpace, firstNodeLocation))
					else:
						row += list(repeat(treeMaxSpace, step))
					
					row.append(str(nodeToInspect.__root).center(treeMaxStrLen))
				  
				elif nodeToInspect.__depth > (self.__height - 1):
					currentDepth = nodeToInspect.__depth
					break
				
				else:
					row = []
					currentDepth += 1
					firstNodeLocation = int(firstNodeLocation/self.__childrenPerNode)
					
					if currentDepth > 1:
						step = int(step/self.__childrenPerNode)
					
					row += list(repeat(treeMaxSpace, firstNodeLocation))
					row.append(str(nodeToInspect.__root).center(treeMaxStrLen))
					
				
				map[currentDepth] = row
				
				for node in nodeToInspect.__left:
					q.put(node)
				
				if len(nodeToInspect.__left) < self.__searchRange:
					for space in range(0, (self.__searchRange - len(nodeToInspect.__left))):
						leaf = K_ary_Tree(self.__childrenPerNode)
						leaf.__depth = nodeToInspect.__depth + 1
						q.put(leaf)
				
				if type(nodeToInspect.__middle) != type(None):
					q.put(nodeToInspect.__middle)
					
				else:
					if self.__childrenPerNode %2 != 0:
						leaf = K_ary_Tree(self.__childrenPerNode)
						leaf.__depth = nodeToInspect.__depth + 1
						q.put(leaf)
				
				
				for node in nodeToInspect.__right:
					q.put(node)
				
				if len(nodeToInspect.__right) < self.__searchRange:
					for space in range(0, (self.__searchRange - len(nodeToInspect.__right))):
						leaf = K_ary_Tree(self.__childrenPerNode)
						leaf.__depth = nodeToInspect.__depth + 1
						q.put(leaf)

		for key in range(0, currentDepth + 1):
			if key in map.keys():
				output = ''.join(map[key])
				print (output.ljust(stringLen))
	
	
	# Private operations
	
	def __subtreeInsert(self, value, nodeList):
	
		if len(nodeList) == self.__searchRange:
			# Find a child to insert under
		
			minHeight = nodeList[0].__height
			
			for node in nodeList:
				if node.__height <= minHeight:
					minHeight = node.__height
				
			
			nodeCount = 0
					
			while nodeCount < self.__searchRange:
				if not nodeList[nodeCount].__isComplete():
					nodesWithChildren = 0
								
					for node in frozenset(self.__left).union(frozenset(self.__right)).union(frozenset([self.__middle])):
						if type(node) != type(None):
							if len(node.__left) > 0 or len(node.__right) > 0 or type(node.__middle) != type(None):
								nodesWithChildren += 1
										
					if nodesWithChildren == 0:
						self.__height += 1
							
					nodeList[nodeCount].Insert(value)
							
					if self.__height <= nodeList[nodeCount].__height:
						self.__height = nodeList[nodeCount].__height + 1	
					break
				
				else:
					if nodeList[nodeCount].__height <= minHeight:
						nodeList[nodeCount].Insert(value)
							
				nodeCount += 1
			
			
		else: 
			newNode = K_ary_Tree(self.__childrenPerNode, value)
			emptySpotFound = False
				
			# iterate over the entire node list to find an empty spot
			
			nodeCount = 0
			
			while nodeCount < len(nodeList) and not emptySpotFound:
				if value < nodeList[nodeCount].__root:
					newNode.__parent = self
					newNode.__depth = self.__depth + 1
					newNode.__height += 1
					
					nodeList.insert(nodeCount, newNode)
					emptySpotFound = True
								
							
				elif value == nodeList[nodeCount].__root:
					nodesWithChildren = 0
								
					for node in frozenset(self.__left).union(frozenset(self.__right)).union(frozenset([self.__middle])):
						if type(node) != type(None):
							if len(node.__left) > 0 or len(node.__right) > 0 or type(self.__middle) != type(None):
								nodesWithChildren += 1
										
					if nodesWithChildren == 0:
						self.__height += 1
								
					if self.__childrenPerNode % 2 != 0:
						nodeList[nodeCount].__middle.Insert(value)
								
						if self.__height <= nodeList[nodeCount].__middle.__height:
							self.__height = nodeList[nodeCount].__middle.__height + 1
					else:
						nodeList[nodeCount].Insert(value)
								
						if self.__height <= nodeList[nodeCount].__height:
							self.__height = nodeList[nodeCount].__height + 1
									
					emptySpotFound = True
								
				nodeCount += 1
					
			if not emptySpotFound:
				newNode.__parent = self
				newNode.__depth = self.__depth + 1
				newNode.__height += 1
				nodeList.append(newNode)
							
	def __treeSuccessor(self):
		successor = None
		
		if len(self.__left) == 0 and len(self.__right) == 0 and type(self.__middle) == type(None):
			pass
			
		else:
			if type(self.__middle) != type(None):
				# If there is a middle child, find where the chain of equal nodes ends and delete the bottom-most middle child
				[successor, subtree] = self.__middle.__lowestMiddleChild()
				
				if (len(successor.__parent.__left) + len(successor.__parent.__right)) == 0:
					self.__middle.__lowestMiddleChild()[0].__parent.__height -= 1
				
				self.__middle.__lowestMiddleChild()[0].__parent.__middle = None
				
			elif len(self.__right) == 0:
				# If there are no right or middle children, find the maximum-valued child of the right-most left subtree 
				[successor, subtree] = self.__left[len(self.__left) - 1].__treeMax()

				if (len(successor.__parent.__left) - 1 + len(successor.__parent.__right)) == 0 and type(successor.__parent.__middle) == type(None):
					self.__left[len(self.__left) - 1].__treeMax()[0].__parent.__height -= 1 # double check

				if type(subtree) == type(None):
					self.__left.pop(len(self.__left) - 1)
				
				elif subtree == 'Right':
					self.__left[len(self.__left) - 1].__treeMax()[0].__parent.__right.pop(len(self.__right) - 1)
					
				elif subtree == 'Middle':
					self.__left[len(self.__left) - 1].__treeMax()[0].__parent.__middle = None
					
				else:
					self.__left[len(self.__left) - 1].__treeMax()[0].__parent.__left.pop(len(self.__left) - 1) # double check
			
			else:
				# If there is a right child, find the minimum-valued child of the left-most right subtree 
				[successor, subtree] = self.__right[0].__treeMin()
			
				if (len(successor.__parent.__left) - 1 + len(successor.__parent.__right)) == 0 and type(successor.__parent.__middle) == type(None):
					self.__right[0].__treeMin()[0].__parent.__height -= 1
					
				if type(subtree) == type(None):
					self.__right.pop(0)
				
				elif subtree == 'Right':
					self.__right[0].__treeMin()[0].__parent.__right.pop(0)
					
				elif subtree == 'Middle':
					self.__right[0].__treeMin()[0].__parent.__Middle = None
					
				else:
					self.__right[0].__treeMin()[0].__parent.__left.pop(0)
				
		return successor
				
			
	def __transplant(self, successor, listIndex, subtree):
		# This operation swaps the successor with the node to delete (self)
		
		self.__root = successor.__root
		
		# Insert the successor's children into the appropriate locations
		
		if type(self.__middle) == type(None):
			self.__middle = successor.__middle
			
		else:
			self.__lowestMiddleChild()[0].__middle = successor.__middle

		# Fill the remaining holes in the current node's left subtree
			
		while len(successor.__left) > 0:  
			nodeCount = 0
			emptySpotFound = False
			newLeftNode = successor.__left.pop(0)
			
			self.__subtreeInsert(newLeftNode.__root, self.__left)
		
		# Fill the remaining holes in the current node's right subtree
		
		while len(successor.__right) > 0:      
			nodeCount = 0
			emptySpotFound = False
			newRightNode = successor.__right.pop(0)
			
			self.__subtreeInsert(newRightNode.__root, self.__right)
		
		del successor
					
				
	def __lowestMiddleChild(self):
		# Find the middle child with the highest depth
		subtree = None
		
		if type(self.__middle) != type(None):
			subtree = 'Middle'
			node = self.__middle

			while type(node.__middle) != type(None):
				node = node.__middle
	
		else:
			node = self
				
		return [node, subtree]
	
	def __treeMax(self):
		# Find the maximum element of the tree
		subtree = None
		
		if len(self.__right) > 0:
			subtree = 'Right'
			node = self.__right[len(self.__right) - 1]
	
			while type(node) != type(None):
				try:
					node = node.__right[len(node.__right) - 1]
				except IndexError:
					break

		else:
			[node, subtree] = self.__lowestMiddleChild()
	
		return [node, subtree]


	def __treeMin(self):
		# Find the minimum element of the tree
		subtree = None
		
		if len(self.__left) > 0:
			node = self.__left[0]
			subtree = 'Left'
			while type(node) != type(None):
				try:
					node = node.__left[0]
				except IndexError:
					break
	
		else:
			node = self.__lowestMiddleChild()[0]
		
		return [node, subtree]
		

	def __isComplete(self):
		# Determine if the tree is complete
		complete = False

		if ((self.__childrenPerNode % 2 != 0) and (type(self.__middle) != type(None)) and (len(self.__left) + len(self.__right) == self.__childrenPerNode - 1)):
			complete = True
		elif ((self.__childrenPerNode % 2 == 0) and (type(self.__middle) == type(None)) and (len(self.__left) + len(self.__right) == self.__childrenPerNode)):
			complete = True
		
		return complete	
		
# A simple exception class
class ValueNotFound(Exception):
	def __init__(self, value, isEmpty):
		self.value = value
		self.isEmpty = isEmpty


def main():
	#	Get user input for the k-value
	
	k = int(input('Enter a value for the number of children each node should have: '))
	
	#	Initialize k-ary tree
	
	tree = K_ary_Tree(k)
	
	choice = ""
	
	while (choice != "E"):
		#	Ask the user to choose to insert, delete or search for an item, or exit
	
		choice = input('Would you like to Insert (I), Delete (D), Print (P), Restart (R) or Exit (E)? ')
		
		if choice == 'I':
			value = int(input("Choose an integer value to insert: "))
			tree.Insert(value)

			
		elif choice == 'D':
			# First, might need to explicitly check if the tree is empty or not... it could be handled below, though.
			value = int(input("Choose an integer value to delete: "))
		
			try:
				tree.Delete(value)
			except ValueNotFound as e:
				if e.isEmpty == False:
					print ("Cannot delete the value '" + str(e.value) + "', because it doesn\'t exist in the tree.")
				else:
					print ("The tree is empty.")
		
		elif choice == 'P':
			tree.Print()
			
		elif choice == 'R':
			#	Get user input for the k-value
	
			k = int(input('Enter a value for the number of children each node should have: '))
	
			#	Initialize k-ary tree
	
			tree = K_ary_Tree(k)
	
			choice = ""
			
		elif choice == 'E':
			print ("Goodbye!")
			exit(0)
			
		else:
			print('That wasn\'t a valid choice.')
	
	
if __name__ == "__main__":
    main()
