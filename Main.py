import random

class Train:
    train_name = "FastTrack-Express"
    
    def __init__(self, r, f, balance):
        self.name = input("Enter your name: ")
        self.seats = r
        self.fare = f
        self.ticketno = random.randint(100, 900)
        self.balance = balance
        self.myseats = int(input("Enter number of seats you want to buy for this route: "))
    
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
                f"Remaining Balance: {self.balance}")
        return info
    
def book_ticket(route_name, available_seats, route_fare):
    if available_seats <= 0:
        print(f"Tickets for {route_name} have been sold out.")
        return available_seats
    
    totalmoney = int(input("Enter current bank status: "))
    train_ticket = Train(available_seats, route_fare, totalmoney)
    
    print("-------------------------------------------------------------------------")
    train_ticket.fare_deduction()
    print(train_ticket.getinfo())
    
    available_seats = train_ticket.seats_deduction()
    
    # Writing data to files
    with open(f"file_{route_name}_seats.txt", "w") as f_seats, open(f"file_{route_name}_info.txt", "w") as f_info:
        f_seats.write(str(available_seats))
        f_info.write(train_ticket.getinfo())
    
    return available_seats


# Initial route setup
i = "y"
r1 = 40
r2 = 30
r3 = 10

fare = {"r1": 1000, "r2": 9000, "r3": 5000}

while i == "y":
    print("----Hello, welcome to FastTrack-Express!-----")
    opt = input(f"\nRoute 1: Karachi to Lahore\nPrice: {fare['r1']} | Tickets Available: {r1} (press 1)"
                f"\nRoute 2: Karachi to Rawalpindi\nPrice: {fare['r2']} | Tickets Available: {r2} (press 2)"
                f"\nRoute 3: Karachi to Multan\nPrice: {fare['r3']} | Tickets Available: {r3} (press 3)"
                "\nEnter your option: ")
    
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
