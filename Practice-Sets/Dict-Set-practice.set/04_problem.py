

# Q4. What will be the length of the following set?

s = set()

s.add(20)
s.add(20.0)
s.add("20")

print(s)
print("Length of set:", len(s))


# Explanation:
# 20 is an integer (int).
# 20.0 is a float.
# In Python, 20 == 20.0 is True.
# Therefore, 20 and 20.0 are treated as the same element in a set.
#
# "20" is a string (str), so it is different from 20 and 20.0.
#
# Therefore, the set contains only 2 unique elements.
#
# Answer: 2