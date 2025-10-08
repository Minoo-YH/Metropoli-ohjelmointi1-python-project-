def print_table(data):
    """Pretty print rows from a list of dictionaries."""
    if not data:
        print("No data found.")
        return
    headers = data[0].keys()
    print("\t".join(headers))
    for row in data:
        print("\t".join(str(v) for v in row.values()))
