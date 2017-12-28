def fibonacci(n, memo):
    if n <= 0:
    	return 0
    elif n == 1:
    	return 1
    elif n not in memo:
    	memo[n] = fibonacci(n-2, memo) + fibonacci(n-1, memo)
    return memo[n]
n = int(input())
print(fibonacci(n, {}))
