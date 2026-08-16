
#STRING METHODS / FUNCTIONS

#1) len() - returns the length of the string
name = "Sania"
print(len(name))

#2) lower() - converts the string to lowercase
name = "Sania"
print(name.lower())

#3) upper() - converts the string to uppercase
name = "Sania"
print(name.upper())

#4) strip() - removes whitespace from the beginning and end of the string
name = " Sania "
print(name.strip())

#5) split() - breaks the string into parts =returns a list of strings
name = "Sania, Alice, Bob"
print(name.strip().split())              

#6) capitalize() - capitalizes the first character of the string
name = "sania pathan"
print(name.strip().capitalize())

#7) title() - capitalizes the first character of each word in the string
name = "sania pathan"
print(name.strip().title())

#8) replace() - replaces a substring with another substring
name = "Sania"
print(name.replace("Sania", "Alice"))

#9) find() - returns the index of the first occurrence of a substring
word = "Hello, welcome to the world of Python!"
print(word.find("welcome"))

#10) count() - returns the number of occurrences of a substring
text = "python python java python"
print(text.count("python"))




#METHOD CHAINING   (FUNCTION / METHOD) = One by one methods can be added

text = "  hello PYTHON  "
print(text.strip().lower().capitalize())