import sys, os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)



from src.services.user_service import register_user, login_user
from src.services.flight_service import show_flights, new_flight
from src.services.game_service import list_games, move_player

def menu():
    while True:
        print("\n=== 🌍 Flight Game Main Menu ===")
        print("1. Register user")
        print("2. Login user")
        print("3. List flights")
        print("4. Add flight")
        print("5. List games")
        print("6. Move player location")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            show_flights()
        elif choice == "4":
            new_flight()
        elif choice == "5":
            list_games()
        elif choice == "6":
            move_player()
        elif choice == "0":
            print("👋 Goodbye, Captain!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    menu()

