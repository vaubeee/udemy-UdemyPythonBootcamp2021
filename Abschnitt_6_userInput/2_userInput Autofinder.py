cars = ["BMW", "Mercedes", "Volkswagen", "Audi", "Toyota"]

user_car = input("Welche Marke suchen Sie? ")

if user_car in cars:
    print(f"Die gewünschte Marke {user_car} ist verfügbar!")
else:
    print(f"Die gewünschte Marke {user_car} ist leider nicht verfügbar!")

