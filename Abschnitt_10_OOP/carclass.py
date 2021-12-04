class Car:
    def __init__(self, brand, color, fin):
        self.brand = brand
        self.color = color
        self.fin = fin
        self.speed = 0 #attribut ohne vorherige init

    def describe(self):
        print(f"Car description: Brand {self.brand}, Color {self.color}, FIN {self.fin}")
        
    def drive(self):
        print(f"Motion-Alarm: Your {self.color} {self.brand} with FIN {self.fin} is moving.")
    
    def increase_speed(self, add_val = 0):
        self.speed = self.speed + add_val
        
    def set_speed(self, new_val):
        if new_val > 299:
            print(f"Set Speed value {new_val} inadmissible!")
        else:
            self.speed = new_val
        
        
