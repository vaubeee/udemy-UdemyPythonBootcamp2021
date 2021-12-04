
def log_student(name, major):
    print(f"Students name is {name}. His major subject is {major}.")

log_student("Programming", "Volker") # ergibt wegen verkehrter Reihenfolge der Argumente kein sinnvolles Ergebnis 
log_student(major = "Programming", name = "Volker") # feste Zuordnung = Reihenfolge egal