
# Python Set Methods Practice

s = {1, 5, 32, 54, 5, 5, "Harry"}

print("Original Set:", s)
print("Type:", type(s))


# 1. add()
s.add(566)
print("\nAfter add():", s)


# 2. remove()
s.remove(1)
print("After remove():", s)


# 3. pop()
s.pop()
print("After pop():", s)


# 4. discard()
s.discard("Harry")
print("After discard():", s)


# 5. clear()
s.clear()
print("After clear():", s)


# Two new sets for set operations

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print("Set 1:", s1)
print("Set 2:", s2)


# 6. union()
print("Union:", s1.union(s2))


# 7. intersection()
print("Intersection:", s1.intersection(s2))


# 8. difference()
print("Difference:", s1.difference(s2))