#variante ohne return = create the car in der func
cars = []

def add_car(brand, color, price, doors = 5):
    car = {"brand" : brand, "color" : color, "price" : price, "doors" : doors}
    cars.append(car)
    
add_car("Volvo", "silver", 10_000)
add_car("BMW", "black", 10_000, 3)
add_car("Porsche", "white", 90_000, 2)
print(cars)

#variante mit return = create the car im program
cars_created = []
def create_car(brand, color, price, doors = 5):
    car = {"brand" : brand, "color" : color, "price" : price, "doors" : doors}
    return car

my_car = create_car("Volvo", "silver", 10_000)
cars_created.append(my_car)
my_car = create_car("BMW", "black", 10_000, 3)
cars_created.append(my_car)
my_car = create_car("Porsche", "white", 90_000, 2)
cars_created.append(my_car)
print(cars_created)