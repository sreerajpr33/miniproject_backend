from datetime import datetime

# Car data
cars = [
    {'car_plate': 'so1', 'car_name': 'bmw', 'capacity': '2', 'price': '6000RS', 'category': 'luxury'},
    {'car_plate': 'so2', 'car_name': 'porsche', 'capacity': '2', 'price': '8000RS', 'category': 'sports'}
]

# Available categories
categories = ['hatchback', 'sedan', 'suv', 'muv', 'coupe', 'convertible', 'pickup']

# Initialize bookings dictionary
bookings = {}
while True:
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
        bookings[b_car].append(booking_date)
        print(f'Car {b_car} booked successfully for {booking_date}.')

    def main():
        b_car, b_days = get_user_input()
        booking_date = validate_date(b_days)
        
        if not check_car_exists(b_car, cars):
            print('Car not found.')
            return
        
        if check_booking_exists(b_car, booking_date, bookings):
            print('Car is already booked on this date.')
        else:
            add_booking(b_car, booking_date, bookings)
        
        print('Current bookings:', bookings)

    if __name__ == "__main__":
        main()





