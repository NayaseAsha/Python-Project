import os

print("\n\tWelcome to our Car rental Service\n")

choice = int(input('\tSelect your login type\n\n\tPress 1: Admin login\n\tPress 2: User Login\n\n\tYour Input: '))

if choice == 1:
    print("\tWelcome to admin page \n\tPlease enter Login Id and password")
    login = input("\n\tPlease enter your Login ID: ")  # Admin Login ID : system1
    password = input("\n\tPlease enter your password: ")  # Admin Password : admin@123
    if login == "system1" and password == "admin@123":
        print("\n\tLogin successful\n")
        os.system("python admin.py")
    else:
        print("\n\tYour entered wrong credentials\n")
elif choice == 2:
    print("\tWelcome to car rental service\n")
    print("\tPress 1: For already registered user\n\tPress 2: For new User\n")
    inp = int(input("\tEnter your choice: "))
    if inp == 1:
        U_id = input("\tEnter your user id: ")
        pw = input("\tEnter your password: ")
        with open("userdeat.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                if U_id == username and pw == password:
                    print("\tLogin Successful!")
                    os.system("python user.py")  # Open user_interface.py after successful login
                    break
            else:
                print("\tOops! You have entered wrong credentials")
    elif inp == 2:
        U_id = input("\tEnter your new user id: ")
        pw = input("\tEnter your new password: ")
        with open("userdeat.txt", "a") as file:
            file.write(f"{U_id},{pw}\n")  # Save new user details on a new line
        print("\tNew User Registered Successfully!")
        os.system("python user.py")  # Open user_interface.py after successful registration
    else:
        print("\tInvalid Choice")
