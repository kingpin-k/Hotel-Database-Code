import csv

f=open("databse.csv","a")
csvwriter = csv.writer(f)
f1=open("room_check.txt","a")
csvwriter=csv.writer(f1)

print("\nCaesars Palace Las Vegas Hotel and Casino")
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
        psuite=psuite-1
    elif room==2:
        room="Business Suite"
        bsuite=bsuite-1
    elif room==3:
        room="Classic Room"
        croom=croom-1
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
    l=[name,room,cin,cout]
    csvwriter.writerow(l)
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
    
    
