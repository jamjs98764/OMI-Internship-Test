
from collections import deque
from random import randint

class binaryTree():
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value

	def getLeftChild(self):
		return self.left

	def getRightChild(self):
		return self.right

	def hasChildren(self):
		if self.left is not None or self.right is not None:
			return True
		else:
			return False

	def getValue(self):
		return self.value

	def setValue(self,value):
		self.value = value

	def insertNode(self,newValue):
		# Element-wise insertion for stream of values
		# If newValue == current node's value, add as left child of current node
		if self.value < newValue:
			if self.right == None: # If right node is empty, create new node
				self.right = binaryTree(newValue)
			else:
				self.right.insertNode(newValue) # Else, go down one level and repeat process
		else:
			if self.left == None:
				self.left = binaryTree(newValue)
			else:
				self.left.insertNode(newValue)

	def printDepthWise(self,levels=None): 
	# Prints node value by tree level
	# Implementation similar to breadth first search
	# List [levels] contains nodes in each particular level
		if levels == None:
			levels = [self] # First initialization, put whole tree or subtree into [levels]
		nextLevel = [] # Queue to add children nodes 
		for node in levels: # For each node in current level add their children nodes (if any) into [nextLevel]
			print (str(node.value) + ", ")
			[nextLevel.append(child) for child in [node.left,node.right] if child is not None] 
		print("NextLevel")
		if nextLevel:
			node.printDepthWise(nextLevel) # If there are children nodes in [nextLevel], do recursion

	def searchTree(self,target,depth=1,path=None): 
	# Assumes target is in tree, prints depth and path to target	
	# "Depth" and "path" are records of recursion, passed here as args to avoid using global variables
		if path == None:
			path = []
		if self.value == target:
			print("Found target. Depth = " + str(depth) + ". Path = " + str(path)) 
			return depth,path
		elif self.value < target:
			if self.right == None:
				print("Target not in Tree.")
			newDepth = depth + 1
			path.append(self.value)
			return self.right.searchTree(target,depth=newDepth,path=path) 
			# Use return even in recursion because I ultimately still want to return "depth" and "path"
		else:
			if self.left == None:
				print("Target not in Tree.")
			newDepth = depth + 1
			path.append(self.value)
			return self.left.searchTree(target,depth=newDepth,path=path)

### Check for insertion and search

def checkTreeFixed(tree,target):
	depth,path = tree.searchTree(target) # Search for 
	return depth,path

### Check for balance

# Helper 1
def treeHeight(tree):
	# Gets height of tree
	if tree.left is None and tree.right is None:
		return 1
	elif tree.left is None:
		return 1 + treeHeight(tree.right)
	elif tree.right is None:
		return 1 + treeHeight(tree.left)
	else:
		return 1 + max(treeHeight(tree.left),treeHeight(tree.right))

def treeMinHeight(tree):
	# Gets height of minimum branch
	if tree.left is None and tree.right is None:
		return 1
	elif tree.left is None:
		return 1 + treeHeight(tree.right)
	elif tree.right is None:
		return 1 + treeHeight(tree.left)
	else:
		return 1 + min(treeMinHeight(tree.left),treeMinHeight(tree.right))

def checkBalance(tree):
	# Tree is balanced is difference between maximum and minimum branch is less than or equal to 1. 
	if tree.hasChildren() == False:
		return True # Tree with only root node is balanced
	elif abs(treeHeight(tree)-treeMinHeight(tree)) <= 1:
		return True
	else:
		return False


### Create balanced tree from array

# Helper function, assumes array is sorted!
def _createBalancedTree(array):
	if array == []: # If no more values in array, stop
		return None
	else:
		midpoint = round((len(array))/2)
		root = binaryTree(array[midpoint])
		root.left = _createBalancedTree(array[0:midpoint])
		root.right = _createBalancedTree(array[midpoint+1:])
		return root

# Additional wrapper function to avoid sorting sublists
def createBalancedTree(array):
	array.sort()
	return _createBalancedTree(array)



myTree = binaryTree(11)
testList = [13,2,1,3,12,4]
# Solution:
#		11
#	2		13
# 1   3   12  
#      4
for item in testList:
	myTree.insertNode(item)
print(checkBalance(myTree))
print(treeHeight(myTree))
print(treeMinHeight(myTree))


testList = [3,2,1,4,5]
testTree = createBalancedTree(testList)
print(checkBalance(testTree))