class train:
    train_name= "FastTrack-Express"
    def __init__(self,r,f,balance):
        self.name=input("enter your name: ")
        self.seats=r
        self.fare=f
        self.ticketno=random.randint(100,900)
        self.balance=balance
    
    def seats_deduction(self,myseats):
        self.seats-=myseats
        return self.seats
    
    def fare_deduction(self,myseats):
        self.balance-=myseats *self.fare
        return self.balance
    
    def getinfo(self,myseats):
        print(f"train name : {self.train_name}")
        print(f"passenger name : {self.name.capitalize()}")
        print(f"passenger ticket no : {self.ticketno}")
        print(f"total tickets purchased by the passenger : {myseats}")
        print(f"total amount of fare passenger paid for {myseats} seats : {self.fare*myseats}")
        print(f"your balance left after booking is : {self.fare_deduction(myseats)}")
        
    
import random

i ="y"
n=1
r1=40
r2=30
r3=10
while(i=="y") :
    
    fare={"r1":1000 ,"r2":9000,"r3":5000}
    print("----Hello welcome to FastTrack-Express !-----")
    opt= input(f"\nRoute 1 is karachi to lahore \nprice :{fare['r1']}\nTickets available : {r1} (press 1)\nRoute 2 is karachi to rawalpindi \nprice :{fare['r2']}\nTickets available :{r2} (press 2)\nRoute 3 is karachi to multan \nprice :{fare['r3']}\nTickets available : {r3} (press 3)\nEnter your option: ")
    if (opt == "1"):
        if (r1<=0):
            print("Tickets for this Route has been sold out.")
            break
        else:
            totalmoney=int (input("enter current bank status: "))
            t1=train(r1,fare["r1"],totalmoney)
            myseats=int(input("enter number of seats u want to buy for this route : "))
            print("-------------------------------------------------------------------------")
            t1.fare_deduction(myseats)
            t1.getinfo(myseats)
            r1=t1.seats_deduction(myseats)
    elif (opt == "2"):
        if (r2<=0):
            print("Tickets for this Route has been sold out.")
            break
        else:
            totalmoney=int (input("enter current bank status: "))
            t1=train(r2,fare["r2"],totalmoney)
            myseats=int(input("enter number of seats u want to buy for this route : "))
            print("-------------------------------------------------------------------------")
            t1.fare_deduction(myseats)
            t1.getinfo(myseats)
            r2=t1.seats_deduction(myseats)
    elif (opt == "3"):
        if (r3<=0):
            print("Tickets for this Route has been sold out.")
            break
        else:
            totalmoney=int (input("enter current bank status: "))
            t1=train(r3,fare["r3"],totalmoney)
            myseats=int(input("enter number of seats u want to buy for this route : "))
            print("-------------------------------------------------------------------------")
            t1.fare_deduction(myseats)
            t1.getinfo(myseats)
            r3=t1.seats_deduction(myseats)
    else:
       print("invalid input.")    
    print("-------seats left--------")
    print(f"Tickets route 1 : {r1}")
    print(f"Tickets route 2 : {r2}")
    print(f"Tickets route 3 : {r3}")
    print("------------------------------------------------------------------------------")
    i =input("do u want to add next passenger (press 'y') : ")