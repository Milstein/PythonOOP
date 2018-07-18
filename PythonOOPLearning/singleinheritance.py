class Apple:  # Base Class
    manufacture = 'Apple Inc.'
    website = 'http://www.apple.com'

    def contact_detail(self):
        print("To contact us, log on to ", self.website)


class MacBook(Apple):  # Derived Class
    def __init__(self):
        self.year_of_manufacture = 2017

    def manufacture_detail(self):
        print("This MacBook was manufactured in the year {} by {}".format(self.year_of_manufacture, self.manufacture))


mac_book = MacBook()
mac_book.manufacture_detail()
mac_book.contact_detail()
