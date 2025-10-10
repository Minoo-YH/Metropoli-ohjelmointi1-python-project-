from context.run import run_query
from Queries.sql import query

current_ident = None

def get_airports_code(iso_country=None):
    try:
        if not iso_country:
            iso_country = input("Type your country code (e.g., FI, US, SW): ==> ").strip().upper()
        if not iso_country:
            print("Error: Country code cannot be empty.")
            return None
        airports = run_query(
            query("get_airports_code"),
            (iso_country,)
        )
        print(f"\nAirports in {iso_country}:")
        print("\n=========================")
        print(f"{'ID':<10} | {'Name':<50}")
        print("-" * 65)
        for airport in airports:
            print(f"{airport['ident']:<10} | {airport['name']:<50}")
        print("-" * 65)

        return airports

    except Exception as e:
        print(f"An Err: {e}")
        return None


def get_one_airport(current_location=None):
    global current_ident
    while True:
        try:
            selected_code = input("Choose your destination airport by ID (or type C to cancel): ==> ").strip().upper()

            if not selected_code:
                print("No ID entered. Canceling selection.")
                return None

            if selected_code == "C":
                print("Selection canceled.")
                return None

            if current_location and selected_code == str(current_location).upper():
                print("You are already at this airport. Please choose a different one.")
                continue

            if selected_code == current_ident:
                print("You already in this airport . Choose another.")
                continue

            airport_results = run_query(
                """
                SELECT ident, name, latitude_deg, longitude_deg, iso_country
                FROM airport
                WHERE ident = %s
                """,
                (selected_code,)
            )

            if not airport_results:
                print("Invalid airport ID. Try again or type C to cancel.")
                continue

            airport_data = airport_results[0]
            print("\n=========================")
            print(f"{'Field':<20} | {'Value'}")
            print("-" * 50)
            for key, value in airport_data.items():
                print(f"{key:<20} | {value}")
            print("=" * 50 + "\n")

            current_ident = selected_code
            return airport_data

        except Exception as error:
            print(f"Error: {error}")
            return None
