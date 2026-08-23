num = int(input("Enter a num : "))

if num > 1:
 for i in range(2,num):
    if num % i == 0:
        print(num,"is not prime number")
        break
    else:
     print(num,"is prime number")
else:
   print(num , "is not a prime number")