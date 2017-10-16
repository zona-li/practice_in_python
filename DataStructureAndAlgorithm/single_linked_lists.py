class SingleLinkedListNode():

	def __init__(self, value, nxt):
		self.value = value
		self.next = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"

class SingleLinkedList():

	def __init__(self):
		self.head = None
		self.end = None
		self.count = 0

	def isEmpty(self):
		return self.head == None

	def push(self, obj):
		"""Appends a new value on the end of the list."""
		node = SingleLinkedListNode(obj, None)
		if self.head == None:
			self.head = node
		else:
			self.end.next = node
		self.end = node
		self.count += 1

	def pop(self):
		""" Delete and return the node at the end of the list. """
		cursor = self.head
		if self.isEmpty():
			raise IndexError("list is empty.")
		elif self.head == self.end:
			result = cursor.value
			self.head = None
			self.end = None
			self.count = 0
		else:
			for i in range(self.count - 2):
				cursor = cursor.next
			result = self.end.value
			self.end = cursor
			self.end.next = None
			self.count -= 1
		return result

	def unshift(self):
		""" Removes the first item and returns it. """
		if self.isEmpty():
			raise IndexError("list is empty.")
		else:
			result = self.head.value
			self.head = self.head.next
			if self.head.next == None:
				self.end = None
		return result

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


""" TESTING CODE """
def test_push():
    colors = SingleLinkedList()
    colors.push("Pthalo Blue")
    assert colors.count == 1
    colors.push("Ultramarine Blue")
    assert colors.count == 2

def test_pop():
    colors = SingleLinkedList()
    colors.push("Magenta")
    colors.push("Alizarin")
    assert colors.pop() == "Alizarin"
    assert colors.pop() == "Magenta"
    assert colors.pop() == None


test_push()
test_pop()