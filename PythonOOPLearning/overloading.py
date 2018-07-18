class Square:
    def __init__(self, side):
        self.side = side

    def __add__(square_one, square_two): # special operator overloading method for +
        return (4 * square_one.side) + (4 * square_two.side)



square_one = Square(5)  # 5*4=20
square_two = Square(10)  # 10*4=40

print("Sum of sides of both squares: ", square_one + square_two)
