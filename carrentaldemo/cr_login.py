from cr_reg import*
car=[{'car_plate':'so1','car_name':'bmw','capacity':'2','price':'6000RS'},
    {'car_plate':'so2','car_name':'porsche','capacity':'2','price':'8000RS'}]
def login():
    email=input('enter your email :')
    password=input('enter your password :')
    if email=='admin123' and password=='1234':
        print('LOGIN SUCESSFULL!')
        while True:
            print('1.add car\n2.remove car\n3.view car\n4.view user details\n5.view carbookings\n6.price calculator')
            adch=int(input('enter your choice :'))
            if adch==1:
                print()
                a_cplate=input('enter the regestration number of car :')
                a_cname=input('enter the cars name :')
                a_cseat=int(input('enter the seat capacity :'))
                a_cprice=input('enter the price (per100km) :')
                print()

                car_exist = False
                for cars in car:
                    if cars['car_plate'] == a_cplate:
                        car_exist = True
                        break
                if car_exist:
                    print('REGISTRATION NUMBER OF THE CAR ALREADY EXISTS!')
                else:
                    car.append({'car_plate': a_cplate, 'car_name': a_cname, 'capacity': a_cseat, 'price': a_cprice}) 
                    print('CAR ADDED SUCCESSFULLY!')
            elif adch==2:
                print()
                a_cplate=input('enter the registration number of car you want to remove :')
                a_cname=input('enter the car name want to remove :')
                f=0
                for cars in car:
                    if cars['car_plate']==a_cplate and cars['car_name']==a_cname:
                        car.remove(cars)
                        f=1
                        print('CAR REMOVED SUCESSFULLY!')
                if f==0:
                    print('CAR NOT FOUND!')
            elif adch==3:
                print()
                # Print the header
                print("{:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price"))
                print('_' * 60)

                # Print each car's details
                for i in car:
                    print("{:<15} {:<15} {:<15} {:<15}".format(i['car_plate'], i['car_name'], i['capacity'], i['price']))
                print()
            elif adch==4:
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format('name','email','address','phone','password'))
                print('_' * 60)
                for i in user:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(i['username'], i['useremail'], i['useraddress'], i['userphone'],i['userpassword']))
                print()
    else:
        user_exist = False
        for users in user:
            if users['useremail'] == email and users['userpassword'] == password:
                user_exist = True
                break

        if user_exist:
            print('LOGIN SUCCESSFUL!')
            #viewcar,booking,cancelbookig
        else:
            print('LOGIN FAILED!')
 
        