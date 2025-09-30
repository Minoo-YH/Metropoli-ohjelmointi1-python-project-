from context.run import run_query
from  Queries.airports import get_airports_iso_country,get_one_airport
import bcrypt

current_user = None
choice_next_stop = None


def user_register():
    try:
        global current_user

        username = input("Type username :=> ")
        email = input("Type email :=> ")
        password = input("Type password :=> ")
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        location = "EFHK"
        battery = 100.0

        query = """
            INSERT INTO users (username, email, password, location, battery)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (username, email, hashed_password.decode('utf-8'), location, battery)
        run_query(query, values)

        query_get_user = "SELECT * FROM users WHERE username = %s"
        current_user = run_query(query_get_user, (username,), fetchone=True)
        print("User registered successfully!")
    except Exception as e:
        print(F"An Err {e}")



def user_login():
    try:
        global current_user

        username = input("Enter username: ")
        password = input("Enter password: ")

        query = """
            SELECT id, username, email, password, location, battery, created_at
            FROM users
            WHERE username = %s
        """
        result = run_query(query, (username,), fetchone=True)

        if result:
            columns = ['id', 'username', 'email', 'password', 'location', 'battery', 'created_at']
            user = dict(zip(columns, result))

            stored_password = user['password']

            if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                user.pop('password', None)
                current_user = user
                print("LogIn successfully!")
                print(current_user)
                return True
            else:
                print("Wrong password")
                return False
        else:
            print("Wrong username")
            return False
    except Exception as e:
        print(F"An Err {e}")

def user_logout():
    try:
        global current_user
        print(f" User {current_user['username']}  logged out.")
        current_user= None
    except Exception as e:
        print(F"An Err {e}")



def user_delete():
    try:
        global current_user
        if current_user is not None:
            delete_input = input("Type Yes if you want to delete your account (Y): ").upper()
            if delete_input == "Y":
                query = "DELETE FROM users WHERE username = %s"
                values = (current_user,)

                run_query(query, values)
                print(f"User '{current_user}' deleted successfully!")
                current_user = None
            else:
                print("Account deletion canceled.")
        else:
            print("No user is currently logged in.")
    except Exception as e:
        print(F"An Err {e}")


def user_update():
    try:
        global current_user
        global choice_next_stop
        if not current_user or not choice_next_stop:
            print("Error: current_user or choice_next_stop not set.")
            return
        query = """
            UPDATE users
            SET battery = GREATEST(battery - 25, 0),
                location = %s
            WHERE id = %s
        """

        run_query(query, (str(choice_next_stop[0]), int(current_user["id"])))
        print(f"User {current_user['username']}   battery: {current_user['battery']}   {choice_next_stop[0]}.")
    except Exception as e:
        print(F"An Err {e}")


def user_update_battry():
    try:
        global current_user

        if not current_user :
            print("Error: current_user .")
            return

        query= """
            UPDATE users 
            SET battery = 100
            WHERE id = %s
    """
        current_user["battery"] = 100  
        run_query(query,(int(current_user["id"]),))
        print(f"User {current_user['username']} battery 100 .")
    except Exception as e:
        print(F"An Err {e}")


def next_stop():
    try:
        global choice_next_stop,current_user
        if current_user['battery'] <= 25:
            charging = input("UR battery under 25. You can not travel. If you want to charge, type (Y):=>").upper()
            if charging == "Y": 
                user_update_battry()
                current_user["battery"] = 100
                print(f"Your battery is {current_user['battery']}.")
            else:
                print("U can not travel.")
                return None

    
        destination_input = input("Where do you want to go? Type country code (e.g., FI, US, SW): ").upper()
        get_airports_iso_country(destination_input)
        choice_next_stop = get_one_airport()

        return choice_next_stop
    except Exception as e:
        print(F"An Err {e}")


def user_tabel():
    try:
        users=run_query("SELECT id, username, email,location,battery from users")
        for user in users:
            print(f"ID: => {user[0]},\n"
                f"username: => {user[1]},\n"
                f"email: => {user[2]},\n"
                f"location: => {user[3]},\n"
                f"battery: => {user[4]}")
    except Exception as e:
        print(F"An Err {e}")







