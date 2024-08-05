import mysql.connector
from acc import*

con = mysql.connector.connect(
    host="localhost",
    user="sreeraj",
    password="sree12345687", 
    database="mydatabase"   
)

cursor = con.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS accesories (acc_id INT, name VARCHAR(255), vehiclename VARCHAR(255),price VARCHAR(20))")
while True:
    print('1.add accessories\n2.view accessories\n3.update accessories\n4.delete accessories\n5.exit')
    choice=int(input('enter your choice :'))
    if choice==1:
        add()

    elif choice==2:
        view()    
            
    elif choice == 3:
        update()

    elif choice == 4:
        delete()

    elif choice==5:
        print("Exiting...!")
        break
    else:
        print("Invalid choice. Please try again.")
        
            
            
