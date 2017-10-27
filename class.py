class Car():
	"""A class that represent a car."""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()


	def read_odometer(self):
		print("Odometer: " + self.odometer_reading)

	def update_odometer(self, milage):
		if milage >= self.odometer_reading:
			self.odometer_reading = milage
		else:
			print("Can't roll back adometer.")

	def fill_gas(self):
		print("Gas filled!")

	def increment_odometer(self, miles):
		self.odometer_reading += mile


class ElectricCar(Car):
	"""A case for inheritance."""

	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()

	def fill_gas(self):
		"""Overriding methods from the parent class"""
		print("No gas tank!")

class Battery():
	"""Instance as attributes"""
	
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)



my_tesla = ElectricCar('Tesla', 'Model X', 2017)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas()
my_tesla.battery.describe_battery()