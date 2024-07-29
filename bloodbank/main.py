from admin import Admin, Donor
import donor_management as dm
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginSystem:
    def __init__(self):
        self.users = {}
        self.admins = {"admin": Admin("admin", "admin123")}
        self.donors = []

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            self.users[username] = User(username, password)
            print(f"User {username} registered successfully.")

    def login(self, username, password, user_type):
        if user_type == "admin":
            if username in self.admins and self.admins[username].password == password:
                print(f"Welcome, Admin {username}!")
                self.admins[username].admin_menu(self.donors)
            else:
                print("Invalid admin username or password.")
        elif user_type == "user":
            if username in self.users and self.users[username].password == password:
                print(f"Welcome, {username}!")
                self.user_menu()
            else:
                print("Invalid username or password.")
        else:
            print("Invalid user type.")

    def user_menu(self):
        while True:
            print("\n1. View All Donors")
            print("2. Book Donor")
            print("3. Cancel Donor")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                dm.view_all_donors(self.donors)
            
            elif choice == '2':
                name = input("Enter the name of the donor to book: ")
                dm.book_donor(self.donors, name)
            
            elif choice == '3':
                name = input("Enter the name of the donor to cancel booking: ")
                dm.cancel_donor(self.donors, name)
            
            elif choice == '4':
                print("Exiting user menu.")
                break
            
            else:
                print("Invalid choice. Please try again.")

def main():
    system = LoginSystem()
    
    while True:
        print("\n1. Register User")
        print("\n2. User Login")
        print("\n3. Admin Login")
        print("\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.register_user(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            system.login(username, password, "user")
        
        elif choice == '3':
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")
            system.login(username, password, "admin")
        
        elif choice == '4':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()