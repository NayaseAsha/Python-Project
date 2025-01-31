import os
class newcar:
    def __init__(self, id="", name="", type="", seat="", rent=""):
        self.c_id = id
        self.c_name = name
        self.c_type = type
        self.c_seat = seat
        self.c_rent = rent 

    def display(self):
        print("Car ID : ", self.c_id)
        print("Car Brand & model  : ", self.c_name)
        print("Type : ", self.c_type)
        print("Seat : ", self.c_seat)
        print("rent : ", self.c_rent)

    def __str__(self):
        data = str(self.c_id) + "," + self.c_name + "," + self.c_type + "," + self.c_seat+ "," + self.c_rent
        return data

if __name__ == "__main__":
    c1 = newcar()  
    c1.display()