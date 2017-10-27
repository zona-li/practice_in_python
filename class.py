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


	def increment_odometer(self, miles):
		self.odometer_reading += mile


class ElectricCar(Car):
	"""A case for inheritance."""

	def __init__(self, make, model, year):
		super().__init__(make, model, year)


my_tesla = ElectricCar('Tesla', 'Model X', 2017)
print(my_tesla.get_descriptive_name())