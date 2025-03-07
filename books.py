import pickle
import os

class Books:
    def __init__(self):
        self.books = {}
        self.load_books()

    def save_books(self):
        os.makedirs("data", exist_ok=True)  
        with open("data/books_data.pkl", "wb") as file:
            pickle.dump(self.books, file)

    def load_books(self):
        try:
            with open("data/books_data.pkl", "rb") as file:
                self.books = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.books = {}

    def add_book(self, book_id, name, author, quantity, price):
        if book_id in self.books:
            print(f"Book ID '{book_id}' already exists! Use update option instead.")
        else:
            self.books[book_id] = {'name': name, 'author': author, 'quantity': quantity, 'price': price}
            self.save_books()
            print(f"Book '{name}' by {author} added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\nAvailable Books:")
            print("ID\tName\tAuthor\tQuantity\tPrice")
            print("-" * 50)
            for book_id, details in self.books.items():
                print(f"{book_id}\t{details['name']}\t{details['author']}\t{details['quantity']}\t{details['price']}")

    def borrow_book(self, book_id):
        if book_id in self.books and self.books[book_id]['quantity'] > 0:
            self.books[book_id]['quantity'] -= 1
            self.save_books()
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id]['quantity'] += 1
            self.save_books()
            return True
        return False
