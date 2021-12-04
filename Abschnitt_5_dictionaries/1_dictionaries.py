person = { "name" : "Volker", "age" : 48, "height" : 173 }
print(person['name'], person['age'], person['height'])
print(f"Name ist {person['name']} und Körpergröße ist {person['height']} \n")

persons = [
    { "name" : "Volker", "age" : 48, "height" : 173 },
    { "name" : "Solveig", "age" : 51, "height" : 183 },
    { "name" : "Lennart", "age" : 15, "height" : 185 }
    ]
for person in persons:
    print(f"Dein Name ist {person['name']} und deine Körpergröße ist {person['height']} cm. Du bist {person['age']} alt. \n")


