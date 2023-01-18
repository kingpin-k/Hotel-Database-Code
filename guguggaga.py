import csv
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="kingpin123",database="hotel")
cursor=mycon.cursor()
if mycon.is_connected():
    print("Successfully connected to Hotel database")

f=open("databse.csv","a")
csvwriter = csv.writer(f)
f1=open("room_check.txt","a")
csvwriter=csv.writer(f1)
id=0

print("   _____                                 _____      _                ")
print("  / ____|                               |  __ \    | |               ")
print(" | |     __ _  ___  ___  __ _ _ __ ___  | |__) |_ _| | __ _  ___ ___ ")
print(" | |    / _` |/ _ \/ __|/ _` | '__/ __| |  ___/ _` | |/ _` |/ __/ _ \ ")
print(" | |___| (_| |  __/\__ \ (_| | |  \__ \ | |  | (_| | | (_| | (_|  __/")
print("  \_____\__,_|\___||___/\__,_|_|  |___/ |_|   \__,_|_|\__,_|\___\___|")
print("")
print("1: Book a new room")
print("2: Check all rooms")
print("3: Option 3")
ch=int(input("Enter your choice: "))
if ch==1:
    print("-------")
    print("BOOKING")
    print("-------")
    name=input("Enter customer name: ")
    print("Please choose your room preference- ")
    print("1: Presidential Suite")
    print("2: Business Suite")
    print("3: Classic Room")
    room=int(input("1/2/3: "))
    if room==1:
        room="Presidential Suite"
    elif room==2:
        room="Business Suite"
    elif room==3:
        room="Classic Room"
    else:
        print("Invalid entry.")
    print("Enter check-in date: ")
    cind=int(input("Date: "))
    cinm=int(input("Month: "))
    cin=str(cind)+"/"+str(cinm)
    print("Enter check-out date: ")
    coutd=int(input("Date: "))
    coutm=int(input("Month: "))
    cout=str(coutd)+"/"+str(coutm)
    l=[name,room,cin,cou]t
    csvwriter.writerow(l)
    v="INSERT INTO guests VALUES(%s,%s,%s,%s"
    print("\n***************")
    print("BOOKING DETAILS")
    print("***************")
    print("Customer's name:",name)
    print("Room Type:",room)
    print("Check-in:",cin,"|","Check-out:",cout)
    
if ch==2:
    print("--------")
    print("CHECKING")
    print("--------")
    print("Presidential Suite:",psuite,"out of 2")
    print("Business Suite:", bsuite,"out of 4")
    print("Classic room:",croom,"out of 4")

f.close()
    
    
