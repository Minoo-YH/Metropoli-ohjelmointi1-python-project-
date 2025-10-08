from context.run import run_query

def update_battery_by_distance(user, distance):
    """
    Reduce battery based on distance traveled.
    Each 10 km = 1% battery used.
    """
    try:
        battery_used = distance / 10
        new_battery = max(user["battery"] - battery_used, 0)

        query = "UPDATE users SET battery = %s WHERE id = %s"
        run_query(query, (new_battery, user["id"]))

        user["battery"] = new_battery

        print(f"🔋 Battery reduced by {battery_used:.2f}% → Remaining: {new_battery:.2f}%")

        if new_battery <= 0:
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