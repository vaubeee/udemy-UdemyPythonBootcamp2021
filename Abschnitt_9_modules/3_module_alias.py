from car_functions import add_car, drive as drive_from_module, driver, act_speed #"as = alias für drive aus modul"
'''oder für import aller funcs aus dem modul: 
from car_functions import * (dann aber keine as alias Anweisung möglich)
'''
cars = []

def drive(): # programm func identisch mit module func führt zum ovveride - zu vermeiden mit alias siehe oben
    print("override der modul func drive()")

my_car = add_car("Volvo", "silver", 10_000)
cars.append(my_car)
my_car = add_car("BMW", "black", 10_000, 3)
cars.append(my_car)
my_car = add_car("Porsche", "white", 90_000, 2)
cars.append(my_car)
print(cars)

drive() #program func

drive_from_module() # alias module func
driver("Volker")
act_speed(120)