class SingleLinkedListNode(object):

	def __init__(self, value, nxt):
		self.value = value
		self.nxt = nxt

	def __repr__(self):
		nval = self.next and self.next.value or None
		return f"[{self.value}:{repr(nval)}]"