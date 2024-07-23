from reg import*  # Assuming users is a list of dictionaries with user data
def login():
    up = {123: [[1, 's', 2, 'd', 'e']],
            223:[[2,'d',1,'f','s']]}
    uphone = int(input('ENTER YOUR PHONE NUMBER: '))
    password = input('ENTER YOUR PASSWORD: ')
    f = 0
    def others(up, s_key):
        for key, values in up.items():
            if key == s_key:
                continue
            print()
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("User Phone", "Pet ID", "Pet Name", "Age", "Type", "Place"))
            print('_' * 85)
            for pet in values:
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(key, pet[0], pet[1], pet[2], pet[3], pet[4]))
            print()

    for i in users:
        if i['phone'] == uphone and i['password'] == password:
            f = 1
            print('LOGIN SUCCESSFUL!')
            while True:
                print('1. Add pets\n2. View added pets\n3. Delete added pets\n4. Adopt\n5. Exit')
                ch = int(input('ENTER YOUR CHOICE: '))
                if ch == 1:
                    p_name = input('ENTER PET NAME: ')
                    p_age = int(input('HOW OLD IS YOUR PET: '))
                    p_type = input('ENTER THE TYPE: ')
                    p_place = input('PLACE: ')

                    if uphone not in up:
                        up[uphone] = []

                    user_pets = up[uphone]
                    pet_id = len(user_pets) + 1
                    user_pets.append([pet_id, p_name, p_age, p_type, p_place])
                    up[uphone] = user_pets
                    print('PET ADDED!')
                    print(up)
                elif ch == 2:
                    if uphone in up:
                        for pet in up[uphone]:
                            print(pet)
                    else:
                        print('No pets added yet.')
                elif ch == 3:
                    if uphone in up:
                        pet_delet = int(input('Enter the pet ID to delete: '))
                        user_pets = up[uphone]
                        up[uphone] = [pet for pet in user_pets if pet[0] != pet_delet]
                        print('PET DELETED!')
                elif ch == 4:
                    others(up, uphone)
                    adoptpet_id = int(input('Enter the ID of the pet you want to adopt: '))
                    pet_found = False
                    for owner_phone, pets in up.items():
                        if owner_phone == uphone:
                            continue
                        for pet in pets:
                            if pet[0] == adoptpet_id:
                                pet_found = True
                                print('Adoption successful!')
                                if uphone not in up:
                                    up[uphone] = []
                                up[uphone].append(pet)
                                pets.remove(pet)
                                if not pets:
                                    del up[owner_phone]
                                break
                        if pet_found:
                            break
                    if not pet_found:
                        print('Invalid pet ID.')  
                elif ch==5: 
                    print('exiting!')
                    break
                else:
                    print('INVALID CHOICE!' )
        else:
            print('INVALID PHONENUMBER OR PASSWORD!')