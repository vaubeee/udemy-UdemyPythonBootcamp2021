print("Even or odd?")
print("Please enter a number or 'Exit' to quit programm.")
user_input = ""

while True:
    user_input = input()
    if user_input == "Exit":
        print("Auf Wiedersehen! \n")
        break
    else:
        digit = int(user_input)
        if digit % 2 == 0:
            print("Number is even \n")
            print("Next Number or 'Exit': ")
        else:
            print("Number is odd \n")
            print("Next Number or 'Exit': ")
