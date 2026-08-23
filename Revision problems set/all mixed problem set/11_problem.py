a = int(input("Enter a first num : "))
b = int(input("Enter a second num : "))
c = int(input("Enter third num : "))

if a > b and a > c:
    print("Greatest number is ", a)
elif b > a and b > c:
    print("Greatest number is ", b)
else:
    print("Greatest number is ", c)