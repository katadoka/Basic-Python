# Write a program in the OOP style to emulate the work of the plant. The program will have two classes: for machines and for the plant. 
# Machines have: name, price and information or collected. The plant keeps a list of machines. The plant keeps a list of machines. 
# The plant provides information on how much cars are now in it and how many of them are collected. Also display information on all machines.

class Car:
	
	brand = None

	def __init__(self, price, condition):
		self.price = price
		self.condition = condition

	@property 	
	def info_car(self):
		return('{} - {}'.format(self.price, self.condition))

	def description(self):
		print('{} - {}'.format(self.brand, self.info_car))


class BMV(Car):
	brand = 'BMV'


class Mersedes(Car):
	brand = 'Mersedes'


class Lanos(Car):
	brand = 'Lanos'


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


c = BMV('15000$', True)
c1 = Mersedes('12000$', False)
c2 = Lanos('3000$', False)
c3 = BMV('17000', True)

plant = Plant()
plant.add_car(c)
plant.add_car(c1)
plant.add_car(c2)
plant.del_car(c1)
plant.show_info_car()

plant1 = Plant()
plant1.add_car(c)
plant1.add_car(c1)
plant1.assamble(c1)
plant1.add_car(c2)
plant1.show_info_car()

plant2 = Plant()
plant2.add_car(c)
plant2.add_car(c1)
plant2.add_car(c2)
plant2.add_car(c3)
plant2.show_info_car()

