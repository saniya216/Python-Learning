#Write a program which finds out whether a given name is present in a list or not.
list = ["Sania", "Rohan", "Ali"]
name = input("Enter name:")

if name in list:
    print(name , "is present in list")
else:
    print(name , "is not present in list")