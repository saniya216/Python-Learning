
#METHODS / FUNCTIONS 
#Example problem 01

text = "  hello python world   "

print("Original:", text)
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Titlecase:", text.title())
print("Replace:", text.replace("python","Java"))
print("Strip:", text.strip())
print("Split:", text.strip().split())
print("Capitalize:", text.strip().capitalize())


#Example problem 02

name = "Sania"
print("Name:", name)

city = "mumbai maharashtra"
print("Length:", len(city))

lang = "PYTHON"
print("Uppercase:", lang.upper())

sentence = " i am learning python programming"
print("Lowercase:", sentence.lower())

text = "I like Python"
print("Replace:", text.replace("Python", "Java"))

text = "   Hello World   "
print("Strip:", text.strip())

sentence = "Python is easy"
print("Split:", sentence.strip().split())

word = "hello saniii"
print("Split:", word.strip().capitalize())



#problem 03
#Take a name from the user and

name = input("Enter your name:")
print("Original name:", name)
print("Length :", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Capitalize:", name.strip().capitalize())


#problem 04
#Split the string using comma and print the second fruit.

data = "apple,mango,banana,grapes"  
fruits = data.strip().split(",")          #convert string into list 
print(fruits)
print(fruits[1])



#problem 05 
#What will be the output?

s = "  pyTHon  "
print(s.strip().capitalize())    #ouput :  Python


#FIND()
#01)
text = "hello python"
print(text.find("python"))


#02)



#COUNT()
#01)
text = "apple apple mango apple"
print(text.count("apple"))


#2)
word = "education"
count_vowels = (word.count("a") + word.count("e") +
                word.count("i") + word.count("o") +
                word.count("u"))
print(count_vowels)



#3)
s = "mississippi"

print(s.count("s"))
print(s.count("ss"))
print(s.count("i"))


#04)
text = "I love Python"       #space count (" ")
print(text.count(" "))    #output = 2


#05 
text = "Python python PYTHON"      #o/p = 1  
print(text.count("python"))         #Case-sensitive Case-sensitive hota hai