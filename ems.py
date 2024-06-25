worker=[[1,'a',20,2,'a@gmail.com',12345],
        [2,'b',20,2,'b@gmail.com',12345671]]
while True:
    print('1.add worker\n2.view worker\n3.update worker\n4.delete worker')
    choice=int(input('enter the choice :'))

    if choice==1:
        w_id=int(input('worker ID :'))
        w_name=str(input('enter worker name :'))
        w_age=int(input('enter the age :'))
        w_exp=int(input('experiance :'))
        w_email=input('enter the e-mail :')
        w_no=int(input('enter the phonr number :'))
        worker.append([w_id,w_name,w_age,w_exp,w_email,w_no])
    
    elif choice==2:

        for i in  worker:
            print()
            print('worker_id :',i[0])
            print('name :',i[1])
            print('age',i[2])
            print('exp',i[3])
            print('email',i[4])
            print('phone number :',i[5])
    
    elif choice==3:
        w_id=int(input("enetr your ID :"))
        f=0
        for i in (worker):
            if w_id==i[0]:
                f=1
                print(i)
                w_name=str(input('enter worker name :'))
                w_age=int(input('enter the age :'))
                w_exp=int(input('experiance :'))
                w_email=input('enter the e-mail :')
                w_no=int(input('enter the phonr number :'))
                i[1]=w_name
                i[2]=w_age
                i[3]=w_exp
                i[4]=w_email
                i[5]=w_no
        if f==0:
            print('invalid id')

    elif choice==4:
            w_id=int(input("enetr the ID :"))
            f=0
            for i in worker:
                if w_id==i[0]:
                    f=1
                    worker.remove(i)
                    print("deleted sucessfully")
                    break
            if f==0:
                print('invalid ID')
    elif choice==5:
        print("exited")
        break


            
            




    


       





