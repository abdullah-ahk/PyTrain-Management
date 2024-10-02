import random  # random to generate random numbers for the receipt.no
from datetime import datetime as dt  # datetime to get current date and time
import sqlite3 # database engine  

class Train:
    train_name = "FastTrack-Express"
    
    def __init__(self, route_name, available_seats, fare, balance):
        self.name = input("Enter your name: ")
        self.route_name = route_name
        self.seats = available_seats
        self.fare = fare
        self.ticketno = random.randint(100, 900)
        self.balance = balance
        while True:
            try:
                self.myseats = int(input("Enter the number of seats you want to buy for this route: "))
                if self.seats - self.myseats >= 0:
                    break
                else:
                    raise ValueError(f"Not enough available seats || Available seats left are: {self.seats} ")
            except ValueError as e:
                print(e)
                print("Please enter a valid number of seats.")
        self.dt = dt.now()

    def seats_deduction(self):
        self.seats -= self.myseats
        c.execute("UPDATE route SET available_seats = ? WHERE route_name = ?", (self.seats, self.route_name))
        conn.commit()
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
                f"Date & Time of Receipt: {self.dt.strftime('%Y-%m-%d %H:%M:%S')}")  # to print current date and time
        return info


# Set up the SQLite database connection
conn = sqlite3.connect("train_management.db")
c = conn.cursor()

# Create the route and passenger information tables
c.execute("""CREATE TABLE IF NOT EXISTS route (
          route_id INTEGER PRIMARY KEY,
          route_name TEXT NOT NULL,
          route_destination TEXT NOT NULL,
          available_seats INTEGER,  
          fare INTEGER 
)""")

c.execute("""CREATE TABLE IF NOT EXISTS passengerinfo (
         s_no INTEGER PRIMARY KEY,
         ticket_id INTEGER,
         passenger_name TEXT NOT NULL,
         ticket_purchased INTEGER,
         route_name TEXT,
         fare_paid INTEGER,
         remaining_balance INTEGER,
         datetime TEXT
)""")
conn.commit()

# List of routes details to insert into route data
routes_details = [
    ("Route1", "Lahore", 40, 1000),  # Karachi to Lahore
    ("Route2", "Rawalpindi", 30, 9000),  # Karachi to Rawalpindi
    ("Route3", "Multan", 10, 5000)  # Karachi to Multan
]

# Insert route data if it does not exist already
c.execute("SELECT COUNT(*) FROM route")
if c.fetchone()[0] == 0:
    c.executemany("INSERT INTO route (route_name, route_destination, available_seats, fare) VALUES (?, ?, ?, ?)", routes_details)
    conn.commit()


# Function to book a ticket
def book_ticket(route_name):
    c.execute("SELECT available_seats, fare FROM route WHERE route_name = ?", (route_name,))
    result = c.fetchone()
    available_seats = result[0]
    fare = result[1]

    if available_seats <= 0:
        print(f"Tickets for {route_name} have been sold out.")
        return

    totalmoney = int(input("Enter current bank status: "))
    train_ticket = Train(route_name, available_seats, fare, totalmoney)
    print("\n")
    train_ticket.fare_deduction()
    i=input("Do you want to print Passenger Receipt || press ('y'): ")
    if(i=='y'):
        print("\n------------------------ Passenger Receipt -----------------------------")
        print(train_ticket.getinfo())
        print("------------------------------------------------------------------------\n")
    available_seats = train_ticket.seats_deduction()
    c.execute("""INSERT INTO passengerinfo (
                 ticket_id, passenger_name, ticket_purchased, route_name, fare_paid, remaining_balance, datetime)
                 VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                 (train_ticket.ticketno, train_ticket.name.lower(), train_ticket.myseats, route_name,
                 train_ticket.fare * train_ticket.myseats, train_ticket.balance, train_ticket.dt.strftime('%Y-%m-%d %H:%M:%S')))
    conn.commit()


# Main function
def main():
    i = "y"
    while i.lower() == "y":
        print("\nWelcome to the FastTrack-Express!")
        print("------------------------------------------------")
        print("Choose your journey from Karachi to your desired destination:")
        print("------------------------------------------------")

        c.execute("SELECT * FROM route")
        routes_data = c.fetchall()

        for idx, route in enumerate(routes_data, start=1):
            print(f"{route[1]}: Karachi to {route[2]}\nPrice: {route[4]} | Tickets Available: {route[3]} (Press {idx})")
            print("------------------------------------------------")

        opt = input("Enter your option (1/2/3): ")

        if opt in ("1", "2", "3"):
            route_name = routes_data[int(opt) - 1][1]
            book_ticket(route_name)
        else:
            print("Invalid input.")

        print("-------Seats Left--------")
        c.execute("SELECT * FROM route")
        updated_routes_data = c.fetchall()
        for route in updated_routes_data:
            print(f"Tickets for {route[1]}: {route[3]}")
        print("------------------------------------------------------------------------------")

        i = input("Do you want to add the next passenger? (press 'y' for yes): ")

    conn.close()

# to print all passenger information
def all_passenger_info():
    conn=sqlite3.connect("train_management.db")
    c=conn.cursor()
    c.execute("SELECT * FROM passengerinfo")
    data=c.fetchall()
    print(f"{'ID':<5} {'TICKET.NO':<10} {'PASSENGER-NAME':<20} {'TICKET-PURCHASED':<18} {'ROUTE-NAME':<15} {'FARE-PAID':<12} {'BALANCE-LEFT':<15} {'DATE & TIME':<20}")
    print("-" * 120)
    for item in data:
        print(f"{item[0]:<5} {item[1]:<10} {item[2]:<20} {item[3]:<18} {item[4]:<15} {item[5]:<12} {item[6]:<15} {item[7]:<20}")
    conn.commit()
    conn.close()

def specific_passenger():
    conn=sqlite3.connect("train_management.db")
    c=conn.cursor()
    name=input("enter a name of passenger who's information you wanna print :")
    print("\n\n")
    c.execute("SELECT * FROM passengerinfo WHERE passenger_name = ?",(name.lower(),))
    data=c.fetchone()
    print(f"{'ID':<5} {'TICKET.NO':<10} {'PASSENGER-NAME':<20} {'TICKET-PURCHASED':<18} {'ROUTE-NAME':<15} {'FARE-PAID':<12} {'BALANCE-LEFT':<15} {'DATE & TIME':<20}")
    print("-" * 120)
    print(f"{data[0]:<5} {data[1]:<10} {data[2]:<20} {data[3]:<18} {data[4]:<15} {data[5]:<12} {data[6]:<15} {data[7]:<20}")
    conn.commit()
    conn.close()

def delete_passenger():
    conn=sqlite3.connect("train_management.db")
    c=conn.cursor()
    name=input("enter a name of passenger who's information you wanna delete :")
    print("\n\n")
    c.execute("SELECT * FROM passengerinfo")
    c.execute("DELETE FROM passengerinfo WHERE passenger_name = ?",(name.lower(),))
    conn.commit()
    conn.close()


# main menu 
m ='m'
while(m=='m'):
    print("\n" + "="*60)
    print("🚂  Welcome to the FastTrack-Express Passenger System 🚂")
    print("="*60)
    print("\nHow can i assist you today?")
    print("-"*60)
    print("[i] Insert new passenger data")
    print("[a] Print all passengers' data")
    print("[p] Print a specific passenger's data")
    print("[d] Delete a passenger record")
    print("[q] Quit the system")
    print("-"*60)
    options =input()
    match options.lower():

        case "i":
            if __name__ == "__main__":
                main()
        case "a":
            all_passenger_info()
        case "p":
            specific_passenger()
        case "d":
            delete_passenger()
        case _:
            print("'invalid option 🚩")
    print("-"*50)
    m =input("Do you want to open main menu | (press 'm')")



    
