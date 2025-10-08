from src.models.flight_model import get_all_flights, add_flight

from src.utils.logger import log_info, log_error


def show_flights():
    print("✈️ Flights:")
    flights = get_all_flights()
    print_table(flights)

def new_flight():
    f = {
        "flight_no": input("Flight no: "),
        "airline": input("Airline: "),
        "origin": input("Origin: "),
        "destination": input("Destination: "),
        "depart_at": input("Depart at (YYYY-MM-DD HH:MM:SS): "),
        "arrive_at": input("Arrive at (YYYY-MM-DD HH:MM:SS): "),
        "price": float(input("Price: ")),
        "status": "SCHEDULED"
    }
    if add_flight(f):
        print("✅ Flight added successfully.")
