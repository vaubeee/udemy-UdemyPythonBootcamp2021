from carclass import Car

my_car = Car("Audi", "Black", "WKN424631958")
my_car.describe()
my_car.drive()

print(f"Actual speed: {my_car.speed}")
my_car.speed = my_car.speed + 20
print(f"Actual speed: {my_car.speed}")

my_car.set_speed(300)
print(f"Set speed: {my_car.speed} km\h")

for i in range(1,11):
    my_car.increase_speed(10)
    print(f"Increase speed {my_car.speed} km\h")
    i+=1
print(f"Speed {my_car.speed} km\h")
