# Python Dictionary Methods Practice

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}

# Original Dictionary
print("Original Dictionary:")
print(marks)


# 1. len()
print("\nLength of Dictionary:")
print(len(marks))


# 2. items()
print("\nDictionary Items:")
print(marks.items())


# 3. keys()
print("\nDictionary Keys:")
print(marks.keys())


# 4. values()
print("\nDictionary Values:")
print(marks.values())


# 5. get()
print("\nMarks of Harry:")
print(marks.get("Harry"))


# 6. update()
marks.update({"Harry": 99})
print("\nAfter update():")
print(marks)


# 7. pop()
marks.pop("Rohan")
print("\nAfter pop():")
print(marks)


# 8. popitem()
marks.popitem()
print("\nAfter popitem():")
print(marks)


# 9. clear()
marks.clear()
print("\nAfter clear():")
print(marks)