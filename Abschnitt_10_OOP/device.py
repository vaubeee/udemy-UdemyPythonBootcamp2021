class Device:
    def __init__(self, name):
        self.name = name
        
    def function(self):
        print("Main functionalty")        

class Vacuum(Device):
    def __init__ (self, name, watts):
        super().__init__(name)
        self.watts = watts
    
    def function(self):
        print("Hoover")

class WashingMachine(Device):
    def __init__ (self, name, watts, rpm):
        super().__init__(name)
        self.watts = watts
        self.rpm = rpm
        
    def function(self):
        print("Wash laundry")