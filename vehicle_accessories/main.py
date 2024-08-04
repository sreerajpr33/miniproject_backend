import sqlite3
from adminch import*
con=sqlite3.connect("miniproject_backend/vehicle_accessories/v_accessories.db")

try:
    con.execute("create table accessories(name text,vehicletype text,vehiclemodel varchar,prince int)")
except:
    pass
users=[]
while True:
    choice=int(input('1.register\n2.login\n3.exit\nenter your choice:'))
    if choice==1:
        uname=input('enter user name :')
        phoneno=int(input('enter phonenumber :'))
        passw=input("enter your passsword :")
        user_exists = False
        for user in users:
            if user[0] == uname or user[1] == phoneno:
                user_exists = True
                break
        
        if user_exists:
            print('These details are already used!')
        else:
            users.append([uname, phoneno, passw])
            print('User registered successfully.')
        print(users)

    if choice==2:
        username=input('enter user name :')
        password=input('enter your password :')
        if username== 'admin123' and password=='123' :
            while True:
                ch=int(input('1.add\n2.update\n3.delete\nexit\nenter your choice:'))
                if ch==1:
                    add()
        else:
            print('y')

   