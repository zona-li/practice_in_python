# n: the number of elements in array 
n = int(input().strip())	

# a: n space-separated integers describing the respective values of the array
a = list(map(int, input().strip().split(' ')))

def bubble_sort(ele_num, arr):
	num_of_swaps = 0
	arr_sorted = False
	while not arr_sorted:
		arr_sorted = True
		for x in range(0,ele_num-1):
			if arr[x] > arr[x+1]:
				swap(arr, x, x+1)
				num_of_swaps += 1
				arr_sorted = False
	return num_of_swaps

def swap(arr, i, j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

result1 = str(bubble_sort(n, a))
result2 = str(a[0])
result3 = str(a[n-1])
print("Array is sorted in " + result1 + " swaps.")
print("First Element: " + result2)
print("Last Element: " + result3)















