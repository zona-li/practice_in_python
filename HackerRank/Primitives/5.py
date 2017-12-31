'''
Write a program that multiplies two nonnegative integers. The only operators you are allowed to use are:
- assignment
- the bitwise operators
- equality checks and boolean combinations
'''


def multiply(a, b):
    def add(x, y):
        while (y != 0):
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x

    num = 0
    while a:
    	if a & 1:
    		num = add(num, b)
    	a, b = a >> 1, b << 1
    return num

print(multiply(4, 17))
