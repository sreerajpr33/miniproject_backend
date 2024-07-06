
stations=[1,2,3,4]
print('1.station A\n2.station B\n3.station C\n4.station D')
print('each station carries RS10!')
entry_station=int(input('enter your entry station :'))
exit_station=int(input('enter your exit station :'))
tickets=int(input('number of tickets you need :'))

if entry_station in stations and exit_station in stations:

    distance = exit_station - entry_station
    if distance < 0:
        distance = -1*distance

    price = distance * tickets * 10
    print('Total price:',price,'RS')
else:
    print('Invalid station! Please enter a valid station number.')



