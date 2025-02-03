class Book:
    def __init__(self, title, author, year):
        """Constructor to initialize the book instance."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor to print a message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Returns a user-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Returns an official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage:
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    print(book1)       # Output: 1984 by George Orwell, published in 1949
    print(repr(book1)) # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book instance
    del book1
