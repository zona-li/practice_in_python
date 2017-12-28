def count_possibilities(n, memo):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	elif n not in memo:
		memo[n] = count_possibilities(n-1, memo) + count_possibilities(n-2, memo) + count_possibilities(n-3, memo)
	return memo[n]

s = int(input().strip())
for a0 in range(s):
	n = int(input().strip())
	result = count_possibilities(n, {})
	print(result)

# cases:
# only 1, 2, or 3
# 1&2		> 3
# 1&3		> 4
# 2&3		> 5
# 1&2&3		> 6

start with 1 + rest
start with 2 + rest
start with 3 + rest