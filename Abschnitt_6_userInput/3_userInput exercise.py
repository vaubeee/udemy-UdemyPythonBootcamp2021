persons = { "name" : "", "age" : 0, "height" : 0}

    persons["name"] = input("Vorname: ")
    persons["age"] = int(input("Alter: "))
    persons["height"] = int(input("Größe: "))
    
print(persons)

''' mein erster Versuch - fälschlicherweise mit List -> Dictionary:
persons = [
    { "name" : "", "age" : 0, "height" : 0}
    ]

for person in persons:
    for key, value in person.items():
        if key == "name" and value == "":
            person["name"] = input("Geben Sie den Vornamen ein: ")
        elif key == "age" and value == 0:
            person["age"] = input("Geben Sie das Alter in Jahren ein: ")
        elif key == "height" and value == 0:
            person["height"] = input("Geben Sie das Alter in Jahren ein: ")
        else:
            print("Error")
print(persons)
'''

