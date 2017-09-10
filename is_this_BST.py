'''
Given the root node of a binary tree, can you determine if it's also a binary search tree?
The function has 1 parameter, which is a pointer to the root of a binary tree.
The function should return a boolean denoting whether or not the binary tree is a BST. 

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''
# Assumption: 
# The given tree is balanced;
# The data of the node is an int;

# Note: Binary search trees usually use inorder traversal, because in that way the printed tree will have the numbers in order from the smallest to the biggest. 
# 		Do null printer checks

arr = []

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBST():
	a = inOrderTraversal(root)
	first = a[0]
	for i in range(1, len(a)):
		if first >= a[i]:
			return "No"
		else:
			first = a[i]
	return "Yes"


# Inorder traversal
def inOrderTraversal(root):
	if (root.left != None):
		inOrderTraversal(root.left)
	arr.append(root.data)
	if (root.right != None):
		inOrderTraversal(root.right)
	return arr

