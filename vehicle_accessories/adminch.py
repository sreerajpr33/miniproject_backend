import sqlite3
con=sqlite3.connect("miniproject_backend/vehicle_accessories/v_accessories.db")    
def add():
    name =str(input('ENTER THE ACCESSORY NAME :'))
    vtype =input('ENTER VEHICLE TYPE(BIKE/CAR):')
    vmodel=input('ENTER THE VEHICLE TYPE ACCESSORY SUITS:')
    price=int(input('ENTER THE PRICE:'))
    con.execute("insert into accessories(name ,vehicletype ,vehiclemodel ,prince)values(?,?,?,?)",(name,vtype,vmodel,price))
    con.commit()
def update():
    
