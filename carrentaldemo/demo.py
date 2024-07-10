from cr_login import*
print('1.view cars\n2.booking\n3.cancel booking :')
uch=int(input('enter your choice :'))
if uch==1:
    print()
                # Print the header
    print("{:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price"))
    print('_' * 60)

                # Print each car's details
    for i in car:
        print("{:<15} {:<15} {:<15} {:<15}".format(i['car_plate'], i['car_name'], i['capacity'], i['price']))
        print()


