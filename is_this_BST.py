'''
Given the root node of a binary tree, can you determine if it's also a binary search tree?
The function has 1 parameter, which is a pointer to the root of a binary tree.
The function should return a boolean denoting whether or not the binary tree is a BST. 

https://www.hackerrank.com/challenges/ctci-is-binary-search-tree?h_r=next-challenge&h_v=zen

Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def checkBST(root):