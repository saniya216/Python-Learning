#Can we have a set with 18 (int) and "18" (str) as a value in it?

s = {18, "18"}

print(s)

#output  == {18, '18'}

#explanation :
#8 is an integer, while "18" is a string. Therefore, Python treats them as different values.