from context.run import run_query

current_ident = None

def get_airports_iso_country(iso_country: str):
    if not iso_country:
        return []
    sql = """
        SELECT ident, name
        FROM airport
        WHERE iso_country = %s
        ORDER BY name
    """
    return run_query(sql, (iso_country.upper(),))

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
