import sys

# Using merge sort to speed up the runtime to nlog(n)
def countInversions(arr):
	copy = list(arr)
	return count_inversions(arr, 0, len(arr)-1, copy)

def count_inversions(arr, start, end, copy):
	if start >= end:
		return 0
	mid = end / 2
	count = 0
	count += count_inversions(copy, start, mid, arr)
	count += count_inversions(copy, mid+1, end, arr)
	count += merge(arr, start, mid, end, copy)

	return count

def merge(arr, start, mid, end, copy):
	i = start
	j = mid+1
	k = start
	count = 0

	while i <= mid && j <= end:
		

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		arr = list(map(int, input().strip().split(' ')))
		result = countInversions(arr)
		print(result)