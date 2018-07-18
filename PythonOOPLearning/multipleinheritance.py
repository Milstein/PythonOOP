class OperatingSystem:  # Base Class
    multitasking = True
    name = 'MAC OS'


class Apple:  # Base Class
    website = 'http://www.apple.com'
    name = 'Apple'


class MacBook(OperatingSystem, Apple):  # Derived Class
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for more detail".format(self.website))
            print('Name: ', self.name) # the order of inheritance in derived class will determine this conflicting
            # name's value First declared base class has high precedence

mac_book = MacBook()
