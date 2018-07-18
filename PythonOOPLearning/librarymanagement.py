# Class => Library
# layers of abstraction => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book

class Library(object):

    def __init__(self, available_books):
        self.available_books = available_books

    def display_available_books(self):
        print()
        print("Available Books: ")
        for book in self.available_books:
            print(book)
        print()

    def lend_book(self, requested_book):
        if requested_book in self.available_books:
            print("You have now borrowed the book")
            self.available_books.remove(requested_book)
        else:
            print("Sorry! the book is not available in our list.")

    def add_book(self, returned_book):
        self.available_books.append(returned_book)
        print("You have returned the book. Thank you!!")


class Customer(object):
    def request_book(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def return_book(self):
        print()
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book


library = Library(['Think and Grow Rich', 'Who Will Cry When You Die', 'For One More Day'])
customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    user_choice = int(input())

    if user_choice is 1:
        library.display_available_books()
    elif user_choice is 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice is 3:
        returned_book = customer.request_book()
        library.add_book(returned_book)
    elif user_choice is 4:
        quit()
    else:
        quit()
