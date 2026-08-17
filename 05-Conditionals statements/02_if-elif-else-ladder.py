#Write a Python program that asks the user to enter their age. Check and display the following:

#If the age is less than 0, print "You are entering invalid age".
#If the age is 0, print "You are entering 0 which is not valid age".
#If the age is 18 or above, print "You are above the age of consent".
#Otherwise, print "You are below the age of consent".

age = int(input("Enter your age: "))

if age < 0:
    print("You are entering an invalid age")

elif age == 0:
    print("You are entering 0, which is not a valid age")

elif age >= 18:
    print("You are above the age of consent")

else:
    print("You are below the age of consent")