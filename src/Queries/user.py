from context.run import run_query
from data_loader import get_users,update_user
from  Queries.airports import get_airports_iso_country,get_one_airport
users = None
current_user = None 
user= None


def get_user_by_name():

    global users,current_user,user
    if current_user:
        return current_user
    if users is None:
        users= get_users()
    name_input= input("Type user name: ==> ").strip()
    for user in users :
        if user["name"] == name_input:
            print("UR data:")
            for key, value in user.items():
                print (f"{key}:==> {value}")
            current_user = user  
            return user
    print("User not found.")
    return None

def current_airport():
    user = get_user_by_name()
    if not user:
        return
   
   
    ident = user.get("location")[0]
    airports = run_query("SELECT * FROM airport WHERE ident = %s",(ident,))
    
    if airports:
        airport = airports[0]  
        print(f"Airport Name: {airport[3]}")
        print(f"Location: {airport[10]}")
        print(f"Country: {airport[8]}")
        print(f"Coordinates: ({airport[4]}, {airport[5]})")
    else:
        print("No airport found.")

def battery_of_user():
    global user
    user = get_user_by_name()
    
    if user:
        print(f"Battery: {user['battery']}%")

    if user['battery'] >= 25:
        print(f"You can travel. Battery: {user['battery']}%")
    
    elif user['battery'] < 25:
        print(f"You cannot travel. Battery: {user['battery']}%")
        charge_battery = input(
            "If you want to charge your battery to travel, type (Y/N): ").capitalize() 
        if charge_battery == "Y":
            user['battery'] = 100
            update_user(users) 
            
            print("Battery charged to 100%!")
        elif charge_battery == "N":
            print(f"{user['battery']}% is less than 25. You cannot travel.")
        else:
            print("Wrong input")

def destination_airport():
    user = get_user_by_name()
    destination_input = input("Where do you want to go? Type country code (e.g., FI, US, SW): ").upper()
    get_airports_iso_country(destination_input)
    user_data = get_one_airport() 

    if user_data:
        user['battery'] -= 25
        user['location'] = user_data  
        user['flights'] += 1
        update_user(users)
        print(f"Traveled to {user_data} \n. Battery: {user['battery']} \n, Flights: {user['flights']}")
    else:
        print("No airport selected. User data remains:")
        print(user)

