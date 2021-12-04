name = input("Vorname eingeben: ")
print(f"Dein Name ist: {name} \n")


number = input("Alter in Jahren eingeben: ")
number = int(number)
print(f"Dein Alter ist: {number} (ist string)\n") #ACHTUNG: STRING!

# als INT
number = input("Zahl eingeben: ")
number = int(number) + 10
print(f"int(number) + 10 = {number} \n")

# kürzer:
number_as_string = input("Number as string to int: ")
number_as_int = int(number_as_string)
print(f"Number as string: {number_as_string}")
print(f"Number as int: {number_as_int} \n")

number_as_string = input("Number as string to float: ")
number_as_float = float(number_as_string)
print(f"Number as string: {number_as_string}")
print(f"Number as float: {number_as_float} \n")


input("<<<Drücke eine Taste zum Beenden>>>")