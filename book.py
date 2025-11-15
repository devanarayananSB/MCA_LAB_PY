class Publisher:
    def __init__(self, name):
        self.name = name
class Book(Publisher):
    def __init__(self, publisher, title, author, pages):
        super().__init__(publisher)
        self.title = title
        self.author = author
        self.pages = pages
    def show(self):
        print("Publisher:", self.name)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Pages:", self.pages)
b = Book("Pearson", "Python Basics", "Devanarayanan", 180)
b.show()
