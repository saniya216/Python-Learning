text = input("Enter a string : ")

count = 0

for ch in text:
    if ch in " ":
        count += 1
print("Total spaces =", count)