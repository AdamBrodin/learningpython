colors = ["Red", "Green", "Blue", "Yellow", "Black",
          "White", "Purple", "Cyan", "Indigo", "Orange", "Brown"]

# simple for loop, going through each item in the list
i = 0
for color in colors:
    # only do this for the first item in the list
    if i == 0:
        print("I like the color " + color.title() + " but also.. ")
    elif i + 1 >= len(colors):
        print("and finally " + color.title())
    else:
        print(color.title() + ",")

    # increment the "index tracker" by 1
    i += 1

# prints the numbers 1 through 101 --> which becomes 100 (does not loop through the last number)
for value in range(1, 101):
    print("Let's count to 100: " + str(value))

# store the range of numbers in a list
numbers = list(range(1, 1001))
print("Now, let's count to 1000. \n" + str(numbers))

print("Now, let's check which ones are even.")
# creates a new list which only creates every other number, step = 2
evenNumbers = list(range(1, len(numbers), 2))
print("Even number: " + str(evenNumbers))

print("\nAnd finally let's add all the even numbers up, totalling a whopping: " +
      str(sum(evenNumbers)))

    
