#Nested if  - Nested if means an if statement inside another if statement.

#Write a Python program to input a number from the user. Check whether the number is even or odd. If the number is even, use a nested if statement to check whether the number is greater than 10 or not.


a = int(input("Enter a number: "))

if a % 2 == 0:
    print(a, "is an even number")

    if a > 10:
        print(a, "is greater than 10")
    else:
        print(a, "is 10 or less")

else:
    print(a, "is an odd number")