
#List Functions / Methods


#1 append() → Adds one element at the end
#2 extend() → Adds multiple elements
#3 remove() → Removes the first matching value
#4 pop() → Removes the last element
#5 count() → Counts occurrences of a value
#6 sort() → Sorts the list
#7 sum() → Returns the sum of all elements


#8 insert() → Adds an element at a specific index
#9 clear() → Removes all elements
#10 index() → Returns the index of a value
#11 reverse() → Reverses the list
#12 copy() → Creates a copy of the list


fruits = ["Apple", "Banana" ,"Mango"]

fruits.append("Orange")
print(fruits)

fruits.insert(1, "Strawberry")
print(fruits)

fruits.pop(2)
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(fruits.count("Strawberry"))

