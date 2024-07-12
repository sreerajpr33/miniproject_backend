# from cr_reg import*

# car=[{'car_plate':'so1','car_name':'bmw','capacity':'2','price':'6000RS','category':'lexuary'},
#     {'car_plate':'so2','car_name':'porsche','capacity':'2','price':'8000RS','category':'sports'}]
# categry=['hatchback,sedan,suv,muv, coupe, convertible,pickup']
# def login():
#     email=input('enter your email :')
#     password=input('enter your password :')
#     if email=='admin123' and password=='1234':
#         print('LOGIN SUCESSFULL!')
#         while True:
#             print()
#             print('1.add car\n2.remove car\n3.view car\n4.view user details\n5.category\n6.view carbookings\n6.price calculator')
#             adch=int(input('enter your choice :'))
#             print()
#             if adch==1:
#                 print()
#                 a_cplate=input('enter the regestration number of car :')
#                 a_cname=input('enter the cars name :')
#                 a_cseat=int(input('enter the seat capacity :'))
#                 a_cprice=input('enter the price (per100km) :')
#                 a_ccategory=input('enter the catogary of car :')
#                 print()

#                 car_exist = False
#                 for cars in car:
#                     if cars['car_plate'] == a_cplate:
#                         car_exist = True
#                         break
#                 if car_exist:
#                     print('REGISTRATION NUMBER OF THE CAR ALREADY EXISTS!')
#                 else:
#                     car.append({'car_plate': a_cplate, 'car_name': a_cname, 'capacity': a_cseat, 'price': a_cprice,'category':a_ccategory}) 
#                     print('CAR ADDED SUCCESSFULLY!')
#             elif adch==2:
#                 print()
#                 a_cplate=input('enter the registration number of car you want to remove :')
#                 a_cname=input('enter the car name want to remove :')
#                 f=0
#                 for cars in car:
#                     if cars['car_plate']==a_cplate and cars['car_name']==a_cname:
#                         car.remove(cars)
#                         f=1
#                         print('CAR REMOVED SUCESSFULLY!')
#                 if f==0:
#                     print('CAR NOT FOUND!')
#             elif adch==3:
#                 print()
#                 # Print the header
#                 print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price","category"))
#                 print('_' * 75)

#                 # Print each car's details
#                 for i in car:
#                     print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(i['car_plate'], i['car_name'], i['capacity'], i['price'],i['category']))
#                 print()
#             elif adch==4:
#                 print("{:<15} {:<15} {:<15} {:<15} {:<15}".format('name','email','address','phone','password'))
#                 print('_' * 60)
#                 for i in user:
#                     print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(i['username'], i['useremail'], i['useraddress'], i['userphone'],i['userpassword']))
#                 print()
#             elif adch==5:
#                 while True:
#                     print()
#                     print('1.view category\n2.add category\n3.delete category\n4.exit')
#                     choic=int(input('enter your choice:')) 
#                     print()                 
#                     if choic == 1:
#                         for i in categry:
#                             print(i)

#                     elif choic == 2:
#                         n_category = input('Enter new category: ').strip().lower()
#                         if n_category in categry:
#                             print('CATEGORY ALREADY EXISTS!')
#                         else:
#                             categry.append(n_category)
#                             print(f'Category "{n_category}" added successfully!')

#                     elif choic == 3:
#                         d_category = input('Enter category to delete: ')
#                         if d_category in categry:
#                             categry.remove(d_category)
#                             print(f'Category "{d_category}" deleted successfully!')
#                         else:
#                             print('CATEGORY NOT FOUND!')
#                     elif choic==4:
#                         break
#                     else:
#                         print('INVALID CHOICE!')
#                 #view carbookings,price calculator
#     else:
#         user_exist = False
#         for users in user:
#             if users['useremail'] == email and users['userpassword'] == password:
#                 user_exist = True
#                 break

#         if user_exist:             
#             print('LOGIN SUCCESSFUL!')
#             print('1.booking\n2.view bookings\n3.cancel booking :')
#             uch=int(input('enter your choice :'))
#             if uch==1:
#                 print()
#                             # Print the header
#                 print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price","category"))
#                 print('_' * 60)

#                             # Print each car's details
#                 for i in car:
#                     print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(i['car_plate'], i['car_name'], i['capacity'], i['price'],i['category']))

#                         #search bar,booking,cancelbookig
#                 cc_search=input('enter the category of car you need :').strip().lower()
#                 found = False
#                 for i in car:
#                     if cc_search == i['category']:
#                         print()
#                         print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(i['car_plate'], i['car_name'], i['capacity'], i['price'],i['category']))
#                         print()
#                         found = True
#                         from datetime import datetime
#                         bookings={}
#                         while True:
#                             def get_user_input():
#                                 b_car = input('Enter the registration number of the car you need: ')
#                                 b_days = input('Enter the booking date (YYYY-MM-DD): ')
#                                 return b_car, b_days

#                             def validate_date(b_days):
#                                 try:
#                                     return datetime.strptime(b_days, '%Y-%m-%d').date()
#                                 except ValueError:
#                                     print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
#                                     exit()

#                             def check_car_exists(b_car, cars):
#                                 return any(car['car_plate'] == b_car for car in cars)

#                             def check_booking_exists(b_car, booking_date, bookings):
#                                 return b_car in bookings and booking_date in bookings[b_car]

#                             def add_booking(b_car, booking_date, bookings):
#                                 if b_car not in bookings:
#                                     bookings[b_car] = []
#                                 bookings[b_car].append(booking_date)
#                                 print(f'Car {b_car} booked successfully for {booking_date}.')

#                             def main():
#                                 b_car, b_days = get_user_input()
#                                 booking_date = validate_date(b_days)
                                
#                                 if not check_car_exists(b_car, cars):
#                                     print('Car not found.')
#                                     return
                                
#                                 if check_booking_exists(b_car, booking_date, bookings):
#                                     print('Car is already booked on this date.')
#                                 else:
#                                     add_booking(b_car, booking_date, bookings)
                                
#                                 print('Current bookings:', bookings)

#                             if __name__ == "__main__":
#                                 main()

                            

                        
#                 if not found:
#                     print('NO CARS FOUND IN THIS CATEGORY!')

#         else:
#             print('INVALID EMAIL OR PASSWORD!')
 
        