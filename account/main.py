import random
import hashlib
import os

accounts = []

while True:
    print("1. Create account\n2. Login to account\n3. Exit")
    choice = int(input('Enter your choice: '))

    if choice == 1:
        name = input('Enter your name: ')
        pin = input('Enter your pin: ')
        balance = 0

        
        pin_bytes = pin.encode()
        hashed_pin = hashlib.sha256(pin_bytes).hexdigest()

        
        account_number = random.randint(100000, 999999)

        while any(account["accountnumber"] == account_number for account in accounts):
            account_number = random.randint(100000, 999999)

        account = {"accountnumber": account_number, "name": name, "balance": balance, "password": hashed_pin}

        accounts.append(account)

        with open(f"miniproject_backend/account/{account_number}.txt", 'w') as f:
            f.write(str(account))

        print(f"Your account has been created. Account number: {account_number}")

    elif choice == 2:
        account_number = input('Enter your account number: ')
        file_path = f"miniproject_backend/account/{account_number}.txt"

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                account_data = f.read()
                account = eval(account_data)  # Convert the string back to a dictionary

            pin = input('Enter your pin: ')
            pin_bytes = pin.encode()
            hashed_pin = hashlib.sha256(pin_bytes).hexdigest()

            if hashed_pin == account['password']:
                print("Login successful!")
                print(f"Welcome {account['name']}")
                print("1. Deposit\n2. Withdraw")
                ch = int(input('Enter your choice: '))

                if ch == 1:  # Deposit
                    amount = int(input('Enter the deposit amount: '))
                    account['balance'] += amount
                    print(f"${amount} deposited successfully. New balance: ${account['balance']}")
                    
                    with open(file_path, 'w') as f:
                        f.write(str(account))

                elif ch == 2:  # Withdraw
                    amount = int(input('Enter the withdrawal amount: '))
                    if amount <= account['balance']:
                        account['balance'] -= amount
                        print(f"${amount} withdrawn successfully. New balance: ${account['balance']}")
                        
                        with open(file_path, 'w') as f:
                            f.write(str(account))
                    else:
                        print("Insufficient balance.")
            else:
                print("Incorrect password.")
        else:
            print("Account not found.")

    elif choice == 3:
        print('Exiting...!')
        break

    else:
        print('Invalid choice....!')