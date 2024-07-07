print('METRO TICKET BOOKING')
users = [{'username': 's', 'phno': 123456, 'password': '123'}]
stations = {1: 'stationA', 2: 'stationB', 3: 'stationC', 4: 'stationD'}

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        phno = int(input('Enter phone number: '))
        password = input("Enter password: ")

        # Check if the phone number already exists
        user_exists = False
        for user in users:
            if user['phno'] == phno:
                user_exists = True
                break

        if user_exists:
            print("Phone number already exists!")
        else:
            users.append({'username': username, 'phno': phno, 'password': password})
            print("Registration successful!")

    elif choice == 2:
        choic = str(input('Enter type (admin / passenger): ')).strip().lower()

        if choic == 'admin':
            admin_name = input('Enter username: ')
            admin_password = input('Enter password: ')
            admin1 = {'username': 'admin', 'password': 'asdf'}

            if admin_name == admin1['username'] and admin_password == admin1['password']:
                while True:
                    print('1. Add new station\n2. View stations\n3. Log out')
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
                        for station_id, station_name in stations.items():
                            print(f"{station_id}: {station_name}")
                        print()

                    elif admchoice == 3:
                        print('Logged out successfully!')
                        break

                    else:
                        print('Invalid choice')

        elif choic == 'passenger':
            phnon = int(input("Enter phone number: "))
            password = input("Enter password: ")

            # Check if the phone number and password match
            login_success = False
            for user in users:
                if user['phno'] == phnon and user['password'] == password:
                    login_success = True
                    break

            if login_success:
                while True:
                    print('1. Book Ticket\n2. Exit')
                    paschoice = int(input('Enter your choice: '))

                    if paschoice == 1:
                        for station_id, station_name in stations.items():
                            print(f"{station_id}: {station_name}")
                        print('Each station carries RS10!')

                        entry_station = int(input('Enter your entry station: '))
                        exit_station = int(input('Enter your exit station: '))
                        tickets = int(input('Number of tickets you need: '))

                        if entry_station in stations and exit_station in stations:
                            distance = abs(exit_station - entry_station)
                            price = distance * tickets * 10
                            print('Total price:', price, 'RS')
                        else:
                            print('Invalid station! Please enter a valid station number.')

                    elif paschoice == 2:
                        print('You have exited.')
                        break

                    else:
                        print('Invalid choice! Please enter 1 or 2.')

            else:
                print("Invalid phone number or password!")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        
            






    
        
            
        
    
