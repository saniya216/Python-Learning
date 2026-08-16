#Arithmetic operators

a = 10 
b = 20 

print("Addition =", a + b)
print("Substraction =", a - b)
print("MUltiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Exponentiation =", a ** b)
print("Floor Division =", a // b)


#practice question
#01

num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))

sum = num1 + num2 

print("SUM =", sum)


#02
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
quotient = num1 // num2

print("Quotient =", quotient)


#03
num1 = int(input("Enter first num:"))
num2 = int(input("Enter second num:"))
avg = num1 + num2 / 2
print("Average =", avg)


#04
length = float(input("Enter the length of Rectangle :"))
width = float(input("Enter the width of Rectangle :"))
Area = length * width

print("Area of Rectangle =", Area)



#Assignment operators

x = 10
print("Initial value of x =", x)

x+= 5
print("After x += 5 =" , x)

x-=5
print("After x -= 5 =", x)

x*= 5
print("After x *= 5 =" , x)

x/= 5
print("After x /= 5 =", x)


#question practice
#01

x = 25
print("Initial value of x =", x)

x += 10
print("After  x + = 10 =" , x)             

x -= 5
print("After x -= 5 =" , x)

x *= 2                                 #double of the number
print("After x *= 2 =" , x)

x *= x                                  #sqaure of the number
print("After x *= x =" , x)

x /= 2
print("After x /= 2 =" , x)


#02

num = int(input("Enter a number :"))
print("Original Number =", num)

num += 10
print("After  x + = 10 =" , num)             

num -= 5
print("After x -= 5 =" ,num )

num *= 2                                 #double of the number
print("After x *= 2 =" , num)

num *= x                                  #sqaure of the number
print("After x *= x =" , num)

num /= 2
print("After x /= 2 =" , num)




#Comparison operators 

x = 10
b = 5

print("x == b =" , x == b)
print("x != b =" , x != b)
print("x > b =" , x > b)
print("x < b =" , x < b)
print("x >= b =" , x >= b)
print("x <= b =" , x <= b)


#question practice 
#01
x = 5
y = 2

print("x == y =", x == y)
print("x > y =" , x > y)
print("x < y =", x < y)

#02
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print("num1 == num2 =", num1 == num2 )
print("num1 != num2 =", num1 != num2)
print("num1 > num2 =", num1 > num2)
print("num1 < num2 =", num1 < num2)
print("num1 >= num2 =", num1 >= num2)
print("num1 <= num2 =", num1 <= num2)




#Logical operators 

a = 10

print("a > 5 and a < 15 =" , a > 5 and a < 15)
print( "a > 5 or a > 15 =" , a > 5 or a > 15)
print("not(a > 5 and a < 15) =", not(a > 5 and a < 15))

#practice question
age = int(input("Enter your age:"))
print( age >= 18 and age <= 60)
