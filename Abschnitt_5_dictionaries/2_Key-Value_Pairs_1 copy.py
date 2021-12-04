person = { "name" : "Volker", "age" : 48, "height" : 173 }
print(person)

person["height"] = 174
print(person)

person["DoB"] = "06.11.1973"
print(person)

person["Partner"] = {"name" : "Solveig", "age" : 51, "married" : True}
print(f"{person['name']}'s partner: {person['Partner']['name']}, {person['Partner']['age']}, married: {person['Partner']['married']}")

