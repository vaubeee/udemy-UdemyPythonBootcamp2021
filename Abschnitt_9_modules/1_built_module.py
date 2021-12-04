import car_functions


cars = []
my_car = car_functions.add_car("Volvo", "silver", 10_000)
cars.append(my_car)
my_car = car_functions.add_car("BMW", "black", 10_000, 3)
cars.append(my_car)
my_car = car_functions.add_car("Porsche", "white", 90_000, 2)
cars.append(my_car)

print(cars)