#Q9. Can you change the values inside a list which is contained in Set S?


# No, because a list is mutable
# and mutable objects cannot be stored in a set.

s = {8, 7, 12, "Harry", [1, 2]}

print(s)

# Output:
# TypeError: unhashable type: 'list'