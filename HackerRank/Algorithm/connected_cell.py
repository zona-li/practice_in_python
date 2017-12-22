class Cell(object):
	"""docstring for Cell"""
	def __init__(self, m, n):
		self.arg = arg
		

def addAdjancent(m, n):
	pass

def getBiggestRegion(grid, m, n):
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 1:
				pass
			else:
				pass

	# return(grid[0][3])
    


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid, m, n))

