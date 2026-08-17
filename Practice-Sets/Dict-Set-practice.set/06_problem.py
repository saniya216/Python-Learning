
# Allow 4 friends to enter their favorite language as value
# and use key as their names.
# Assume that the names are unique.

s = {}

name = input("Enter your name: ")
lang = input("Enter your favourite language name: ")
s.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favourite language name: ")
s.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favourite language name: ")
s.update({name: lang})

name = input("Enter your name: ")
lang = input("Enter your favourite language name: ")
s.update({name: lang})

print(s)