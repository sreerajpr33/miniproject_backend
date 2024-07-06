print('METRO TICKET BOOKING')
users = []
stations = {1: 'stationA', 2: 'stationB', 3: 'stationC', 4: 'stationD'}

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        phno = int(input('Enter phone number: '))

        # Check if the phone number already exists
        user_exists = False
        for user in users:
            if user['phno'] == phno:
                user_exists = True
                break

        if user_exists:
            print("Phone number already exists!")
        else:
            users.append({'username': username, 'password': password, 'phno': phno})
            print("Registration successful!")

    elif choice == 2:
        choic = input('Enter type (admin / passenger): ').strip().lower()

        if choic == 'admin':
            admin_name = input('Enter username: ')
            admin_password = input('Enter password: ')
            predefined_admin = {'usrname': 'admin', 'passwrd': 'asdf'}
            
            if admin_name == predefined_admin['usrname'] and admin_password == predefined_admin['passwrd']:
                while True:
                    print('1. Add new station\n2. Exit')
                    admchoice = int(input('Enter your choice: '))
                    if admchoice == 1:
                        new_station_name = input('Enter new station name: ')
                        new_station_id = max(stations.keys()) + 1
                        if new_station_name not in stations.values():
                            stations[new_station_id] = new_station_name
                            print('Station added successfully!')
                        else:
                            print('Station already exists!')
                    elif admchoice == 2:
                        print('Log out successfully!')
                        break
                    else:
                        print('Invalid choice')
            else:
                print('Invalid admin credentials!')

        elif choic == 'passenger':
            phno = int(input("Enter phone number: "))
            password = input("Enter password: ")

            # Check if the phone number and password match
            login_success = False
            for user in users:
                if user['phno'] == phno and user['password'] == password:
                    login_success = True
                    break

            if login_success:
                print("Login successful!")
            else:
                print("Invalid phone number or password!")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")