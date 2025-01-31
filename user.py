from carfun import car
from carentry import newcar

if __name__=='__main__':
 choice = 0
 c1 = car()
while (choice != 4):
         
         print("  _________*__Please choice your option___*_________\n")
         print("\t\t1. Display available cars")
         print("\t\t2. Search for Car using id")
         print("\t\t3. book for car enter id ")
         print("\t\t4. Exit ")
         
         
         
         choice = int(input("Enter your option : "))

         if choice ==1:
              print("The avalable cars list \n ")
              c1.show_car_data()
         if choice ==2:
              print("Search for available car")
              c_id =int(input('Enter the car to search '))
              c1.search_car(c_id)
         if choice == 3:
              c_id =int(input('Enter the car id to  book '))
              
              c1.remove_car(c_id)


              
              