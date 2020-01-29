# string basics #

# <-- hashtag for singleline comment (ignores the line when compiled)
# declaring two variables in one line -> set values at the end
firstname, lastname = "adam", "brodin"
name = firstname + " " + lastname

print("Hello, " + firstname)
print("#1 lastname is " + lastname.title())
print("Your full name is " + name.title())
# title() capitalises the first letter of each word in the string

favoriteMovie = "My favorite movie is Interstellar"
print(favoriteMovie)
# find() returns the index (place) of the input in the string
print("Interstellar index at: " + str(favoriteMovie.find("Interstellar")))

rageText = "I LOVE CAPSLOCK!!!"
print(rageText.lower())
# lower() makes the string all lowercase

# replacing, stripping and removing spaces & lines #
famousQuote = "\nSAY HELLO TO MY LITTLE FRIEND"
modifiedQuote = famousQuote.replace("FRIEND", "BOPE")
print(modifiedQuote.lower())
# replace() replaces text within a string with another string

spacedText = "     I like apples  "
print(spacedText.strip())
# strip() removes any white spaces/blanks in the beginning and end of a string | lstrip() for beginning | rstrip() for end

print("\n" + "bope")
print("\t bope")
# \n adds a new line to the string | \t adds a tab to the string
