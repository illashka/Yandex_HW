a = int(input())
b = int(input())
c = int(input())

if c >= 0:
    if a == 0: 
        if b == c**2:
            print('MANY SOLUTIONS')         
        if b != c**2:
            print('NO SOLUTION')
    
    if a != 0:
        if ((c*c - b) // a) == ((c*c - b) / a):
            print((c*c - b) // a)
        else:
            print('NO SOLUTION')
else:
    print('NO SOLUTION')
