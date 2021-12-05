class Vehicle:
    def __init__ (self, max_speed, door_count):
        self.max_speed = max_speed
        self.door_count = door_count
    
    def drive(self):
        print("The Vehicle is driving.")

class Plane(Vehicle):
    def __init__ (self, max_speed, door_count, wing_lenght):
        super().__init__(max_speed, door_count)
        self.wing_lenght = wing_lenght
        
    def start_landing(self):
        print("Plane is landing")

    def drive(self):
        print("The Plane is flying.")