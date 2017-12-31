'''
Write a program that multiplies two nonnegative integers. The only operators you are allowed to use are:
- assignment
- the bitwise operators
- equality checks and boolean combinations
'''
def add(x, y):
    while (y != 0):
        carry = x & y
        x = x ^ y
        y = carry << 1
    return x

def multiply(a, b):
	isOdd = False
	if b & 1 == 1:	# b is odd
		isOdd = True
	times = b >> 1
	if isOdd:
		num = a << times
		num = add(num, a)
	else:
		num = a << times
	return num


print(multiply(4, 5))