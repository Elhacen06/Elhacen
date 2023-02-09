a = int(input("entre le nomber  a = "))
b = int(input("entre le nomber b= "))
c = int(input("entre le nomber c = "))

def plus_grand(a, b,c):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    return max_num


print("le plus grand ",plus_grand(a,b,c))