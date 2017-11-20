class SingleLinkedListNode(object):

	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		return f"{self.value}"

class SingleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None

	def push(self, obj):
		"""Appends a new value on the end of the list."""
		node = SingleLinkedListNode(obj, None)
		if self.begin == None:
			self.begin = node
			self.end = self.begin
		else:
			self.end.next = node
			self.end = node

	def pop(self):
		""" Delete and return the node at the end of the list. """
		if self.end == None:
			return None
		elif self.begin == self.end:
			node = self.begin
			self.end = self.begin = None
			return node.value
		else:
			node = self.begin
			while node.next != self.end:
				node = node.next
			self.end = node
			return node.next.value

	def unshift(self):
		""" Removes the first item and returns it. """
		if self.begin == None:
			return None
		else:
			node = self.begin
			self.begin = node.next
			if node.next == None:
				self.end = None
			return node.value

	def remove(self, obj):
		"""Finds a matching item and removes it from the list."""

	def first(self):
		"""Returns a *reference* to the first item."""

	def last(self):
		"""Returns a *reference* to the last item."""

	def count(self):
		"""Counts the number of elements in the list."""
		node = self.begin
		count = 0
		while node:
			count += 1
			node = node.next
		return count

	def get(self, index):
		"""Counts the number of elements in the list."""

	def dump(self, mark):
		"""Debugging function that dumps the contents of the list."""
