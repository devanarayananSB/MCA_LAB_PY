class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
    def __init__(self, publisher, title, author,price, pages):
        super().__init__(publisher)
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages
    def show(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)
b = Book("Pearson", "Python Basics", "Devanarayanan",2500, 180)
b.show()
