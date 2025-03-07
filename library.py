import pickle

class Library:
    def __init__(self):
        self.books = {}  
        self.users = {}
        self.load_data()

    def save_data(self):
        with open("data/library_data.pkl", "wb") as file:
            pickle.dump({'users': self.users}, file)

    def load_data(self):
        try:
            with open("data/library_data.pkl", "rb") as file:
                data = pickle.load(file)
                self.users = data.get('users', {})
        except FileNotFoundError:
            pass

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists! Try another.")
        else:
            self.users[username] = password
            self.save_data()
            print("User registered successfully! You can now log in.")

    def login_user(self, username, password):
        if username in self.users and self.users[username] == password:
            print(f"Welcome, {username}!")
            return True
        else:
            print("Invalid username or password!")
            return False
