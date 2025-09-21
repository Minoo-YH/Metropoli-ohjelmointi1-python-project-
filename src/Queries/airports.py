from  context.run import run_query

def get_airports():
    airports = run_query("SELECT ident, name FROM airport")
    for airport in airports:
        print(f"ID: {airport[0]}, Name: {airport[1]}")
    return airports
def get_airports_iso_country(iso_country):
    airports = run_query(
       "SELECT * FROM airport WHERE iso_country = %s",
        (iso_country,)
    )
    if airports:
        print(f"\nAirports in {iso_country}:")
        for airport in airports:
            print(f"ID: {airport[0]}, Name: {airport[1]}")
    else:
        print(f"No airports found in {iso_country}")
    return airports
def get_airports_code():
    iso_country=input("Type ur country_code :==>  ")

    airports = run_query(
        "SELECT ident, name FROM airport WHERE iso_country = %s",
        (iso_country,)
    )
    if airports:
        print(f"\nAirports in {iso_country}:")
        for airport in airports:
            print(f"ID: {airport[0]}, Name: {airport[1]}")
    else:
        print(f"No airports found in {iso_country}")
    return airports







# in processing
def get_one_airport(): 
    chosen_ident = input("Choose your destination airport by ID: ==> ").strip()
    airports = run_query(
        "SELECT ident, name FROM airport WHERE ident = %s",
        (chosen_ident,)
    )
    if airports:
        airport = airports[0]
        print(f"You selected: {airport[1]} (ID: {airport[0]})")
        return airport
    else:
        print("Invalid airport ID.")
        return None
