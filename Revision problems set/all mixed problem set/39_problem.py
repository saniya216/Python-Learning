numbers = [-22, 34, -56, 79, -98, 99, -39, 67, 22, -57, 66]

positive = 0
negative = 0

for num in numbers :
    if num > 0:
        positive += 1
    else:
        negative += 1

print("Positive Numbers =", positive)
print("Negative Numbers =", negative)