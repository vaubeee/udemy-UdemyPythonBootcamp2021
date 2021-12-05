from vehicle import Vehicle, Plane

my_vehicle = Vehicle(800, 10)
print(my_vehicle.max_speed)
print(my_vehicle.door_count)
my_vehicle.drive()

my_plane = Plane(800, 10, 8)
my_plane.start_landing()
print(my_plane.wing_lenght)
my_plane.drive()
