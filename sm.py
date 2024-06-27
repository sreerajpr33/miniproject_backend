product=[[123,'apple',20],[234,'orange',25]]
while True:
    print('1.add product\n2.viewproduct\n3.updateproduct\n4.delectproduct\n5.exit')
    choice=int(input('enter your choice :'))


    if choice==1:
        print()
        p_id=int(input('enter product ID :'))
        p_name=input('enter product name :')
        p_price=int(input('enter the price of product :'))
        product.append([p_id,p_name,p_price])
        print()

    elif choice==2:
        for i in product:
            print()
            print('product ID :',i[0])
            print('product name :',i[1])
            print('price :',i[2])
            print('..........')

    elif choice==3:
        p_id=int(input('enter the product id you want to edit :'))
        f=0
        for i in product:
            if p_id==i[0]:
                f==1
                print(i)
                p_name=str(input('enter product name :'))
                p_price=int(input('enter the price of product :'))
                i[1]=p_name
                i[2]=p_price
        if f==0:
            print('invalid id')

    elif choice==4:
        p_id=int(input('enter the product id you want to delete : '))
        f=0
        for i in product:
            if i in product:
                f=1
                product.remove(i)
        if f==0:
            print('invalid id')
            
    elif choice==5:
        print('you have exited')
        break

                



    