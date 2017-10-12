class SingleLinkedListNode(object):

	def __init__(self, value, nxt):
		self.value = value
		self.nxt = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList(object):

	def __init__(self):
		self.begin = None
		self.end = None

	def push(self, obj):


	def pop(self):


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