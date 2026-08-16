#1 Add two numbers 

num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))

SUM= num1 + num2 
print("SUM =", SUM)


#2 Find remainder when a number is divided by z

num1 = int(input("Enter a number: "))
z = int(input("Enter z (divisor): "))

Remainder = num1 % z
print("Remainder =", Remainder)

#3 Check the type of variable from input()

user_value = input("Enter Something :")

print("You Entered :", user_value)
print("Type of variabe :", type(user_value))


#4 check whether a is greater than b or not 

a = 34
b = 80

if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")


#5 Avg of two number 

num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))

AVG = (num1 + num2) / 2
print("Average =", AVG)


#6 Calculate square of a number

num = int(input("Enter a num:"))
print("Square =", num**2)