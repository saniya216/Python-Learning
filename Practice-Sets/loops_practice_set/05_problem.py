n = int(input("Enter a num : "))

for i in range(2,n):
    if n % i == 0:
        print("Non Prime no.")
        break
else:
    print("Prime No.")