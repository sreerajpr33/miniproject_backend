from car_reg import*
car=[]
choice=str(input('enter user type(ADMIN/CUSTOMER) :')).strip().lower()
admin1= {'email': 'admin', 'password': 'asdf'}
if choice=='admin':
    email=input('ENTER YOUR EMAIL : ')
    password=input('ENTER YOUR PASSWORD')    
    if email==admin1['username'] and password==admin1['password']:
        print('ADMIN LOGIN SUCESSFULL')
        print('')
    else:
        print('INVALID EMAIL OR PASSWORD')    

    
