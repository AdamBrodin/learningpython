inputName = input("What's your name?: ")
inputAge = input("How old are you?: ")


if int(inputAge) >= 20 and inputName.title() == "Adam":
    print("Welcome!")
else:
    print("Sorry you may not come in.")
