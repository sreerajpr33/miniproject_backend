print('PET ADOPTION')
from reg import*
from login import*
while True:
    print('1.register\n2.login\n3.exit')
    choice=int(input('ENTER YOUR CHOICE :'))
    if choice==1:                              #adopter side only
        reg()
    elif choice==2:
        login()
    elif choice==3:
        break
    else:
        print('invalid choice!')