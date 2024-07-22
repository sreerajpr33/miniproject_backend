from reg import*
# pets={1:['s',2,'d','ekm']}
def others(up,s_key):
    for key,values in up.items():
        if key==uphone:
            continue
        print()
        print("{:<15} {:<15} {:<15} {:<15} {:<15}{:<15}".format("userphone", "pet id", "pet name", "age", "type", "place"))
        print('_' * 85)
        user_pets = up[key]
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(key, user_pets[0], user_pets[1], user_pets[2], user_pets[3], user_pets[4]))
        print()
up={123:[1,'boxer',1,'dog','ekm'],223:[2,'kitty',2,'cat','ekm']}
uphone=int(input('ENTER YOUR PHONE NUMBER :'))
password=input('ENTER YOUR PASSWORD :')
f=0
for i in users:
    if i['phone'] == uphone and i['password']==password :
        f=1
        print('LOGIN SUCESSFULL!')
        while True:
            print('1.add pets\n2.view added pets\n3.delete added pets\n4.adopt\n5.exit')
            ch=int(input('ENTER YOUR CHOICE :'))
            if ch==1:
                p_name=input('ENTER PET NAME :')
                p_age=int(input('HOW OLD IS YOUR PET :'))
                p_type=input('ENTER THE TYPE :')
                p_place=input('PLACE :')
                if not up:
                    # pets[1]=[p_name,p_age,p_type,p_place]
                    up[uphone]=[1,p_name,p_age,p_type,p_place]
                    print('PET ADDED!')
                else:
                    new_petid = max(up.keys()) + 1
                    # pets[new_petid]=[p_name,p_age,p_type,p_place]
                    up[uphone]=[new_petid,p_name,p_age,p_type,p_place]
                    print('PET ADDED!')
            elif ch == 2:
                if uphone in up:
                    print()
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}{:<15}".format("userphone", "pet id", "pet name", "age", "type", "place"))
                    print('_' * 85)
                    user_pets = up[uphone]
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(uphone, user_pets[0], user_pets[1], user_pets[2], user_pets[3], user_pets[4]))
                    print()
                else:
                    print("No pets found for this phone number.") 
            elif ch==3:
                if uphone in up:
                    print()
                    print("{:<15} {:<15} {:<15} {:<15} {:<15}{:<15}".format("userphone", "pet id", "pet name", "age", "type", "place"))
                    print('_' * 85)
                    user_pets = up[uphone]
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(uphone, user_pets[0], user_pets[1], user_pets[2], user_pets[3], user_pets[4]))
                    print()
                    p_id=int(input('ENTER THE PET ID YOU WANT TO DELETE :'))
                    if p_id==user_pets[0]:
                        # del pets[p_id]
                        del up[uphone]
            if ch == 4:
                
                s_key=uphone
                others(up,s_key)
                a_pet=int(input('enter the id of pet you want to adopt :'))
                b=0
                for keys,values in up.items():
                    if a_pet==values[0]:
                        f=1
                        print('adoption sucessfull!')
                        
                    if f==0:
                        print('invalid id')







                
            elif ch==5:
                break    
                
if f==0:
    print('INVALID PHONENUMBER OR PASSWORD!')
