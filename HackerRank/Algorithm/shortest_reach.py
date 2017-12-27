import queue

'''
n: number of nodes
m: number of edges
x, y: connected nodes
s: index of the starting node

'''
class Graph(object):
	"""docstring for Graph"""
	def __init__(self, nodes_number):
		self.nodes = []
		for x in range(nodes_number):
			self.nodes.append(Node(x))

	def get(self, index):
		return self.nodes[index]

	def connect(self, x, y):
		self.nodes[x].adjancent.append(self.nodes[y])
		self.nodes[y].adjancent.append(self.nodes[x])

	def find_all_distances(self, start_node):
		self.nodes[start_node].shortest_dist = 0
		q = queue.Queue()
		q.put(self.nodes[start_node])
		self.nodes[start_node].processed = True
		while not q.empty():
			node = q.get()
			for n in node.adjancent:
				if n.processed == False:
					q.put(n)
					n.processed = True
				
			if node.shortest_dist == -1:
				shortest_distance = self.nodes[node.id - 1].shortest_dist + 6
				for adj in node.adjancent:
					if adj.shortest_dist + 6 < shortest_distance:
						shortest_distance = adj.shortest_dist + 6
				
				node.shortest_dist = shortest_distance

		for sequence_node in self.nodes:
			if sequence_node.id != start_node:
				print(sequence_node.shortest_dist)

	def __repr__(self):
		return(self.nodes)

class Node(object):
	"""docstring for Node"""
	def __init__(self, id):
		self.id = id
		self.adjancent = []
		self.shortest_dist = -1
		self.processed = False

	def __repr__(self):
		return (
			'node(' + str(self.id) + ')'
		)

		



t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)