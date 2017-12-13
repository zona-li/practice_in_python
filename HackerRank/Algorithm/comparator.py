from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
    	return '%s %d' % (self.name, self.score)
        
    def comparator(a, b):