#print table of given number using while loop


num = int(input("Enter a num : "))

i = 1
while i < 11:
    print( num , "*" , i , "=", num * i)
    i+=1


num = int(input("Enter a num : "))

for i in range(1, num+1):
    print(num , "*", i , "=", num * i)