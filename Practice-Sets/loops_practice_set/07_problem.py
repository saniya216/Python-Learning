#using while loop
#a)
n = int(input("Enter a num : "))

i = 1
fact = 1
while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =" ,fact)




#b) 
n = int(input("Enter a num : "))

i = 1
product = 1
while i <= n:
    product = product * i
    i = i + 1

print("Factorial =" ,product)




#using for loop 
#a)
n = int(input("Enter a num : "))


fact = 1
for i in range(1, n+1):
    fact = fact * i

print("Factorial =", fact)




#b)

n = int(input("Enter a num :"))

product = 1
for i in range(1,n+1):
      product = product * i

      print("Factorial =", product)