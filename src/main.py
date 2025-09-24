from Queries.user import  current_airport,battery_of_user,destination_airport

def main():
    print("=== Flight Game ===")
    while True:
        print("\nChoose an option:")
        print("1. destination_airport")
        print("2. Show Current Airport")
        print("3. Check Battery")
        print("10. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            destination_airport()
        elif choice == "2":
            current_airport()
        elif choice == "3":
            battery_of_user()
   
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()



