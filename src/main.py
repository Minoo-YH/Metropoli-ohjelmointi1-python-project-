from Queries.user import user_register, user_login, user_delete, next_stop

def main():
    current_user = None
    print("=== Flight Game ===")
    while True:
        print("\nChoose an option:")
        print("1. user_register")
        print("2. user_login")
        print("3. choes UR destination")
        print("9. user_delete")
        print("10. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            user_register()
        elif choice == "2":
            result = user_login()
            if result:
                from Queries.user import current_user as cu
                current_user = cu
        elif choice == "3":
            if current_user:
                next_stop(current_user)
                
            else:
                print("Error: You must login first.")
        elif choice == "9":
            user_delete()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
