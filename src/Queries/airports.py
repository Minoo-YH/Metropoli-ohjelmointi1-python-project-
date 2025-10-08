from context.run import run_query

current_ident = None

def get_airports_code(iso_country=None):
    try:
        if not iso_country:
            iso_country = input("Type your country code (e.g., FI, US, SW): ==> ").strip().upper()

        airports = run_query(
            "SELECT ident, name FROM airport WHERE iso_country = %s ORDER BY name",
            (iso_country,)
        )

        if airports:
            print(f"\nAirports in {iso_country}:")
            for airport in airports:
                print(f"ID: {airport['ident']}, Name: {airport['name']}")
        else:
            print(f"No airports found in {iso_country}")

        return airports
    except Exception as e:
        print(f"An Err: {e}")
        return None

def get_one_airport(ident: str):
    if not ident:
        return None
    sql = """
        SELECT ident, name, iso_country, continent, municipality, latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
        LIMIT 1
    """
    return run_query(sql, (ident.upper(),), fetchone=True)
