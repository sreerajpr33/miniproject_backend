acc=[['s',12345,'s.com','123',300]]
while True:
    print('1.regestration\n2.login')
    choice=int(input("enter your choice :"))
    
    if choice==1:
        name=input("enter your name :")
        phno=int(input("enter the phone number :"))
        email=input("enter your email :")
        password=input("enter your password :")
        acc.append([name,phno,email,password,0])
    elif choice==2:
        email=input("enter your email :")
        password=input("enter your password :")
        f=0
        for i in acc:
            if email==i[2] and password==i[3]:
                f=1
                print('logged in sucessfully :')
                while True:
                    print('1.balance\n2.deposite\n3.withdraw\n4.logout')
                    a=int(input('enter your choice :'))
                    if a==1:
                        print('your balance =',i[4])
                    elif a==2:
                        dep=int(input('enter the deposit amount :'))
                        i[4]+=dep
                    elif a==3:
                        witd=int(input('enter the withdrawal amount :'))
                        if i[4]<=0:
                            i[4]-=witd
                            print('withdraw sucessfully')
                        else:
                            print('insuficient amount')

                    elif a==4:
                        print('logout sucessfully')
                        break
        if f==0:
            print('incorrect email or password :')
        
