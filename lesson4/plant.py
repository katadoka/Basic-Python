# Write a program in the OOP style to emulate the work of the plant.
# The program will have two classes: for machines and for the plant.
# Machines have: name, price and information or collected.
# The plant keeps a list of machines. The plant keeps a list of machines.
# The plant provides information on how much cars are now in it
# and how many of them are collected. Also display information on all machines.


class Car:
    def __init__(self, name, price, condition):
        self.name = name
        self.price = price
        self.condition = condition

    def info_car(self):
        print('{}: {} - {}'.format(self.name, self.price, self.condition))


class Plant:
    counter = 0

    def __init__(self):
        self.cars = []
        self.counter = 0
        self.dont_work = 0

    def add_car(self, car):
        self.cars.append(car)
        self.counter += 1
        Plant.counter += 1

    def del_car(self, car):
        self.cars.remove(car)
        self.counter -= 1
        Plant.counter -= 1

    def show_info_car(self):
        print('The total  cars of plant: {}'.format(self.counter))
        print('The total cars of plants: {}'.format(Plant.counter))
        for car in self.cars:
            car.info_car()
            if car.condition != 'work':
                self.dont_work += 1
        print('The total cars of plant is dont work:{}'.format(self.dont_work))

c = Car('BMV', '15000$', 'work')
c1 = Car('Mersedes', '12000$', 'dont work')
c2 = Car('Lanos', '3000$', 'dont work')


plant = Plant()
plant.add_car(c)
plant.add_car(c1)
plant.add_car(c2)
plant.del_car(c1)
plant.show_info_car()

plant1 = Plant()
plant1.add_car(c)
plant1.add_car(c1)
plant1.add_car(c2)
plant1.show_info_car()
