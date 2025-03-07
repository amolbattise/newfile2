def user_menu(library, books, username):
    while True:
        print("\nUser Menu:")
        print("1. View Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            books.view_books()

        elif choice == '2':
            book_id = input("Enter Book ID to borrow: ")
            if books.borrow_book(book_id):
                print(f"{username} borrowed the book successfully!")
            else:
                print("Book not available!")

        elif choice == '3':
            book_id = input("Enter Book ID to return: ")
            if books.return_book(book_id):
                print(f"{username} returned the book successfully!")
            else:
                print("Invalid Book ID!")

        elif choice == '4':
            print("Logging out from User Menu...")
            break

        else:
            print("Invalid choice! Try again.")
