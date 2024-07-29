class Donor:
    def __init__(self, name, blood_type, contact):
        self.name = name
        self.blood_type = blood_type
        self.contact = contact

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def add_donor(self, donors, name, blood_type, contact):
        donors.append(Donor(name, blood_type, contact))
        print(f"Donor {name} added successfully.")

    def view_donors(self, donors):
        if not donors:
            print("No donors available.")
        else:
            for donor in donors:
                print(f"Name: {donor.name}, Blood Type: {donor.blood_type}, Contact: {donor.contact}")

    def delete_donor(self, donors, name):
        for donor in donors:
            if donor.name == name:
                donors.remove(donor)
                print(f"Donor {name} deleted successfully.")
                return
        print(f"Donor {name} not found.")

    def admin_menu(self, donors):
        while True:
            print("\n1. Add Donor")
            print("2. View Donors")
            print("3. Delete Donor")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter donor name: ")
                blood_type = input("Enter blood type: ")
                contact = input("Enter contact information: ")
                self.add_donor(donors, name, blood_type, contact)
            
            elif choice == '2':
                self.view_donors(donors)
            
            elif choice == '3':
                name = input("Enter the name of the donor to delete: ")
                self.delete_donor(donors, name)
            
            elif choice == '4':
                print("Exiting admin menu.")
                break
            
            else:
                print("Invalid choice. Please try again.")