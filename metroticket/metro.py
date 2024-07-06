print('METRO TICKET BOOKING')
users = []
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

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
        
            






    
        
            
        
    
