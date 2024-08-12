
from acc1 import *
accounts = []

while True:
    print("1. Create account\n2. Login to account\n3. Exit")
    choice = int(input('Enter your choice: '))

    if choice == 1:
        acc()

    elif choice == 2:
        log()

    elif choice == 3:
        print('Exiting...!')
        break

    else:
        print('Invalid choice....!')