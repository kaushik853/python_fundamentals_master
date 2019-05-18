'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the + operator in one of the classes
    so that it adds two attributes of that class.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''
class Vehicle(object):
    vehicle_transmission = 'manual'
    country_of_registration = 'DE'
    def __init__(self, model='rickshaw', emission='petrol', wheels=2):
        self.model = model
        self.emission = emission
        self.wheels = wheels
    def __str__(self):
        return "This class is for vehicle object"
    def vehicle_print(self):
        return "This class talks about vehicle {} and the {} emission and also about {} wheels".format(self.model, self.emission, self.wheels)
    def __add__(self, other):
        return self.wheels + other.wheels

car = Vehicle('Audi', 'diesel', 4)
print(car.model)
print(car.vehicle_print())
#print(car.__add__())

truck = Vehicle('Man', 'diesel', 16)
print(car + truck)


class inhabitant(object):
    living = True
    source_of_life = 'oxygen'
    def __init__(self, planet='earth', species='alien', arm=4 ):
        self.planet = planet
        self.species = species
        self.arm = arm

    def __str__(self):
        return " This class is about creatures of this universe"

    def inhab_print(self):
        return "This inhabitants are from planet {} of species as {} with {} arms".format(self.planet, self.species, self.arm)

human = inhabitant('earth', 'homospaiens', )
print(human.inhab_print())
print(human)
dead_rat = inhabitant('nebula', 'raton', 8)
dead_rat.source_of_life = 'co2'
print(dead_rat.source_of_life)
