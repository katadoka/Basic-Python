# Use the program from the previous lesson as a basis. Add the following features:
# - add different classes of machines. The name does not need to be transmitted, it is given in the class itself.
# - add the maximum number of machines at the factory.
# - add function "assamble", which will accept the car as a parameter and collect it.

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

