import sys

# Using merge sort to speed up the runtime to nlog(n)
def countInversions(arr):
	copy = list(arr)
	return count_inversions(arr, 0, len(arr)-1, copy)

def count_inversions(arr, start, end, copy):
	if start >= end:
		return 0

	mid = int((start + (end - start)) / 2)
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

	while i <= mid or j <= end:
		if i > mid:
			arr[k] = copy[j]
			j += 1
			k += 1
		elif j > end:
			arr[k] = copy[i]
			k += 1
			i += 1
		elif copy[i] <= copy[j]:
			arr[k] = copy[i]
			k += 1
			i += 1
		else:
			arr[k] = copy[j]
			count += mid + 1 - i

	return count

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		arr = list(map(int, input().strip().split(' ')))
		result = countInversions(arr)
		print(result)





