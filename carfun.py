import os
from prettytable import PrettyTable

class car():
    def add_car(self,c_id):
        print ("Provide details to update for car id",c_id)
        a = str(c_id)
        
        if os.path.exists('car.txt'):
            with open("car.txt", "r") as file:
                if a in file.read():
                    print("Car ID already exists. Please enter a unique ID.")
                    return False
                
        car_details = input("Enter car details (Name, Type, Seats, Rent): ")
        car_info = f"{a},{car_details}"
        with open("car.txt", "a") as file:
            file.write(car_info + '\n')

        print("New car details added successfully.")
        return True
    
    def search_car(self, c_id):
        if os.path.exists("car.txt"):
            with open("car.txt", "r") as fp:
                for i in fp:
                    if str(c_id) in i:
                        print('This car is available')
                        break
                else:
                    print("Sorry, Car not available at this moment")
        else:
            print("Sorry, file does not exist")
    
    def remove_car(self, c_id):
        if os.path.exists('car.txt'):
            allcar = []
            flag = False
            with open("car.txt", 'r') as fp:
                for i in fp:
                    if str(c_id) not in i:
                        allcar.append(i)
                    else:
                        flag = True
                
            if flag:
                with open("car.txt", "w") as fp:
                    for i in allcar:
                        fp.write(i)
                    print("The car with id", c_id, "is booked now")
            else:
                print("This record is not available to delete")
        else:
            print('File does not exist')

    def updatecar(self, c_id):
        if os.path.exists("car.txt"):
            allcar = []
            flag = False
            with open("car.txt", "r") as fp:
                for i in fp:
                    if str(c_id) in i:
                        i = i.split(",")
                        ans = input("Any change in name Y/N: ")
                        if ans.upper() == "Y":
                            i[1] = input("enter updated brand name : ")
                        ans = input("Any change in type of car Y/N : ")
                        if ans.upper() == "Y":
                            i[2] = input("enter type to update : ")
                        ans = input("Any change in num of seat  Y/N : ")
                        if ans.upper() == "Y":
                            i[3] = input("enter updated Seat capacity : ")
                        ans = input("Any change in num Rent  Y/N : ")
                        if ans.upper() == "Y":
                            i[3] = input("enter updated rent per day: ")
    
                        i = ",".join(i)
                        flag = True
                    allcar.append(i)
            if flag:
                with open("car.txt", "w") as fp:
                    for i in allcar:
                        fp.write(i)
            else:
                print("Record is not available")
        else:
            print("File does not exist")
    
    def book_car(self, c_id):
        if os.path.exists('car.txt'):
            allcar = []
            flag = False
            with open("car.txt", 'r') as fp:
                for i in fp:
                    if str(c_id) not in i:
                        allcar.append(i)
                    else:
                        flag = True
                
            if flag:
                with open("car.txt", "w") as fp:
                    for i in allcar:
                        fp.write(i)
            else:
                print("This record is not available to delete")
        else:
            print('File does not exist')
    def show_car_data(self):
     if os.path.exists('car.txt'):
        table = PrettyTable()
        table.field_names = ["Car ID", "Car Name", "AC/Non-AC", "Seats Available", "Rent Per Day"]
        with open("car.txt", "r") as file:
            for line in file:
                car_info = line.strip().split(",")
                table.add_row(car_info)
        print("Car Details:")
        print(table)
     else:
        print("Car file does not exist")

    def payment(self, c_id):
        c_rent = int(input("Enter the per day rent for your car : "))
        day = int(input("\nEnter the number of days you want to book : "))
        ext = int(input("\nIf any Extra charges: "))
        print("\n The final amount to be Paid for car id", c_id, ":", c_rent * day + ext,  " Ruppes \n\n_______Thank you for visiting our service______\n")

