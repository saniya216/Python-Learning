#1 Create a list of 5 numbers and print it.
numbers = [1, 2, 3, 4, 5]
print(numbers)

#2 Print the first element of the list
print(numbers[0])

#3 Print the last element of the list.
print(numbers[-1])
print(numbers[4])

#4 Change 20 to 25.
numbers_ = [10, 20, 30, 40]
numbers_[1] = 25
print(numbers_)

#5 Add 60 to the end of the list.
numbers_.append(60)
print(numbers_)

#6 Insert 25 at index 2 
numbers_.insert(2,25)
print(numbers_)

#7 Remove 30 from the list.
numbers_.remove(30)
print(numbers_)

#8 Remove the last element using pop().
numbers_.pop()
print(numbers_)

#9 Print the first three elements using slicing.
print(numbers[:3])

#10 Reverse the list.
numbers_.reverse()
print(numbers_)


#11 Sort the list in ascending order.
_numbers = [80, 50, 20, 30, 10]
_numbers.sort()
print(_numbers)

#12 Find how many times 10 appears in the list.
numbers = [ 10 , 20 , 10 , 50 , 10 , 100]
numbers.count(10)
print(numbers)

#13 Find the index of 30.
numbers = [ 10 , 20 , 30 , 40 , 50]
print(numbers.index(30))

#14 Check whether 50 is present in the list.
numbers = [10, 20, 30, 40, 50]
print(50 in numbers)

#15 Find the total number of elements in the list.
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

#16 Add the numbers [40, 50, 60] to the list [10, 20, 30].
numbers = [10, 20, 30]
new_numbers = [40, 50, 60]

numbers.extend(new_numbers)

print(numbers)
