# Public => memberName
# Protected => _memeberName
# Private => __memberName


class Car:
    no_of_wheels = 4
    _color = 'Black'
    __year_of_manufacture = 2019  # _car__year_of_manufacture

    def __init__(self):
        self.__year_of_manufacture = 2018

class BMW(Car):
    def __init__(self):
        print("Protected attribute _color: ", self._color)

car = Car()
print("Public attribute no_of_wheels: ", car.no_of_wheels)
print("Protected attribute year_of_manufacture ", _Car__year_of_manufacture)

bmw = BMW()
