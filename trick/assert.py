def applyDiscount(product, discount):
	amount = int(product['price'] - (1 - discount))
	assert(0 < amount < product['price'], 'Price cannot be smaller than zero and larger than the original amount')

'''
Note: 
1. Cannot assert a tuple, otherwise no matter what you put in the first argument, it will always assert true. 
2. Do not use assertion to check data, in certain conditions, asserts won't be executed at all, thus causing error. 

Example:
assert(1 == 2, 'This should fail but will not')

'''