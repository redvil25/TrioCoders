# Bus Ticket Management System

Team name: TrioCoders 

Team Members and Roll No :                          
(1) Narala Venkata Vishal Reddy - BC2025067
(2) Tiyyagura Chandra Sekhar Reddy - BC2025104
(3) Md Adil Jawadh - BC2025060

# Project Overview 
This project is a simple Python Bus Ticket System that works like a basic real-life booking system.  

It supports:
    Viewing available buses  
    Booking tickets  
    Cancelling tickets  
    Viewing all bookings  
    Saving and loading data using JSON  

# Concepts Used  
    Python functions & modules  
    Object-Oriented Programming (Classes & Objects)  
    File Handling (JSON)  
    Lists & Dictionaries  
    Loops & Conditionals  

# Libraries  
 Python standard libraries:  
    json  
    os 

# File Details  

# 1. bus_system.py
Contains:
- Bus class  
- BusSystem class  
Handles booking, cancellation, seat tracking, and bus management.

# 2. utils.py 
Handles:
- Saving bookings to JSON  
- Loading data when program starts  

# 3. main.py
A simple interactive menu-based UI for user operations.

#  How to Run the Project  

1. Install Python 3  
2. Keep all .py files in one folder  
3. Open terminal in that folder  
4. Write the command 'python3 main.py' and press enter

# Input/Output Example  

1. View All Buses
2. Book Ticket
3. Cancel Ticket
4. View Bus Bookings
5. Save & Exit


Enter option: 1

Available Buses:
Bus ID: BUS101 | Route: Hyderabad → Bangalore | Seats Left: 30 / 30
Bus ID: BUS202 | Route: Chennai → Vizag | Seats Left: 25 / 25
Bus ID: BUS303 | Route: Mumbai → Pune | Seats Left: 40 / 40

Enter option: 2
Enter Bus ID: BUS202
Enter Passenger Name: Adil
Ticket Booked Successfully! Seat Number: 1

Enter option: 4
Enter Bus ID: BUS202

Bookings:
Seat 1 - Adil


 
