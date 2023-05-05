cat_enmus = ("Politics", "History", "Tourism", "Science")

class Book:
    def __init__(self, title, author, cat, price, pages) -> None:
        self.title = title
        self.author = author
        self.cat = cat_enmus[cat]
        self.pages = pages
        self.price = price

    def __str__(self) -> str:
        return f"Book {self.title} {self.author} {cat_enmus[self.cat]} price:{self.price} pages:{self.pages}"

class Reader:
    def __init__(self, full_name) -> None:
        self.full_name = full_name
        self.read_books = dict()
        self.purchased_books = []
        self.intereseed_books = []

    def add_read_book(self, book):
        self.read_books[book.title] = self.read_books.get(book.title, 0) +1

    def add_purchased_book(self, book):
        if book not in self.purchased_books:
            self.purchased_books.append(book)
        else:
            raise ValueError("book is already purchased")
        
    def add_intereseed_book(self, book):
        if book not in self.intereseed_books:
            self.intereseed_books.append(book)
        else:
            raise ValueError("book is already in the list")
             
    def list_read_book(self):
        print(self.read_books)

    def book_consumption(self):
        sum = 0
        for book in self.purchased_books:
            sum += book.price
        return sum

book1 = Book("book1", "me", 0, 100, 150)
book2 = Book("book2", "you", 0, 200, 200)

majdy = Reader("majdydaood")

majdy.add_read_book(book1)
majdy.list_read_book()
majdy.add_read_book(book1)
majdy.list_read_book()
majdy.add_read_book(book2)
majdy.list_read_book()

majdy.add_purchased_book(book1)
majdy.add_purchased_book(book2)

total = majdy.book_consumption()
print(total)


