import sys

# Using merge sort to speed up the runtime to nlog(n)
def countInversions(arr):
	copy = list(arr)
	return count_inversions(arr, 0, len(arr)-1, copy)

def count_inversions(arr, start, end, copy):
	count = 0
	if end > start:
		mid = int((start + end) / 2)
		first_half = arr[:mid]
		second_half = arr[mid:]
		first_half_copy = list(first_half)
		second_half_copy = list(second_half)
		count = count_inversions(first_half, start, mid, first_half_copy)
		count += count_inversions(second_half, mid+1, end, second_half_copy)
		count += merge(arr, start, mid+1, end, copy)

	return count

def merge(arr, start, mid, end, copy):
	i = start
	j = mid
	k = start
	count = 0

	while i < mid and j <= end:
		if arr[j] < arr[i]:
			copy[k] = arr[j]
			j += 1
			k += 1
			count = count + mid - i
		else:
			copy[k] = arr[i]
			k += 1
			i += 1

	# Copy over the remaining elements. 
	# Only one of these two while loops will get executed. 
	while i <= mid-1:
		copy[k] = arr[i]
		k += 1
		i += 1

	while j <= end:
		copy[k] = arr[j]
		k += 1
		j += 1

	for i in range(start,end+1):
		arr[i] = copy[i]

	return count

if __name__ == "__main__":
	t = int(input().strip())
	for a0 in range(t):
		n = int(input().strip())
		arr = list(map(int, input().strip().split(' ')))
		result = countInversions(arr)
		print(result)





