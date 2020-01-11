import functools
import operator
# import geocoder

numbers = [1,2,3,4,5,6]

print(functools.reduce(lambda a,b: a + b, numbers))
print(map(lambda x: x + x, numbers))
print(functools.reduce(operator.mul, numbers))

class B:
    kind  = 'Herbivore'

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour