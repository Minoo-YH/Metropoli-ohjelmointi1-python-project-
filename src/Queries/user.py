from context.run import run_query
from data_loader import get_users,update_user
users = None
current_user = None 


def get_user_by_name():
    global users,current_user
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
    
    ident= user.get("current_airport_of_user")
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


        
    













    
# def destination_airport():
#     global airport
#     if airport:
#         print(f" U R IN THIS airport :==> {airport[1]}")
#         print(f": U R IN THIS  Country:==> {airport[8]}")
#     all_airport_in_city = input("Type the country code where you want to travel (e.g., US, FI): ==> ")
# columns = [
#     "id", "ident", "type", "name", "latitude_deg", "longitude_deg", "elevation_ft",
#     "continent", "iso_country", "iso_region", "municipality", "scheduled_service",
#     "gps_code", "iata_code", "local_code", "home_link", "wikipedia_link", "keywords"
# ]



    
# def current_airport():

#     ident_user= get_user_by_name()
#     if not ident_user:
#         return
#     ident=ident_user.get("current_airport_of_user")
#     print("ident____" , ident)
#     airports = run_query(
#        "SELECT * FROM airport WHERE ident = %s",
#         (ident,)
#     )  
#     if airports:
#         airport = airports[0]  
#         print(f"Airport Name: {airport[3]}")
#         print(f"Location: {airport[10]}")
#         print(f"Country: {airport[8]}")
#         print(f"Coordinates: ({airport[4]}, {airport[5]})")
#     else:
#         print("No airport found.")