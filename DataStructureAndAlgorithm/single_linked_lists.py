class SingleLinkedListNode():

	def __init__(self, value):
		self.value = value
		self.nxt = None

	def getVal(self):
		return self.value

	def getNxt(self):
		return self.nxt

	def setVal(self, newVal):
		self.value = newVal

	def setNxt(self, newNxt):
		self.nxt = newNxt

	def __repr__(self):
		nval = self.next and self.next.value or None
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

	def pop(self):
		""" Delete and return the node at the end of the list. """

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





temp = SingleLinkedListNode(98, None)
print(temp.getNxt())