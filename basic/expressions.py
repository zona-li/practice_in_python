print("------------			If Statements			------------")
answer = 17
question = 20
if answer == 17 and question == 20:
	print("Correct!")

banned_users = ['andrew', 'James', 'caroline']
usr = 'andrew'
if usr not in banned_users:
	print("You have access to this computer!")
elif usr in banned_users:
	print("You are banned from using this computer")
else:
	print("Sorry, you cannot use this computer")

requested_toppings = []
if requested_toppings:
	print("Yum yum")
else:
	print("This pizza is going to taste aweful")

print("------------			Dictionaris			------------")
alien = {'color': 'green', 'points': 5}
alien['x_pos'] = 0
alien['y_pos'] = 25
print(alien)
alien['color'] = 'yellow'
del alien['points']
print(alien)
# Dictionaty with similar objects
languages = {
	'zona': 'swift',
	'xiong': 'python',
	'sarah': 'java',
	'glo': 'python',
}
print("Zona's favorite language is " + languages
	['zona'].title() + ".")
for key, value in languages.items():
	print("Key: " + key)
	print("Value: " + value)
for name in languages.keys(): # This is the same as "for language in languages:" 
	print(name)
for language in set(languages.values()): # Set will remove the duplicates for you
	print(language)
# A list in the dictionary
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'cheese'], 
}
# You can also put a dictionary in a dictionary


print("------------			User Input			------------")
name = input("What is your name? \n")
print("Hey " + name)

print("------------			While loop			------------")
pets = ['dog', 'cat', 'fish', 'birds', 'hamster', 'cat', 'turtle', 'cat']
while 'cat' in pets:
	pets.remove('cat')
print(pets)