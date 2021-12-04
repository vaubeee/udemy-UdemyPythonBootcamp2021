employees_salaries = []

user_input = ""
while True:
    user_input = input()
    if user_input == "Exit":
        break
        print("Eingaben beendet. Auf Wiedersehen!")
    else:
        user_input = "Geben Sie den Namen oder 'Exit' ein: "
        if user_input == "Exit":
            break
            print("Eingaben beendet. Auf Wiedersehen!")
        else:
            employee_name = user_input
        
        user_input = "Geben Sie das Gehalt oder 'Exit' ein: "
        if user_input == "Exit":
            break
            print("Eingaben beendet. Auf Wiedersehen!")
        else:
            employee_salary = int(user_input)
        
        employees_salaries = zip(employee_name, employee_salary)

print(employees_salaries)   