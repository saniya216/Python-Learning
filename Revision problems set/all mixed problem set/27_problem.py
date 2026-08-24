text = input("Enter a string : ")

count = 0

for ch in text:
    if ch == "a" or ch == "e" or ch =="i" or ch == "o" or ch == "u":
        count += 1

print("Total Vowels :", count)





#or 





text = input("Enter a string : ")

count = 0

for ch in text:
    if ch in "aeiou":
        count += 1
        
print("Total Vowels :", count)