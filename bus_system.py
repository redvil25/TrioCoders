
class Bus:
    def __init__(self, bus_id, route, total_seats=30):
        # Unique bus ID
        self.bus_id = bus_id
        # City Route 
        self.route = route
        # Total seats in the bus
        self.total_seats = total_seats
        # Booked seats 
        self.booked_seats = []

    def available_seats(self):
        # Calculate remaining seats
        return self.total_seats - len(self.booked_seats)

    def book_seat(self, passenger_name):
        # Assign next available seat number
        if self.available_seats() > 0:
            seat_no = len(self.booked_seats) + 1
            self.booked_seats.append({
                "seat_no": seat_no,
                "name": passenger_name
            })
            return seat_no
        return None

    def cancel_ticket(self, seat_no):
        # Cancel a ticket using seat number
        for ticket in self.booked_seats:
            if ticket["seat_no"] == seat_no:
                self.booked_seats.remove(ticket)
                # Reassign seat numbers for neatness
                for i, t in enumerate(self.booked_seats):
                    t["seat_no"] = i + 1
                return True
        return False

    def view_bookings(self):
        # Returns booked seat list
        return self.booked_seats


class BusSystem:
    def __init__(self):
        # List of bus objects
        self.buses = []

    def load_default_buses(self):
        # Preloaded buses
        self.buses = [
            Bus("BUS101", "Hyderabad → Bangalore", 30),
            Bus("BUS202", "Chennai → Vizag", 25),
            Bus("BUS303", "Mumbai → Pune", 40),
        ]

    def list_buses(self):
        # Returns summary 
        bus_info = []
        for bus in self.buses:
            bus_info.append({
                "bus_id": bus.bus_id,
                "route": bus.route,
                "available": bus.available_seats(),
                "total": bus.total_seats
            })
        return bus_info

    def get_bus(self, bus_id):
        # Retrieve a bus by ID
        for bus in self.buses:
            if bus.bus_id == bus_id:
                return bus
        return None
