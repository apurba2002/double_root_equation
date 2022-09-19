import math

def root  (a,b,c):
    determiner = (b*b)-4*a*c
    if (determiner < 0):
        print("complex")
    else:
        x1 = ((-b + math.sqrt(determiner))// 2*a)

        x2 = ((-b - math.sqrt(determiner))// 2*a)
        print("(",x1,",",x2,")")

while True:
    a = float(input("Enter the value of a :-"))
    b = float(input("Enter  the value of b :-"))
    c = float(input("Enter the value of c :-"))
    root(a,b,c)