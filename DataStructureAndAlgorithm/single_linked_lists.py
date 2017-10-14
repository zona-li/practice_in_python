class SingleLinkedListNode():

	def __init__(self, value):
		self.value = value
		self.nxt = None

	def __repr__(self):
		nval = self.nxt and self.nxt.value or None
		return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList():

	def __init__(self):
		self.head = None
		self.end = None

	def isEmpty(self):
		return self.head == None

	def push(self, obj):
		""" Insert the node at the end of the list. """
		node = Node(obj)
		if self.head == None:
			self.head = node
		else:
			self.end.nxt = node
		self.end = node

	def pop(self):
		""" Delete and return the node at the end of the list. """
		cursor = self.head
		if self.isEmpty():
			raise IndexError("list is empty.")
		elif self.head == self.end:
			result = cursor.value
			self.head = None
			self.end = None
		else:
			for i in range(self.count - 2):
				cursor = cursor.nxt
			result = self.end.value
			self.end = cursor
			self.end.nxt = None
		return result

	def unshift(self):
		""" Removes the first item and returns it. """

	def remove(self, obj):
		"""Finds a matching item and removes it from the list."""

	def first(self):
		"""Returns a *reference* to the first item."""

	def last(self):
		"""Returns a *reference* to the last item."""

	def count(self):
		"""Counts the number of elements in the list."""

	def get(self, index):
		"""Counts the number of elements in the list."""

	def dump(self, mark):
		"""Debugging function that dumps the contents of the list."""





temp = SingleLinkedListNode(98)
print(temp)