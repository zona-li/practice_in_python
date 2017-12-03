class Node(object):
	"""The Node for Trie data structure"""
	def __init__(self, label=None, data=None):
		self.label = label	
		self.data = data
		self.children = dict()
		
	def add_child(self, key, data=None):
		if not isinstance(key, Node):
			self.children[key] = Node(key, data)
		else:
			self.children[key.label] = key

	def __get__(self, key):
		return self.children[key]


class Trie(object):
	"""Trie data structure"""
	def __init__(self):
		self.head = Node()

	def __get__(self, key):
		return self.head.children[key]

	def add(self, word):
		current_node = self.head
		word_finished = True

		for i in range(len(word)):
			if word[i] in current_node.children:
				current_node = current_node.children[word[i]]
			else:
				word_finished = False
				break

		# For every new letter, create a new child node
		if not word_finished:
			while i < len(word):
				current_node.add_child(word[i])
				current_node = current_node.children[word[i]]
				i += 1

		# Store the full word at the end node so we don't need to trace back
		current_node.data = word

	def has_word(self, word):
		if word == '':
			return False
		if word == None:
			raise ValueError('Require a not-Null string')

		current_node = self.head
		exists = True
		for letter in word:
			if letter in current_node.children:
				current_node = current_node.children[letter]
			else:
				exists = False
				break

		if exists:
			if current_node.data == None:
				exists = False

		return exists


	def start_with_prefix(self, prefix):
		count = 0
		if prefix == None:
			raise ValueError('Requires not-Null prefix')

		top_node = self.head
		for letter in prefix:
			if letter in top_node.children:
				top_node = top_node.children[letter]
			else:
				return count

		if top_node == self.head:
			queue = [node for key, node in top_node.children.items()]
		else:
			queue = [top_node]

		while queue:
			current_node = queue.pop()
			if current_node.data != None:
				count += 1
			queue = [node for key, node in current_node.children.items()] + queue

		return count
		
n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
    	trie.add(contact)
    else:
    	print(trie.start_with_prefix(contact))

