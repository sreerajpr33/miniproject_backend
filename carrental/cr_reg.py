user=[{'username':'sree','useremail':'s.com','useraddress':'tpra','userphone':12345,'userpassword':'asdf'}]    
def register():
    print()
    u_name=input('enter your name :')
    u_email=input('enter your email :')
    u_address=input('enter your address :')
    u_phone=int(input('enter your number :'))
    u_pwd=input('enter your password :')
    print()

    user_exists = False
    for usr in user:
        if usr['useremail'] == u_email:
            user_exists = True
            break

    if user_exists:
        print('THIS EMAIL IS ALREADY USED!')
    else:
        user.append({'username': u_name,'useremail':u_email,'useraddress':u_address,'userphone':u_phone,'userpassword':u_pwd})
        print("Registration successful!")


                    





            
            
            
