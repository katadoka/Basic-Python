# Write a program in the OOP style to emulate the work of the plant. The program will have two classes: for machines and for the plant. 
# Machines have: name, price and information or collected. The plant keeps a list of machines. The plant keeps a list of machines. 
# The plant provides information on how much cars are now in it and how many of them are collected. Also display information on all machines.

class PriceException(Exception):
	pass


class Car:
	
	def __init__(self, condition):
		self.condition = condition

	@property 	
	def info_car(self):
		return'{} - {}'.format(self.price, self.condition)

	def description(self):
		print('{} - {}'.format(self.brand, self.info_car))

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, amount):
		if amount > 15000:
			raise PriceException('Price should be < 15000$')
		elif amount < 0:
			raise PriceException('Price should be > 0')
		else:
			self._price = amount

	@property
	def conditions(self):
		return self.condition 

	@conditions.setter
	def conditions(self, condition):
		if not isinstance(condition, bool):  # перевірка чи являється 1 елемент до другого і можна використовувати дочірні класи
			raise Exception('Condition should be True or false!!!')

	def __enter__(self):
		if self.condition == False:
			self.condition == True
		else:
			raise Exception('This car is collected!!')
		return self

	def __exit__(self, *args):
		return


class BMV(Car):
	brand = 'BMV'
	_price = '15000$'


class Mersedes(Car):
	brand = 'Mersedes'
	_price = '12000$'


class Lanos(Car):
	brand = 'Lanos'
	_price = '3000$'


class Plant:
	counter = 0 
	def __init__(self):
		self.cars = []

	def add_car(self, car):
		if len(self.cars) == 3:
				print('The plant is full!')
		else:
			self.cars.append(car)
			Plant.counter += 1

	def del_car(self, car):
		self.cars.remove(car)
		Plant.counter -= 1

	def assamble(self, car):
		car.condition = True

	def show_info_car(self):
		dont_work = 0
		for car in self.cars:	
			if car.condition != True:
				dont_work += 1
			car.description()
		print('Total cars: {}'.format(Plant.counter))
		print('On plant: {}/{}'.format(dont_work, len(self.cars)))	


c = BMV(True)
c1 = Mersedes(False)
c2 = Lanos(False)
c3 = BMV(True)

with c1:
	print('Car is collected.')

with c:
	print('Car is collected.')

# c1.conditions = True
# c1.description()
# c2.conditions = "True2321"
# c2.description()

# c.price = 14000
# c.description()
# c.price = 4000
# c.description()
# c1.price = -100
# c1.description()

# plant = Plant()
# plant.add_car(c)
# plant.add_car(c1)
# plant.add_car(c2)
# plant.del_car(c1)
# plant.show_info_car()

# plant1 = Plant()
# plant1.add_car(c)
# plant1.add_car(c1)
# plant1.assamble(c1)
# plant1.add_car(c2)
# plant1.show_info_car()

# plant2 = Plant()
# plant2.add_car(c)
# plant2.add_car(c1)
# plant2.add_car(c2)
# plant2.add_car(c3)
# plant2.show_info_car()
