class Book:
    def __init__(self, title, author):
        """Initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with additional file_size attribute."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} (EBook - {self.file_size}MB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with additional page_count attribute."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} (PrintBook - {self.page_count} pages)"

class Library:
    def __init__(self):
        """Initialize the library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            print(book)
