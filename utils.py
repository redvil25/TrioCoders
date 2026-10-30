import json, os
from bus_system import Bus

# File where data will be stored
DATA_FILE = "bookings.json"

def save_data(system):
    data = []
    for bus in system.buses:
        data.append({
            "bus_id": bus.bus_id,
            "route": bus.route,
            "total_seats": bus.total_seats,
            "booked_seats": bus.booked_seats
        })
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data(system):
    if not os.path.exists(DATA_FILE):
        system.load_default_buses()
        return
    
# Read existing booking data from JSON file
    with open(DATA_FILE, "r") as f:
        buses = json.load(f)

    for b in buses:
        loaded_bus = Bus(b["bus_id"], b["route"], b["total_seats"])
        loaded_bus.booked_seats = b["booked_seats"]
        system.buses.append(loaded_bus)
