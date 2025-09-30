from  context.run import run_query
current_ident = None  

def get_airports():
    try:
        airports = run_query("SELECT ident, name FROM airport")
        for airport in airports:
            print(f"ID: {airport[0]}, Name: {airport[1]}")
        return airports
    except Exception as e:
        print(F"An Err {e}")



def get_airports_iso_country(iso_country):
    try:
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
    except Exception as e:
        print(F"An Err {e}")



def get_airports_code():
    try:
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
    except Exception as e:
        print(f"An Err {e}")
        return None



def get_one_airport():
    global current_ident
    while True:
        try:
            chosen_ident = input("Choose your destination airport by ID: ==> ").strip()

            
            if chosen_ident == current_ident:
                print("You are already at this airport. Please choose a different one.")
                continue

            airports = run_query(
                """
                SELECT ident, name, latitude_deg, iso_country
                FROM airport
                WHERE ident = %s
                """,
                (chosen_ident,)
            )
        
            if airports:

                airport = airports[0] 

                current_ident = chosen_ident

                print("=== Airport Information ===")
                columns = ["ident", "name", "latitude_deg", "iso_country"]    
                for col, val in zip(columns, airport):
                    print(f"{col}: {val}")
                return airport
            else:
                print("Invalid airport ID.")
                return None
        except Exception as e:
            print(f"An Err: {e} ")

