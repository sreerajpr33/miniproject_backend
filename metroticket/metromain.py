print('METRO TICKET BOOKING')
users = []
stations={1:'stationA',2:'stationB',3:'stationC',4:'stationD'}
while True:
    print("\n1. Register\n2. login \n3.exit")
    choice =int(input("Enter your choice: "))

    if choice == 1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        phno=int(input('enter phone number '))

        # Check if the username already exists
        user_exists = False
        for user in users:
            if user['phno'] == phno:
                user_exists = True
                break

        if user_exists:
            print("phone number already exists!")
        else:
            users.append({'username': username, 'password': password,'phno':phno})
            print("Registration successful!")

    elif choice == 2:
        choic=str(input('enter type(admin / passenger) :')).strip().lower()

        if choic=='admin':
            print()
            admin_name=input('enter user_name :')
            admin_password=input('enter the password')
            admin1=[{'usrname':'admin','passwrd':'asdf'}]
            print()

            for i in admin1:
                if admin_name == i['usrname'] and admin_password == i['passwrd']:
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
                            print()
                            for station_id, station_name in stations.items():
                                print(f"{station_id}: {station_name}")
                                print()

                        elif admchoice == 3:
                            print('Log out successfully!')
                            break

                        else:
                            print('Invalid choice')

        elif choice=='passenger':
            phnon = int(input("Enter phone number : "))
            password = input("Enter password: ")

                    # Check if the username and password match
            login_success = False
            for user in users:
                if user['phno'] == phnon and user['password'] == password:
                    login_success = True
                    break

                if login_success:
                    print("Login successful!")
                else:
                    print("Invalid username or password!")

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")