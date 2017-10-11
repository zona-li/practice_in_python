fruits = ['dates', 'apple', 'citris', 'banana', 'elderberry']
print(fruits[3].title())
fruits.append('orange')
fruits.insert(4, 'mango')
del fruits[5]
useDeletedFruit = fruits.pop(4)
fruits.remove('apple')
print(fruits)
print("Deleted: " + useDeletedFruit)
fruits.sort(reverse=True)
# Use sorted() to temprarily sort a list
print(fruits)
# In reverse order: list.reverse()
print("Fruits' length: " + str(len(fruits)))

##############			Working through a list			##############
for fruit in fruits:
	print(fruit)
for ints in range(1,4):
	print(ints)
evenNum = list(range(2,11,2))
print(evenNum)
print(min(evenNum))	# Also can use max(), sum()
squares = [value**2 for value in range(1,11)]
print(squares)

print("------------			Slicing a list			------------")
players = ['zona', 'thomas', 'glo', 'maleina', 'donna']
print(players[1:3])
print(players[-3:])

print("------------			Tuples			------------")
dimensions = (200, 50)
print("Original: ")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("Modified: ")
for dimension in dimensions:
	print(dimension)











