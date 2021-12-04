print("Welcome! Please introduce yourself")

students = []

user_input = ""

while user_input != "Exit":
    user_input = input("What ist your name?")
    
    if user_input != "Exit":
        students.append(user_input)
        print(f"Hello {user_input}")

all_students = ""
i = 0
for student in range(len(students)):
    all_students += students[i] + ", "
    i += 1
print(f"{all_students}thank you for introducing yourselves. Let´s begin!")