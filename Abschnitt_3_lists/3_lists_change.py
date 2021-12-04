animals = ["Zebra", "Gans", "Elefant", "Giraffe", "Nashorn"]
print(animals)

animals[1] = "Gepard"
print(animals)

animals[0] = "" # creates an empty index
print(animals)

animals[0] = "Zebra"
print(animals)

animals2 = [] #empty list
print(animals2)

# APPEND @ end of list
animals2.append("Zebra")
print(animals2)
animals2.append("Elefant")
print(animals2)

# INSERT at specific index
animals2.insert(1, "Gepard")
print(animals2)

# REMOVE last object form list
animals2.pop()
print(animals2)

#REMOVE specific obj. from list
del animals2[0] # statement (nicht Funktion)
#or
#animals2.pop(0) # pop-Funktion ist zu verwenden, wenn entferntes Obj. in einer Variablen (zwischen-)gespeichert werden soll:
removedObject = animals2.pop(0)
print(animals2)
print(f"Removed: {removedObject}")


#REMOVE by value
animals2 = ["Zebra", "Gans", "Elefant", "Giraffe", "Nashorn"]
print(animals2)
animals2.remove("Zebra")
print(animals2)