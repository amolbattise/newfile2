from books import Books

def admin_menu(books):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            quantity = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            books.add_book(book_id, name, author, quantity, price)

        elif choice == '2':
            books.view_books()

        elif choice == '3':
            print("Logging out from Admin Panel...")
            break

        else:
            print("Invalid choice! Try again.")
