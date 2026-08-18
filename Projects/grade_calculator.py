
maths = int(input("Enter Maths marks :"))
english = int(input("Enetr English Marks :"))
ai = int(input("Enter AI marks :"))
dbms = int(input("Enter DBMS marks :"))
python = int(input("Enter Python Marks :"))

total_marks = maths + english + ai + dbms + python
print("Total marks" , total_marks)

percentage = (total_marks / 500) * 100
print("Percentage =", percentage , "%")

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >=70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade =", grade)

if percentage >= 40:
    print("Result : Pass")
else:
    print("Result : Fail")