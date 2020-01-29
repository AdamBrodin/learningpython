# list basics #
colors = ["Red", 1, 3.1415]
# initializing a list starts at index 0, can contain any type of variable/value
print(colors)
# print the entire list
print("Value of index 1: " + str(colors[1]))
# print specific index of list
print("List length: " + str(len(colors)))
# len returns the length of the list

# editing lists #
colors[0] = "Blue"
# modified the first index of the list
print("\nUpdated color is: " + str(colors[0]))

colors.append("Orange")
# append() adds a new item to the list at index == length of list (last index)
print("Appended list: " + str(colors))

colors.insert(2, "Green")
# insert() adds a new item to the list at a specific index
print("New list: " + str(colors))
print("Index 2 of colors: " + str(colors[2]))

del colors[0]
# del removes the object from the list at the specified index
print("Deleted index [0], new list: " + str(colors))
