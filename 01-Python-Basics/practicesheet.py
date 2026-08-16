# To find the largest of 3 numbers given by the user

# Method 1
a = int(input("Enter First Num :"))
b = int(input("Enter Second Num :"))
c = int(input("Enter Third Num :"))

if a >= b and a >= c:
    print(a, "is largest number")
elif b >= a and b >= c:
    print(b, "is largest number")
else:
    print(c, "is largest number")



# Method 2
a = int(input("Enter First Num :"))
b = int(input("Enter Second Num :"))
c = int(input("Enter Third Num :"))

largest = max(a, b, c)
print("Largest number is", largest)





# To find the smallest of 3 numbers given by the user

# Method 1
num1 = int(input("Enter First Num :"))
num2 = int(input("Enter Second Num :"))
num3 = int(input("Enter Third Num :"))

smallest = min(num1, num2, num3)
print("smallest number is", smallest)



# Method 2
num1 = int(input("Enter First Num :"))
num2 = int(input("Enter Second Num :"))
num3 = int(input("Enter Third Num :"))

if num1 <= num2 and num1 <= num3:
    print(num1, "is the smallest number")
elif num2 <= num1 and num2 <= num3:
    print(num2, "is the smallest number")
else:
    print(num3, "is the smallest number")



# Average of 3 numbers given by user

num1 = int(input("Enter first num :"))
num2 = int(input("Enter second num :"))
num3 = int(input("Enter third num :"))

avg = (num1 + num2 + num3) / 3
print("Average =", avg)



#Area of sqaure 

side = float(input("Enter side of a sqaure:"))
sqr = side * side
print("Area of square =", sqr)