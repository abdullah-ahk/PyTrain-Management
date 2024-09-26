import random # random to generate random numbers for the receipt.no
import os # os module for handling file and directory operations
from datetime import datetime as dt #datetime to get current date and time

count=1
class Train:
    train_name = "FastTrack-Express"
    
    def __init__(self, r, f, balance):
        self.name = input("Enter your name: ")
        self.seats = r
        self.fare = f
        self.ticketno = random.randint(100, 900)
        self.balance = balance
        self.myseats = int(input("Enter number of seats you want to buy for this route: "))
        self.dt=dt.now()
    
    def seats_deduction(self):
        self.seats -= self.myseats
        return self.seats
    
    def fare_deduction(self):
        total_fare = self.myseats * self.fare
        self.balance -= total_fare
        return self.balance
    
    def getinfo(self):
        info = (f"Train Name: {self.train_name}\n"
                f"Passenger Name: {self.name.capitalize()}\n"
                f"Ticket No: {self.ticketno}\n"
                f"Tickets Purchased: {self.myseats}\n"
                f"Total Fare Paid: {self.fare * self.myseats}\n"
                f"Remaining Balance: {self.balance}\n"
                f"Date & Time of Receipt: {self.dt.strftime('%Y-%m-%d %H:%M:%S')}") # to print current date and time 
        return info



def read_remaining_seats(route_name, default_seats):
    # Reads the remaining seats from file, if it exists.
    file_path = f"File{route_name}/Remaining_seats.txt"
    if os.path.exists(file_path):# it checks if the file_path exist in the directory or not 
        with open(file_path, "r") as f_seats:
            return int(f_seats.read().strip())
    else:
        return default_seats



def book_ticket(route_name, available_seats, route_fare):
    if available_seats <= 0:
        print(f"Tickets for {route_name} have been sold out.")
        return available_seats
    
    totalmoney = int(input("Enter current bank status: "))
    train_ticket = Train(available_seats, route_fare, totalmoney)
    
    print("\n------------------------ Passenger Receipt -----------------------------")
    train_ticket.fare_deduction()
    print(train_ticket.getinfo())
    print("------------------------------------------------------------------------\n")
    available_seats = train_ticket.seats_deduction()
    
    # Writing data to files
    global count
    with open(f"File{route_name}/Remaining_seats.txt", "w") as f_seats, open(f"File{route_name}/file{count}_info.txt", "w") as f_info:
        f_seats.write(str(available_seats))
        f_info.write(train_ticket.getinfo())
        
    count+=1
    return available_seats



i = "y" 
# reads the remaining seats from the file if it exists else will assign default seats 
r1 = read_remaining_seats("Route1", 40)  
r2 = read_remaining_seats("Route2", 30)  
r3 = read_remaining_seats("Route3", 10)  
fare = {"r1": 1000, "r2": 9000, "r3": 5000}# dictionary to easily access the fare through their routes

while i == "y":
    print("\n Welcome to the FastTrack-Express! ")
    print("------------------------------------------------")
    print("Choose your journey from Karachi to your desired destination:")
    print("------------------------------------------------")
    print(f"Route 1: Karachi to Lahore")
    print(f"Price: {fare['r1']} | Tickets Available: {r1}  (Press 1)")
    print("------------------------------------------------")
    print(f"Route 2: Karachi to Rawalpindi")
    print(f"Price: {fare['r2']} | Tickets Available: {r2}  (Press 2)")
    print("------------------------------------------------")
    print(f"Route 3: Karachi to Multan")
    print(f"Price: {fare['r3']} | Tickets Available: {r3}  (Press 3)")
    print("------------------------------------------------")
    opt = input("Enter your option (1/2/3): ")
    
    if opt == "1":
        r1 = book_ticket("Route1", r1, fare['r1'])
    elif opt == "2":
        r2 = book_ticket("Route2", r2, fare['r2'])
    elif opt == "3":
        r3 = book_ticket("Route3", r3, fare['r3'])
    else:
        print("Invalid input.")
    
    print("-------Seats Left--------")
    print(f"Tickets for Route 1: {r1}")
    print(f"Tickets for Route 2: {r2}")
    print(f"Tickets for Route 3: {r3}")
    print("------------------------------------------------------------------------------")
    
    i = input("Do you want to add the next passenger? (press 'y' for yes): ")
