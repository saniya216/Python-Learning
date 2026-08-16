letter = "Hello Sania"        #simple string example
print(letter)
print(type(letter))


a = "20"                      # using double quotes makes the value a string
print(a)
print(type(a))



# String slicing

#1)positive indexing
name = "Sania"
print(name[0:3])  # prints characters from index 0 to 2
print(name[1:])   # prints characters from index 1 to the end
print(name[:4])   # prints characters from the beginning to index 3
print(name[2:5])  # prints characters from index 2 to 4



#2)Negative indexing
name = "Sania"
print(name[-3:-1])  # prints characters from index -3 to -2
print(name[-5:-2])  # prints characters from index -5 to -3


#string slicing with skip value 
#(start:stop:step)

name = "Saniya"
print(name[-3:-1:2])  # prints characters from index -3 to -2 with step 2
print(name[-3:-1:1])  # prints characters from index -3 to -2 with step 1
print(name[0:4:3])  # prints characters from index 0 to 3 with step 3


