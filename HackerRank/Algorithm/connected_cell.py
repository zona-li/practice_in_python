def count_region(matrix, i, j):
	if i < 0 or j < 0 or i >= n or j >= m:
		return 0

	if matrix[i][j] == 0:
		return 0

	val = 1
	matrix[i][j] = 0

	val += count_region(matrix, i+1, j)
	val += count_region(matrix, i-1, j)
	val += count_region(matrix, i, j+1)
	val += count_region(matrix, i, j-1)
	val += count_region(matrix, i+1, j+1)
	val += count_region(matrix, i+1, j-1)
	val += count_region(matrix, i-1, j+1)
	val += count_region(matrix, i-1, j-1)

	return val

def getBiggestRegion(grid):
	count = 0
	for i in range(n):
		for j in range(m):
			num = count_region(grid, i, j)
			count = max(count, num)
	return count
    


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid, m, n))

