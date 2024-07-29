def view_all_donors(donors):
    if not donors:
        print("No donors available.")
    else:
        for donor in donors:
            print(f"Name: {donor.name}, Blood Type: {donor.blood_type}, Contact: {donor.contact}")

def book_donor(donors, name):
    for donor in donors:
        if donor.name == name:
            print(f"Donor {name} booked successfully.")
            return
    print(f"Donor {name} not found.")

def cancel_donor(donors, name):
    for donor in donors:
        if donor.name == name:
            print(f"Donor {name} booking canceled successfully.")
            return
    print(f"Donor {name} not found.")