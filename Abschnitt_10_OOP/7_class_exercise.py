from device import Device
from device import Vacuum
from device import WashingMachine

my_device = Device("Haushaltsgerät")
print(my_device.name)
my_device.function()

my_vacuum = Vacuum("Bosch Super-Hoover", 1200)
print(my_vacuum.name)
my_vacuum.function()
print(my_vacuum.watts)

my_washingMachine = WashingMachine("Siemens Mega-Wash", 3000, 1200)
print(my_washingMachine.name)
my_washingMachine.function()
print(my_washingMachine.watts)
print(my_washingMachine.rpm)



    