from context.run import run_query
from Queries.airports import get_airports_code, get_one_airport
from context.utils import haversine
<<<<<<< HEAD
=======
from Queries.sql import query
>>>>>>> nipa_1
import bcrypt

choice_next_stop = None
current_user = None


def user_register():
    try:
        global current_user
        username = input("Type username :=> ")
        email = input("Type email :=> ")
        password = input("Type password :=> ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        location = "EFHK"
        battery = 100.0

<<<<<<< HEAD
        query = """
                INSERT INTO users (username, email, password, location, battery)
                VALUES (%s, %s, %s, %s, %s) \
                """
        values = (username, email, hashed_password.decode('utf-8'), location, battery)
        run_query(query, values)
=======
        sql = query("register") 
        values = (username, email, hashed_password.decode('utf-8'), location, battery)
        run_query(sql, values)
>>>>>>> nipa_1

        print("User registered successfully!")
    except Exception as e:
        print(f"An Err {e}")


<<<<<<< HEAD
=======

>>>>>>> nipa_1
def user_login():
    global current_user
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

<<<<<<< HEAD
        query = """
                SELECT u.id, \
                       u.username, \
                       u.email, \
                       u.password, \
                       u.location, \
                       u.battery, \
                       u.KM, \
                       u.membership,
                       a.ident, \
                       a.latitude_deg, \
                       a.longitude_deg
                FROM users u
                         JOIN airport a ON u.location = a.ident
                WHERE u.username = %s \
                """
        result = run_query(query, (username,), fetchone=True)
=======
        sql = query("user_login")
        result = run_query(sql, (username,), fetchone=True)
>>>>>>> nipa_1

        if result:
            user = dict(result)
            stored_password = user['password']

            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                user.pop('password', None)
                current_user = user
                print("LogIn successfully!")
                return True
            else:
                print("Wrong password")
                return False
        else:
            print("Wrong username")
            return False

    except Exception as e:
        print(f"An Err {e}")


<<<<<<< HEAD
=======

>>>>>>> nipa_1
def user_delete():
    try:
        global current_user
        if current_user is not None:
            delete_input = input("Type Yes if you want to delete your account (Y): ").upper()
            if delete_input == "Y":
                if isinstance(current_user, dict):
                    username = current_user.get("username")
                else:
                    username = current_user
<<<<<<< HEAD
                query = "DELETE FROM users WHERE username = %s"
                values = (username,)
                run_query(query, values)
=======

                sql = query("delete_user")
                values = (username,)
                run_query(sql, values)

>>>>>>> nipa_1
                print(f"User '{username}' deleted successfully!")
                current_user = None
            else:
                print("Account deletion canceled.")
        else:
            print("No user is currently logged in.")
    except Exception as e:
        print(f"An Err {e}")


<<<<<<< HEAD
=======


>>>>>>> nipa_1
def user_update():
    try:
        global current_user
        global choice_next_stop
        if not current_user or not choice_next_stop:
            print("Error: current_user or choice_next_stop not set.")
            return
<<<<<<< HEAD
        update_query = """
                       UPDATE users
                       SET battery  = GREATEST(battery * 0.75, 0),
                           location = %s
                       WHERE id = %s \
                       """
        rows_affected = run_query(update_query, (str(choice_next_stop['ident']), int(current_user["id"])))

        if rows_affected > 0:
            select_query = "SELECT battery FROM users WHERE id = %s"
            result = run_query(select_query, (int(current_user["id"]),), fetchone=True)

=======
        update_query = query("update_user_location","update_user_battery")
        rows_affected = run_query(update_query, (str(choice_next_stop['ident']), int(current_user["id"])))
        if rows_affected > 0:
            select_query = query("get_user_battery")
            result = run_query(select_query, (int(current_user["id"]),), fetchone=True)
>>>>>>> nipa_1
            if result:
                current_user["battery"] = float(result["battery"])
                current_user["location"] = choice_next_stop['ident']
            else:
                print("Error: battery not fetched after update.")
        else:
            print("Error: No user was updated. Check user id.")

    except Exception as e:
<<<<<<< HEAD
        print(f"An Err {e}")
=======
        print(f"An Err {e} 22")
>>>>>>> nipa_1


def user_update_battry():
    try:
        global current_user
        if not current_user:
            print("Error: current_user .")
            return

<<<<<<< HEAD
        query = """
                UPDATE users
                SET battery = 100
                WHERE id = %s \
                """
        current_user["battery"] = 100
        run_query(query, (int(current_user["id"]),))
=======
        run_query(query("update_user_battery"), (int(current_user["id"]),))
        current_user["battery"] = 100
>>>>>>> nipa_1
        print(f"User {current_user['username']} battery 100 .")
    except Exception as e:
        print(f"An Err {e}")


<<<<<<< HEAD
=======



>>>>>>> nipa_1
def next_stop(current_user=None):
    global choice_next_stop
    if not current_user:
        print("Error: No current user is logged in.")
        return

    try:
        battery_val = int(current_user.get('battery', 0))
    except Exception:
        battery_val = 0

    if battery_val <= 25:
        charging = input("UR battery under 25. You can not travel. If you want to charge, type (Y):=>").upper()
        if charging == "Y":
            user_update_battry()
            current_user["battery"] = 100
            print(f"Your battery is {current_user['battery']}.")
        else:
            print("U can not travel.")
            return None

    destination_input = input("Where do you want to go? Type country code (e.g., FI, US, SW): ").upper()
    airports = get_airports_code(destination_input)

    if not airports:
        print("No airports found for this country.")
        return None

    print("\nType the AIRPORT IDENT you want to go (e.g., EFHK):")
    target_ident = input("Ident: ==> ").strip().upper()

    chosen_airport = get_one_airport(target_ident)
    if not chosen_airport:
        print("No next stop selected.")
        return None

    choice_next_stop = chosen_airport

    distance = haversine(
        float(current_user["latitude_deg"]),
        float(current_user["longitude_deg"]),
        float(chosen_airport["latitude_deg"]),
        float(chosen_airport["longitude_deg"])
    )

    insert_km(current_user, distance)
    return choice_next_stop


<<<<<<< HEAD
=======


>>>>>>> nipa_1
def insert_km(user, distance):
    user_id = user["id"]
    KM = float(distance)

<<<<<<< HEAD
    query = """
            UPDATE users
            SET KM = COALESCE(KM, 0) + %s
            WHERE id = %s \
            """
    run_query(query, (KM, user_id))

    check = run_query("SELECT KM FROM users WHERE id = %s", (user_id,), fetchone=True)
=======
    run_query(query("update_user_km"), (KM, user_id))

    check = run_query(query("get_user_km",), (user_id,), fetchone=True)
>>>>>>> nipa_1
    total_km = check["KM"] if check else 0

    if 1000 <= total_km <= 100000:
        membership = "Gold"
    elif total_km > 100000:
        membership = "Diamond"
    else:
        membership = "Silver"

<<<<<<< HEAD
    membership_query = """
                       UPDATE users
                       SET membership = %s
                       WHERE id = %s \
                       """
    run_query(membership_query, (membership, user_id))

    print("\n=====  =====")
    print(f"{user['username']}, you have traveled an additional {KM:.2f} km.")
    print(f"Total distance traveled with us: {total_km:.2f} km.")
    print(f"Current membership: {membership}")
    print("==============================\n")
=======
    run_query(query("update_user_membership"), (membership, user_id))

    user["membership"] = membership
    user["KM"] = total_km
    user_update()
    

    print("\n==========================")
    print(f"{user['username']}, you have traveled an additional {KM:.2f} km.")
    print(f"Total distance traveled with us: {total_km:.2f} km.")
    print(f"Current membership: {membership}")
    print("============================\n")

>>>>>>> nipa_1


def user_info(current_user):
    print("\n===== User Information =====")
    print(f"Username       : {current_user.get('username', 'Unknown')}")
    print(f"Email          : {current_user.get('email', 'Unknown')}")
    print(f"Location       : {current_user.get('location', 'Unknown')}")
    print(f"Battery        : {current_user.get('battery', 0)}%")
    print(f"Travelled      : {current_user.get('KM', 0)} km")
    print(f"membership     : {current_user.get('membership')}")
    print("==============================\n")


def user_logout():
    try:
        global current_user
        print(f" User {current_user['username']}  logged out.")
        current_user = None
    except Exception as e:
        print(f"An Err {e}")


<<<<<<< HEAD
=======

>>>>>>> nipa_1
