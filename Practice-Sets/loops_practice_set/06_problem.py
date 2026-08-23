n = int(input("Enter a number: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)



#for loop

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n + 1):
    sum += i
    print("Sum =", sum)

