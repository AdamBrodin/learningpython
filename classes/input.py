correctUsername = "Adam"
correctPassword = "asdf1234"

# input() waits for a user text input before proceeding
inputUsername = input("Enter your username: ")
if inputUsername == correctUsername:
    inputPassword = input("Enter your password: ")
    if inputPassword == correctPassword:
        print("You are now logged in as " + inputUsername)
