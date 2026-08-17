#Write a program to find out whether a student has passed or failed 
# if it requires a total of 40% and at least 33% in each subject. 
# Assume 3 subjects and take marks as input from the user.


marks1 = int(input("Enter Python marks:"))
marks2 = int(input("Enter Java marks :"))
marks3 = int(input("Enter AI marks:"))

total_marks = marks1 + marks2 + marks3 
percentage = (total_marks/300)*100

if percentage >= 40 or marks1 > 30 or marks2 > 30 or marks3 > 30:
    print("You are pass", percentage ,"%")
else:
    print("You failed, try next year" , percentage ,"%")