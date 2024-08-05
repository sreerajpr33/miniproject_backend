import mysql.connector


con = mysql.connector.connect(
    host="localhost",
    user="sreeraj",
    password="sree12345687", 
    database="mydatabase"   
)

cursor = con.cursor()
def add():        
    acc_id = int(input('Enter ID: '))
    name= input('Enter name of accessory: ')
    vehiclename =input('Enter vehicle name that suits: ')
    price = float(input('Enter the price : '))  
    cursor.execute('insert into accesories (acc_id, name, vehiclename, price) VALUES (%s, %s, %s, %s)', (acc_id, name, vehiclename,price))
    con.commit()

def view():
    cursor.execute('SELECT * FROM accesories')
    data = cursor.fetchall()
    print("{:<10}{:<20}{:<20}{:<15}".format('id', 'accessory_name', 'vehicle_suits', 'price'))
    print('_' * 65)
    for i in data:
        print("{:<10}{:<20}{:<20}{:<15}".format(i[0], i[1], i[2], i[3]))

def update():
    acc_id = int(input('Enter ID: '))
    cursor.execute('SELECT * FROM accesories WHERE acc_id = %s', (acc_id,))
    data = cursor.fetchone()
    if data:
        name = input('Enter name of accessory: ')
        vehiclename = input('Enter vehicle name that suits: ')
        price = float(input('Enter the price: '))
        cursor.execute('UPDATE accesories SET name = %s, vehiclename = %s, price = %s WHERE acc_id = %s', (name, vehiclename, price, acc_id))
        con.commit()
        print("Record updated successfully.")
    else:
        print("ID doesn't exist.")
def delete():
    acc_id = int(input('Enter ID: '))
    cursor.execute('DELETE FROM accesories WHERE acc_id = %s', (acc_id,))
    con.commit()
    print("Record deleted successfully.")