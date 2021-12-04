person = { "name" : "Volker", "age" : 48, "height" : 173 }
print(person)

person["height"] = 174
print(person)

person["DoB"] = "06.11.1973"
print(person)

person["Partner"] = {"name" : "Solveig", "age" : 51, "married" : True}
print(f"{person['name']}'s partner: {person['Partner']['name']}, {person['Partner']['age']}, married: {person['Partner']['married']} \n")

# delete functions:
del person["height"]
print(person)

users = {
    "Volker" : False,
    #"Solveig" : True,
    "Lennart" : False    
}
print(f"User Status Ban: {users}")

#print(f"Is User Solveig banned? {users['Solveig']}")
#besser, da auch der case nicht vorhandener Werte aufgefangen wird:
print(f"Is User Solveig banned? {users.get('Solveig', 'No such user in dict!')}")




