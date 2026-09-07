def greatest(a,b,c):
    if a > b and a > c:
        return a 
    elif b > a and b > c:
        return b 
    elif c > a and c > b:
        return c 

print("Greatest number is :", greatest(10,20,30))