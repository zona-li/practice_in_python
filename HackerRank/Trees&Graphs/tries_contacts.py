class Node(object):
	"""The Node for Trie data structure"""
	def __init__(self, arg):
		super(Node, self).__init__()
		self.arg = arg
		


class Trie(object):
	"""docstring for Trie"""
	def __init__(self, arg):
		super(Trie, self).__init__()
		self.arg = arg
		

def add(contact):
	pass

def find(contact):
	pass

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
    	trie.add(contact)
    else:
    	print(find(contact))

