users = {
    "Volker" : False,
    "Solveig" : True,
    "Lennart" : False    
}
#key und value
for key, value in users.items():
    print(f"User: {key} is banned: {value}")

# nur key
for key in users.keys():
    print(f"User: {key}")
  
# nur value
for value in users.values():
    print(f"User: {value}")
    
persons = [
    { "name" : "Volker", "age" : 48, "height" : 173, "married" : True },
    { "name" : "Solveig", "age" : 51, "height" : 183, "married" : True },
    { "name" : "Lennart", "age" : 15, "height" : 185, "married" : False }
    ]

for person in persons:
    for key, value in person.items():
        print(f"key: {key} and value: {value} \n")

for person in persons:
    for key in person.keys():
        print(f"key: {key} \n")
        
for person in persons:
    for value in person.values():
        print(f"value: {value} \n")

