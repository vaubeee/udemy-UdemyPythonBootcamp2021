range_list= list(range(1, 100))

list_1 = []
list_2 = []

for value in range_list:
    if value % 5 == 0:
        list_1.append(value)
    else:
        list_2.append(value)

print(f"Liste 1: {list_1}, \nListe 2: {list_2}")

