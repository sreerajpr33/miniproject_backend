from datetime import datetime
from cr_reg import*

# Car data
cars = [
    {'car_plate': 'so1', 'car_name': 'bmw', 'capacity': '2', 'price': '12000', 'category': 'sports'},
    {'car_plate': 'so2', 'car_name': 'porsche', 'capacity': '2', 'price': '15000', 'category': 'sports'},
    {'car_plate': 'so3', 'car_name': 'polo', 'capacity': '4', 'price': '3000', 'category': 'sports'},
    {'car_plate': 'so4', 'car_name': 'innova', 'capacity': '7', 'price': '5000', 'category': 'muv'},
    {'car_plate': 'so5', 'car_name': 'amg', 'capacity': '7', 'price': '11000', 'category': 'luxury'},
]



# Initialize bookings dictionary
bookings = {}


def get_user_input():
    b_car = input('Enter the registration number of the car you need: ')
    b_days = input('Enter the booking date (YYYY-MM-DD): ')
    return b_car, b_days

def validate_date(b_days):
    try:
        return datetime.strptime(b_days, '%Y-%m-%d').date()
    except ValueError:
        print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
        exit()

def check_car_exists(b_car, cars):
    return any(car['car_plate'] == b_car for car in cars)

def check_booking_exists(b_car, booking_date, bookings):
    return b_car in bookings and booking_date in bookings[b_car]

def add_booking(b_car, booking_date, bookings):
    if b_car not in bookings:
        bookings[b_car] = []
    bookings[b_car].append(booking_date)                                    #addbookings
    print(f'Car {b_car} booked successfully for {booking_date}.')

def login():
    email = input('Enter your email: ')
    password = input('Enter your password: ')
    
    if email == 'admin123' and password == '1234':
        print('LOGIN SUCCESSFUL!')
        while True:
            print()
            print('1. Add car\n2. Remove car\n3. View cars\n4. View user details\n5. View car bookings\n6. Exit')
            adch = int(input('Enter your choice: '))
            print()
            if adch == 1:
                print()
                a_cplate = input('Enter the registration number of the car: ')
                a_cname = input('Enter the car name: ')
                a_cseat = int(input('Enter the seat capacity: '))
                a_cprice = int(input('Enter the price (per 100 km): '))
                a_ccategory = input('Enter the category of the car: ')
                print()

                if any(cars['car_plate'] == a_cplate for cars in cars):
                    print('REGISTRATION NUMBER OF THE CAR ALREADY EXISTS!')
                else:
                    cars.append({'car_plate': a_cplate, 'car_name': a_cname, 'capacity': a_cseat, 'price': a_cprice, 'category': a_ccategory})
                    print('CAR ADDED SUCCESSFULLY!')
            elif adch == 2:
                print()
                a_cplate = input('Enter the registration number of the car you want to remove: ')
                a_cname = input('Enter the car name you want to remove: ')
                f = 0
                for car in cars:
                    if car['car_plate'] == a_cplate and car['car_name'] == a_cname:
                        cars.remove(car)
                        f = 1
                        print('CAR REMOVED SUCCESSFULLY!')
                if f == 0:
                    print('CAR NOT FOUND!')
            elif adch == 3:
                print()
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price", "Category"))
                print('_' * 75)
                for car in cars:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(car['car_plate'], car['car_name'], car['capacity'], car['price'], car['category']))
                print()           
            elif adch == 4:
                print("{:<15} {:<15} {:<15} {:<15} {:<15}".format('Name', 'Email', 'Address', 'Phone', 'Password'))
                print('_' * 60)
                for u in user:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(u['username'], u['useremail'], u['useraddress'], u['userphone'], u['userpassword']))
                print()
        
            elif adch == 5:
                print('Car bookings:')
                for car_plate, dates in bookings.items():
                    print(f'Car {car_plate}: {dates}')
            elif adch == 6:
                break
            else:
                print('INVALID CHOICE!')
    else:
        user_exist = any(u['useremail'] == email and u['userpassword'] == password for u in user)
        if user_exist:
            print('LOGIN SUCCESSFUL!')
            while True:
                print('1. Booking\n2. View bookings\n3. Cancel booking\n4. Exit')
                uch = int(input('Enter your choice: '))
                if uch == 1:
                    # bookings={}
                    print()
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format("Reg No", "Car Name", "Seat Capacity", "Price", "Category"))
                    print('_' * 75)
                    for car in cars:
                        print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(car['car_plate'], car['car_name'], car['capacity'], car['price'], car['category']))
                    print()
                    
                    cc_search = input('Enter the category of car you need: ').strip().lower()
                    found = False
                    for car in cars:
                        if cc_search == car['category']:
                            found = True
                            print()
                            print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(car['car_plate'], car['car_name'], car['capacity'], car['price'], car['category']))
                            

                    if found:
                        b_car, b_days = get_user_input()
                        booking_date = validate_date(b_days)

                        if not check_car_exists(b_car, cars):
                            print('Car not found.')
                        elif check_booking_exists(b_car, booking_date, bookings):
                            print('Car is already booked on this date.')
                        else:
                            add_booking(b_car, booking_date, bookings)
                        print('Current bookings:', bookings)
                    else:
                        print('NO CARS FOUND IN THIS CATEGORY!')
                elif uch == 2:
                    print('Current bookings:')
                    for car_plate, dates in bookings.items():
                        print(f'Car {car_plate}: {dates}')
                elif uch == 3:
                    b_car = input('Enter the registration number of the car to cancel booking: ')
                    b_days = input('Enter the booking date (YYYY-MM-DD) to cancel: ')
                    booking_date = validate_date(b_days)
                    if check_booking_exists(b_car, booking_date, bookings):
                        bookings[b_car].remove(booking_date)
                        print(f'Booking for car {b_car} on date {booking_date} canceled successfully.')
                        if not bookings[b_car]:
                            del bookings[b_car]
                    else:
                        print('No such booking found.')
                elif uch == 4:
                    break
                else:
                    print('INVALID CHOICE!')
        else:
            print('INVALID EMAIL OR PASSWORD!')

if __name__ == "__main__":
    login()