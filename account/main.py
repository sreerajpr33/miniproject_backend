import  random
import hashlib
accounts=[]
while True:
    print("1.create account\n2.login to account")
    choice=int(input('enter your choice :'))
    if choice==1:
        name=input('enter your name :')
        pin=input('enter your pin :')
        balance=0
        pin_bytes = pin.encode()
        hashed_pin = hashlib.sha256(pin_bytes).hexdigest()
        account_number= random.randint(100000,999999)
        if account_number not in accounts:
            accounts={"accountnumber":account_number,"name":name,"balance":balance,"password":hashed_pin}
            f=open(f"miniproject_backend/account/{account_number}.txt",'x')
            f.write(f"details : {accounts}")
            print(accounts)
        print(f"your account number is {account_number}")
    elif choice==2:
        acc_no=int(input('enter account no :'))
        f=0
        for i in accounts :
            if acc_no == i['accountnumber']: 
                f=1
                pinno=input('enter the pin :')
                pinbytes = pinno.encode()
                hash_pin = hashlib.sha256(pinbytes).hexdigest()
                for i in accounts:
                    q=0
                    if hash_pin==i['password']:
                        q=1
                        print('login sucessfull!')
                    if q==0:
                        print('incorrect pin ')
            if f==0:
                print('wrong account number!')
    elif choice==3:
        print('exiting...!')
        break
    else:
        print('invalid choice....!')