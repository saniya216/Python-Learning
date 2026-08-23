#to print a pyramid using *

''' *
   ***
  *****
 *******
*********

'''


n = int(input("Enter a num : "))

for i in range( 1, n + 1):
    print(" " * ( n - i) + "*" * (2 * i - 1))