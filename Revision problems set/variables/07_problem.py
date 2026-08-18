 #To find the largest of 3 numbers given by the user

#method1

num1 = int(input("Enter first num : "))
num2 = int(input("Enter second num : "))
num3 = int(input("Enter third num : "))

largest = max(num1 , num2 , num3)
print("Largest number is", largest)



#Method 2 

num1 = int(input("Enter first num : "))
num2 = int(input("Enter second num : "))
num3 = int(input("Enter third num : "))

if num1 > num2 and num1 > num3:
    print(num1 ,"is largest number")
elif num2 > num1 and num2 > num3:
    print(num2 ,"is largest number")
else:
    print(num3 ,"is largest number")

