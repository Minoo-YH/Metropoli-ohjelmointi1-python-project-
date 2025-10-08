from Queries.user import user_register, user_login, user_delete, next_stop, user_info, user_logout , current_user

def main():
    current_user = None
    print("=== Welcome to Finnair Booking System ===")
    print("To enjoy our services and book your flight, please register first ")
    while True:
        if not current_user:
            print("Choose an option:")
            print("1. Register")
            print("2. Login")
            print("10. Exit")
        else:
            print(f"\nWelcome, {current_user['username']}!")
            print("Choose an option:")
            print("3. Choose your destination")
            print("4. User info")
            print("8. Logout")
            print("9. Delete user")
            print("10. Exit")

        choice = input("Enter choice: ").strip()

        if not current_user:
            if choice == "1":
                user_register()
            elif choice == "2":
                result = user_login()
                if result:
                    from Queries.user import current_user as cu
                    current_user = cu
            elif choice == "10":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please register or login first.")
        else:
            if choice == "3":
                next_stop(current_user)
            elif choice == "4":
                user_info(current_user)
            elif choice == "8":
                user_logout()
                current_user = None
            elif choice == "9":
                user_delete()
                current_user = None
            elif choice == "10":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
