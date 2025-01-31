from carfun import car
from carentry import newcar
import os
from prettytable import PrettyTable

# def show_car_data():
#     if os.path.exists('car.txt'):
#         table = PrettyTable()
#         table.field_names = ["Car ID", "Car Name", "AC/Non-AC", "Seats Available", "Rent Per Day"]
#         with open("car.txt", "r") as file:
#             for line in file:
#                 car_info = line.strip().split(",")
#                 table.add_row(car_info)
#         print("Car Details:")
#         print(table)
    # else:
    #     print("Car file does not exist")

def show_user_data():
    if os.path.exists('userdeat.txt'):
        table = PrettyTable()
        table.field_names = ["Username", "Password"]
        with open("userdeat.txt", "r") as fp:
            for line in fp:
                username, password = line.strip().split(",")
                table.add_row([username, password])
        print("User Details:")
        print(table)
    else:
        print("User file does not exist")

if __name__ == "__main__":
    choice = 0
    c1 = car()
    while choice != 8:
        print("                 Welcome Admin")
        print("_________*__Please choice your option___*_________\n")
        print("\t\t1. Display available cars")
        print("\t\t2. Add car")
        print("\t\t3. Search for Car using id ")
        print("\t\t4. Remove any car")
        print("\t\t5. Update any car")
        print("\t\t6. Payment ")
        print("\t\t7. User Details ")
        print("\t\t8. Exit\n")

        choice = int(input("Enter your option : "))
        print()
        if choice == 1:
            c1.show_car_data()
        elif choice == 2:
            print("\n You can add a new car to your service ")
            c_id = int(input("enter c_id : "))
            
            
            c1.add_car(c_id)
        elif choice == 3:
            print("Search for available car")
            c_id = int(input('Enter the car Id  to search '))
            c1.search_car(c_id)
            print()
        elif choice == 4:
            print("Now you can remove a car \n")
            c_id = int(input("enter c id to remove it "))
            c1.remove_car(c_id)
            c1.show_car_data()
        elif choice == 5:
            print("You can update car details using car id")
            c_id = int(input("enter c id  to update details : "))
            c1.updatecar(c_id)
        elif choice == 6:
            c_id = int(input("enter c id to book car : "))
            c1.payment(c_id)
        elif choice == 7:
            show_user_data()
        elif choice == 8:
            print("_______Thank you for visiting our service______")
