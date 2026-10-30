# USER INTERFACE


from bus_system import BusSystem
from utils import load_data, save_data

def main():
    system = BusSystem()
    load_data(system)

    while True:
        print("\n==============================")
        print("     BUS TICKET SYSTEM")
        print("==============================")
        print("1. View All Buses")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Bus Bookings")
        print("5. Save & Exit")
        print("==============================")

        choice = input("Enter option: ")

    # Show list of all available buses
        if choice == "1":
            buses = system.list_buses()
            print("\nAvailable Buses:")
            for b in buses:
                print(f"Bus ID: {b['bus_id']} | Route: {b['route']} | Seats Left: {b['available']} / {b['total']}")

    # Book a seat in a bus
        elif choice == "2":
            bus_id = input("Enter Bus ID: ")
            bus = system.get_bus(bus_id)
            if bus:
                name = input("Enter Passenger Name: ")
                seat_no = bus.book_seat(name)
                if seat_no:
                    print(f"Ticket Booked Successfully! Seat Number: {seat_no}")
                else:
                    print("No seats available!")
            else:
                print("Invalid Bus ID")

    # Cancel a booked ticket
        elif choice == "3":
            bus_id = input("Enter Bus ID: ")
            bus = system.get_bus(bus_id)
            if bus:
                seat_no = int(input("Enter Seat Number to Cancel: "))
                if bus.cancel_ticket(seat_no):
                    print("Ticket Cancelled Successfully.")
                else:
                    print("Invalid Seat Number")
            else:
                print("Invalid Bus ID")

    # Show all bookings of a specific bus  
        elif choice == "4":
            bus_id = input("Enter Bus ID: ")
            bus = system.get_bus(bus_id)
            if bus:
                print("\nBookings:")
                for t in bus.view_bookings():
                    print(f"Seat {t['seat_no']} - {t['name']}")
            else:
                print("Invalid Bus ID")

    # Save data and exit program
        elif choice == "5":
            save_data(system)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
