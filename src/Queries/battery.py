from context.run import run_query
from Queries.airports import get_airports_iso_country, get_one_airport

def update_battery_by_distance(user, distance):
    """
    Reduce battery based on distance traveled.
    Each 10 km = 1% battery used.
    """
    try:
        battery_used = float(distance) / 10
        current_battery = float(user.get("battery", 100))
        new_battery = max(current_battery - battery_used, 0)

        # Update DB
        query = "UPDATE users SET battery = %s WHERE id = %s"
        run_query(query, (new_battery, user["id"]))

        # Refresh from DB to keep user dict in sync
        result = run_query("SELECT battery FROM users WHERE id = %s", (user["id"],), fetchone=True)
        if result:
            user["battery"] = float(result[0])
        else:
            user["battery"] = new_battery

        #  Show battery info
        print(f"🔋 Battery reduced by {battery_used:.2f}% → Remaining: {user['battery']:.2f}%")

        if user["battery"] <= 5:
            print("⚠️ Battery depleted. Please recharge before next trip.")

    except Exception as e:
        print(f"Error updating battery: {e}")


def recharge_battery(user):
    """Recharge battery to 100%."""
    try:
        query = "UPDATE users SET battery = 100 WHERE id = %s"
        run_query(query, (user["id"],))
        user["battery"] = 100
        print(f"🔌 User {user['username']} battery fully charged (100%).")
    except Exception as e:
        print(f"Error charging battery: {e}")
