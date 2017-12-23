'''
n: number of nodes
m: number of edges
x, y: connected nodes
s: index of the starting node

'''
class Graph(object):
	"""docstring for Graph"""
	def __init__(self, nodes_number):
		self.num_nodes = nodes_number
		self.nodes = []
		for x in xrange(nodes_number):
			nodes.append(Node(x))


class Node(object):
	"""docstring for Node"""
	def __init__(self, id):
		self.id = id
		self.adjancent = {}
		self.shortest_dist = -1

		


def find_all_distances(self):
	pass

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)