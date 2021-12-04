animals = ["Zebra", "Affe", "Elefant", "Giraffe", "Nashorn"]

#temp sort
animal_sorted = sorted(animals)
print(f"New sorted temp: {animal_sorted}")
print(f"Original remaining unsorted: {animals}")

#permanet sort
animals.sort() # alphabetic sort
print(f"New Original permanently sorted: {animals}")
animals.sort(reverse = True) # reverse alphabetic sort
print(f"New Original permanently reverse sorted: {animals}")

# determine lenght of list
list_lengths = len(animals)
print(f"Lenght as int: {list_lengths}")






