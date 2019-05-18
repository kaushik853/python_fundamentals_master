'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car(object):
    ''' This a class for car '''
    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def increase(self):
        self.max_speed += 5
        return self.max_speed

    def __str__(self):
        return "This is {} of car , manufactured in {} with speed of {}".format(self.model, self.year, self.max_speed)


k1_car = Car('Audi-TT', 2014, 280)
c1_car = Car('Pigeot-208', 2013, 200)
print(k1_car)
print(c1_car)
print(k1_car.model)
print(c1_car.model)
print(k1_car.max_speed)
print(c1_car.max_speed)
print(f"c1's car speed now {c1_car.increase()}")
