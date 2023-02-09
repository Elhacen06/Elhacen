import math
a = float(input("entre le nomber  a = "))
b = float(input("entre le nomber b= "))
c = float(input("entre le nomber c = "))
delta =b**2 -4*a*c
if delta < 0 :
    print("pas de solution")
elif delta == 0 :
    x=(-b)/(2*a)
    print("la solution",x)
else :
    x1= (-b-math.sqrt(delta))/(2*a)
    x2= (-b+math.sqrt(delta))/(2*a)
    print(f"la solution delta = {delta} et x1= {x1 } et  x2={x2}")