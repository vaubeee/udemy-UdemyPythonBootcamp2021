from car_functions import add_car, drive, driver, act_speed

cars = []
my_car = add_car("Volvo", "silver", 10_000)
cars.append(my_car)
my_car = add_car("BMW", "black", 10_000, 3)
cars.append(my_car)
my_car = add_car("Porsche", "white", 90_000, 2)
cars.append(my_car)
print(cars)

drive() 
driver("Volker")
act_speed(120)

