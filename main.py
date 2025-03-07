from library import Library
from books import Books
from admin import admin_menu
from user import user_menu

def main():
    library = Library()
    books = Books()

    while True:
        print("\nLibrary Management System")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Register User")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            password = input("Enter Admin Password: ")
            if password == "admin123":
                admin_menu(books)
            else:
                print("Incorrect password!")

        elif choice == '2':
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if library.login_user(username, password):
                user_menu(library, books, username)

        elif choice == '3':
            username = input("Enter new Username: ")
            password = input("Enter new Password: ")
            library.register_user(username, password)

        elif choice == '4':
            print("Exiting system...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
