# list basics #
colors = ["Red", 1, 3.1415]
# initializing a list starts at index 0, can contain any type of variable/value
# print the entire list
print(colors)
# print specific index of list
print("Value of index 1: " + str(colors[1]))
# len returns the length of the list
print("List length: " + str(len(colors)))

# editing lists #
# modified the first index of the list
colors[0] = "Blue"
print("\nUpdated color is: " + str(colors[0]))

# append() adds a new item to the list at index == length of list (last index)
colors.append("Orange")
print("Appended list: " + str(colors))

# insert() adds a new item to the list at a specific index
colors.insert(2, "Green")
print("New list: " + str(colors))
print("Index 2 of colors: " + str(colors[2]))

# del removes the object from the list at the specified index
del colors[0]
print("Deleted index [0], new list: " + str(colors))

# pop() removes an object from index and returns it
removedObject = colors.pop(3)
print("Removed item: " + str(removedObject) + " at index 3")
print("New list layout: " + str(colors))

# remove() removes an object from the list by exact value, without knowing the index
colors.remove("Green")
print("New list layout: " + str(colors))

colors = ["Red", "Green", "Blue", "Purple", "Cyan"]
# sorted() temporarily sorts a list without actually altering the variable
print("Temporarily sorted list: " + str(sorted(colors)))

# sort() permanently sorts a list by changing it to ascending/descending order (alphabetical/numerical)
colors.sort()
print("Ascending order: " + str(colors))
# reverse = true parameter reverses the sorting
colors.sort(reverse=True)
print("Descending order:" + str(colors))

# get list values between specific index points
print("Names at index 3-4: " + str(colors[3:5]))

# print out the 2 last list index values
print("The two last colors are: " + str(colors[-2:]))
