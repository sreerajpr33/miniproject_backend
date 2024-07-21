users=[{'name':'s','phone':123,'password':'Qwe'}]
def reg():
    import re
    name=input('ENTER YOUR NAME :')
    ph_no=int(input('ENTER YOUR PHONE NUMBER :'))
    password=input('ENTER YOUR PASSWORD :')
    if re.search('[A-Z]',password):
        user_exist=False
        for user in users:
            if user['phone'] == ph_no:
                user_exist=True
                break
        if user_exist :
                print('PHONE NUMBER ALREADY USED :')
        else:
                users.append({'name':name,'phone':ph_no,'password':password})
                print('REGISTRATION IS SUCCESSFULL!')
        print(users)
    else:
        print('USE SOME CAPITAL LETTERS!')


