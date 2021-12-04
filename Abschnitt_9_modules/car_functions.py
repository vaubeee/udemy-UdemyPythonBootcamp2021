def add_car(brand, color, price, doors = 5):
    car = {"brand" : brand, "color" : color, "price" : price, "doors" : doors}
    return car

def drive():
    print("Car is driving.")
    
def driver(name):
    print(f"Driver: {name}")
    
def act_speed(speed):
    print(f"Actual speed: {speed}")