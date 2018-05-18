
from collections import deque
from random import randint
import math

######
# Part 1: Tree Class 
#####


class binaryTree():
	# Simple implementation of binary search tree, with insertion and search
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
		# NB! May result in non-BST if stream of values are in specific order.
		# NB! Solution to above error: (i) use createdBalancedTree(array) or (ii) implement trees with on-the-fly rotation like splay trees etc.

		if self.value < newValue: # If node value is less than added value, add on right child 
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
	# If target is in tree, returns depth and [tree path]
	# If target is not in tree, returns 0 as depth and empty list as tree path
	# If target is at root directly, returns 1 as depth and empty list
		if path == None:
			path = []
		if self.value == target:
			print("Found target. Depth = " + str(depth) + ". Path = " + str(path)) 
			return depth,path
		elif self.value < target:
			if self.right == None:
				print("Target not in Tree.")
				return (0,[])
			newDepth = depth + 1
			path.append(self.value)
			return self.right.searchTree(target,depth=newDepth,path=path) 
			# Use return even in recursion because I ultimately still want to return "depth" and "path"
		else:
			if self.left == None:
				print("Target not in Tree.")
				return (0,[])
			newDepth = depth + 1
			path.append(self.value)
			return self.left.searchTree(target,depth=newDepth,path=path)

######
# Part 2: Functions on Tree
#####

### Check for insertion and search

def checkTreeFixed(tree,target):
	depth,path = tree.searchTree(target)
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

# Helper 2
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


######
# Part 3: Creating Balanced Tree from Array (ie. Static BST)
#####


# Helper function, assumes array is sorted!
def _createBalancedTree(array):
	if array == []: # If no more values in array, stop
		return None
	else:
		midpoint = math.trunc((len(array))/2)
		root = binaryTree(array[midpoint])
		root.left = _createBalancedTree(array[0:midpoint])
		root.right = _createBalancedTree(array[midpoint+1:])
		return root

# Additional wrapper function to avoid sorting sublists
def createBalancedTree(array):
	array.sort()
	return _createBalancedTree(array)



