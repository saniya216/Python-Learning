#Welcome user

name = input("Enter your name : ")
print("Welcome ,", name)


#Addition using user input  (ADD)

num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))
sum = num1 + num2 
print("SUM =", sum)


#Area of Rectangle    (Multiplication)

Length = float(input("Enter the Length of Rectangle :"))
Width = float(input("Enter the width of Rectangle :"))
Area = Length * Width 
print("Area of Rectangle =", Area)


#Two number (DIV)

num1 = int(input("Enter a num:"))
num2 = int(input("Enter a num:"))
print("Division =", num1 / num2 )


#Area of Circle      

radius = float(input("Enter the radius of circle:"))
Area = 3.14 * (radius **2)                            #area of circle = pi*r*r   (pi = 3.14)
print("Area of circle =", Area)


#sqaure of the number

num = int(input("Enter the num:"))
sqr = num ** 2
print("Sqaure =", sqr)



#cube of the number 
num = int(input("Enter a num:"))
cube = num ** 3
print("cube =" , cube)


#AVERAGE
a = int(input("Enter a num:"))
b = int(input("Enter a num:"))
c = int(input("Enter a num:"))

average = (a + b + c / 3)

print("Average =" , average)



#marks 

maths = int(input("Enter Maths marks :"))
science = int(input("Enter science marks :"))
english = int(input("Enter English marks :"))

total = maths + science + english 

print("Total Marks =", total)


#city 

city = input("Enter your city name:")
print("Your city is " , city)


#student details 

name = input("Enter your name:")
age = int(input("Enter your age :"))
city = input("Enter your city :")

print(name)
print(age)
print(city)

first_name = input("Enter your first name:")
last_name = input("Enter your last name :")
print(first_name + " " + last_name)


#MIXED PRACTICE 

name = input("Enter your name:")
age = int(input("Enter your age:"))
city = input("Enter your city name:")
pincode = int(input("Enter your city Pincode:"))

print(name)
print(type(name))
print(age)
print(type(age))
print(city)
print(type(city))
print(pincode)
print(type(pincode))