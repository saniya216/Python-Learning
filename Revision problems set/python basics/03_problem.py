#Write a Python program to print the content of a directory using OS module. Search online for the function which does that.

#use chatgpt 



# 1. Import os module
import os

# 2. Select directory
directory = r"C:\Users\Saniya\Desktop"

# 3. Get files and folders
contents = os.listdir(directory)

# 4. Print each item
for item in contents:
    print(item)