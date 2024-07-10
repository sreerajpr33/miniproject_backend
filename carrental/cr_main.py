print('CAR RENTAL SERVICE')
from cr_reg import*
from cr_login import*
while True:
    print('1.register\n2.login\n3.exit')
    ch=int(input('enter your choice :'))
    if ch==1:
        register()
    if ch==2:
        login()
        
        

        


