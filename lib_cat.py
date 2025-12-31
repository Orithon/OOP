#Library Catalog
"""
Project Idea: Build a library catalog system where users can add books,
search for books by title or author, and check book availability. Each book can be an object.
Why It’s Great for Beginners: This project teaches you about object composition.
You can create a Book class and use it as part of a larger Library class.
"""

class Book:

    def __init__(self,title,author, available= True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:

    def __init__(self):
        self.books = []

    def add_book(self,title,author,available):
        self.books.append(Book(title,author,available))
        print(f"{title} added to Library")

    def view_books(self):
        if not self.books:
            print("Library is empty.")
            return

        for book in self.books:
            status = "Available" if book.available else "Not available"
            print(f"{book.title} by {book.author} - {status}")

    def search_book(self,title):
        return next(
            (b for b in self.books if b.title.lower() == title.lower()),
            None
        )

    def check_availability(self, title):
        book = self.search_book(title)

        if book:
            return "Available" if book.available else "Not available"
        else:
            return "Book not found"


def main():
    library = Library()

    while True:
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Check Availability of Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter the book's author: ")
            available_input = input("Enter the availability status (true/false): ").lower()
            available = available_input== "true"
            library.add_book(title, author, available)

        elif choice == 2:
            library.view_books()

        elif choice == 3:
            title = input("Enter the title of the book: ")
            book = library.search_book(title)

            if book:
                print(f"{book.title} by {book.author}")
            else:
                print("Book not found")

        elif choice == 4:
            title = input("Enter the title of the book: ")
            status = library.check_availability(title)
            print(status)

        elif choice == 5:
            print("Thank you for using this program.")
            break

        else:
            print("Invalid choice.")

main()