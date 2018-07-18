from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        return 0


class Square(Shape):
    side = 4

    def area(self):
        print("Area of Square: ", self.side * self.side)


class Rectangle(Shape):
    length = 10
    width = 5

    def area(self):
        print("Area of Rectangle: ", self.length * self.width)


square = Square()
rectangle = Rectangle()

square.area()
rectangle.area()
# shape = Shape() # Can't instantiate abstract class Shape with abstract methods area
