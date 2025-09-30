from Queries.user import  user_register,user_login,user_delete,next_stop

def main():
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
            user_login()
              
        elif choice == "3":
                next_stop()

        elif choice == "9":
                user_delete()
    
        elif choice == "10":
                print("Goodbye!")
                break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()


