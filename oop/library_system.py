class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        # Initialize the base class (Book) attributes
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        # Return the string representation of the EBook
        return f"{super().__str__()}, File Size: {self.file_size}MB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Initialize the base class (Book) attributes
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        # Return the string representation of the PrintBook
        return f"{super().__str__()}, Pages: {self.page_count}"


class Library:
    def __init__(self):
        # Initialize an empty list to store books in the library
        self.books = []

    def add_book(self, book):
        # Add a book to the library collection (can be a Book, EBook, or PrintBook)
        self.books.append(book)

    def list_books(self):
        # List all books in the library
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
