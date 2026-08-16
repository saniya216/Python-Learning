#tuple functions

#1 Create a tuple of 5 numbers and print it.
numbers = (10, 20, 30, 40, 50)
print(numbers)

#2 Print the first element of the tuple.
print(numbers[0])

#3 Find how many times 10 appears in the tuple.
numbers = (10, 20, 10 , 30, 10 , 40, 50, 10)
numbers.count(10)
print(numbers)


#4 Find the index of 30.
numbers = (10, 20, 30, 40, 50)
print(numbers.index(30))

#5 Find the number of elements in the tuple.
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

#6 slicing : Print the first 3 elements of the tuple.
numbers = (10, 20, 30, 40, 50)
print(numbers[0:3])